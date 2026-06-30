/*
 * Poker engine: hand evaluation + Monte Carlo equity.
 *
 * Card encoding: a card is an integer `rank * 4 + suit`.
 *   rank: 2..14  (11=J, 12=Q, 13=K, 14=A)
 *   suit: 0..3   (0=spades, 1=hearts, 2=diamonds, 3=clubs)
 * Valid card ints therefore run 8..59 (52 cards).
 *
 * Hand score: an integer where higher is better. Category occupies the high
 * digits (0=high card .. 8=straight flush) and the kickers a base-15 tail.
 */
(function (root) {
  'use strict';

  var RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
  var SUITS = [0, 1, 2, 3];

  function makeCard(rank, suit) { return rank * 4 + suit; }
  function cardRank(card) { return card >> 2; }
  function cardSuit(card) { return card & 3; }

  // Scratch count array reused across score5 calls (single-threaded).
  var _cnt = new Array(15).fill(0);
  var POW15_5 = 759375; // 15^5

  // Score the best (and only) 5-card hand made of five card ints.
  function score5(a, b, c, d, e) {
    var ra = a >> 2, rb = b >> 2, rc = c >> 2, rd = d >> 2, re = e >> 2;
    var sa = a & 3, sb = b & 3, sc = c & 3, sd = d & 3, se = e & 3;
    var flush = sa === sb && sb === sc && sc === sd && sd === se;

    var cnt = _cnt;
    cnt[ra]++; cnt[rb]++; cnt[rc]++; cnt[rd]++; cnt[re]++;

    // Present ranks in descending order.
    var gRank = [];
    var gCnt = [];
    for (var r = 14; r >= 2; r--) {
      if (cnt[r]) { gRank.push(r); gCnt.push(cnt[r]); }
    }
    var n = gRank.length;

    var straight = false, high = 0;
    if (n === 5) {
      if (gRank[0] - gRank[4] === 4) { straight = true; high = gRank[0]; }
      else if (gRank[0] === 14 && gRank[1] === 5) { straight = true; high = 5; } // wheel A-5
    }

    // Build tiebreak by group priority (count desc, then rank desc).
    var tb = 0, maxc = 0, secondc = 0, seen = 0;
    for (var wantc = 4; wantc >= 1; wantc--) {
      for (var i = 0; i < n; i++) {
        if (gCnt[i] === wantc) {
          if (seen === 0) maxc = wantc; else if (seen === 1) secondc = wantc;
          seen++;
          tb = tb * 15 + gRank[i];
        }
      }
    }

    var cat;
    if (straight && flush) cat = 8;
    else if (maxc === 4) cat = 7;
    else if (maxc === 3 && secondc === 2) cat = 6;
    else if (flush) cat = 5;
    else if (straight) cat = 4;
    else if (maxc === 3) cat = 3;
    else if (maxc === 2 && secondc === 2) cat = 2;
    else if (maxc === 2) cat = 1;
    else cat = 0;
    if (cat === 8 || cat === 4) tb = high;

    // Reset scratch counts.
    cnt[ra]--; cnt[rb]--; cnt[rc]--; cnt[rd]--; cnt[re]--;

    return cat * POW15_5 + tb;
  }

  // Best 5-card score among any 5 of the given cards (n = 5..8).
  function bestAny5(cards) {
    var n = cards.length;
    if (n < 5) return -1;
    var best = -1, s;
    for (var i = 0; i < n - 4; i++)
      for (var j = i + 1; j < n - 3; j++)
        for (var k = j + 1; k < n - 2; k++)
          for (var l = k + 1; l < n - 1; l++)
            for (var m = l + 1; m < n; m++) {
              s = score5(cards[i], cards[j], cards[k], cards[l], cards[m]);
              if (s > best) best = s;
            }
    return best;
  }

  // Omaha: exactly 2 of the hole cards + exactly 3 of the board.
  function bestOmaha(hole, board) {
    var best = -1, s;
    for (var i = 0; i < hole.length - 1; i++)
      for (var j = i + 1; j < hole.length; j++) {
        var h0 = hole[i], h1 = hole[j];
        for (var a = 0; a < board.length - 2; a++)
          for (var b = a + 1; b < board.length - 1; b++)
            for (var c = b + 1; c < board.length; c++) {
              s = score5(h0, h1, board[a], board[b], board[c]);
              if (s > best) best = s;
            }
      }
    return best;
  }

  // Evaluate a player's best hand given their hole cards, the 5-card board,
  // and the game type. Returns an integer score.
  function evaluate(hole, board, game) {
    if (game === 'omaha') return bestOmaha(hole, board);
    // holdem & pineapple: any combination of hole + board.
    return bestAny5(hole.concat(board));
  }

  /*
   * Monte Carlo equity.
   *   hole      : array of known hole card ints (length must equal holeCount)
   *   board     : array of 0..5 known community card ints
   *   game      : 'holdem' | 'pineapple' | 'omaha'
   *   opponents : number of opposing players (each dealt holeCount cards)
   *   holeCount : cards per player (2 holdem, 3 pineapple, 4 omaha)
   *   iters     : simulation count
   * Returns { win, tie, lose, equity } as percentages (0..100).
   */
  function simulate(hole, board, game, opponents, holeCount, iters) {
    var used = {};
    var i, c;
    for (i = 0; i < hole.length; i++) used[hole[i]] = true;
    for (i = 0; i < board.length; i++) used[board[i]] = true;

    var deck = [];
    for (c = 8; c < 60; c++) if (!used[c]) deck.push(c);
    var deckLen = deck.length;

    var needBoard = 5 - board.length;
    var needTotal = needBoard + opponents * holeCount;

    var winCount = 0;
    var tieEquity = 0; // accumulated split shares
    var loseCount = 0;

    var fullBoard = new Array(5);
    var oppHole = new Array(holeCount);

    for (var it = 0; it < iters; it++) {
      // Partial Fisher-Yates: draw `needTotal` cards from the deck.
      for (i = 0; i < needTotal; i++) {
        var j = i + ((Math.random() * (deckLen - i)) | 0);
        var tmp = deck[i]; deck[i] = deck[j]; deck[j] = tmp;
      }

      // Compose the full board.
      for (i = 0; i < board.length; i++) fullBoard[i] = board[i];
      for (i = 0; i < needBoard; i++) fullBoard[board.length + i] = deck[i];

      var myScore = evaluate(hole, fullBoard, game);

      var idx = needBoard;
      var bestOpp = -1, ties = 0;
      for (var o = 0; o < opponents; o++) {
        for (var h = 0; h < holeCount; h++) oppHole[h] = deck[idx++];
        var os = evaluate(oppHole, fullBoard, game);
        if (os > bestOpp) bestOpp = os;
      }

      if (myScore > bestOpp) {
        winCount++;
      } else if (myScore === bestOpp) {
        // Count opponents tied at the top to split the pot.
        idx = needBoard;
        ties = 0;
        for (var o2 = 0; o2 < opponents; o2++) {
          for (var h2 = 0; h2 < holeCount; h2++) oppHole[h2] = deck[idx++];
          if (evaluate(oppHole, fullBoard, game) === bestOpp) ties++;
        }
        tieEquity += 1 / (ties + 1);
      } else {
        loseCount++;
      }
    }

    var win = (winCount / iters) * 100;
    var tie = (tieEquity / iters) * 100;
    var lose = (loseCount / iters) * 100;
    return { win: win, tie: tie, lose: lose, equity: win + tie };
  }

  var api = {
    RANKS: RANKS, SUITS: SUITS,
    makeCard: makeCard, cardRank: cardRank, cardSuit: cardSuit,
    score5: score5, bestAny5: bestAny5, bestOmaha: bestOmaha,
    evaluate: evaluate, simulate: simulate
  };

  // Expose on global (browser/worker) and module (node tests).
  for (var key in api) root[key] = api[key];
  if (typeof module !== 'undefined' && module.exports) module.exports = api;

})(typeof self !== 'undefined' ? self : this);
