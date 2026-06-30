/* UI logic for the Poker Odds PWA. Tap-only — no text inputs anywhere. */
(function () {
  'use strict';

  var SUIT_SYM = ['♠', '♥', '♦', '♣']; // ♠ ♥ ♦ ♣
  var SUIT_RED = [false, true, true, false];
  var RANK_LBL = { 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A' };
  var RANK_ORDER = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2];
  var HOLE_COUNT = { holdem: 2, pineapple: 3, omaha: 4 };
  var ITERS = 30000;

  // ---- State ----------------------------------------------------------------
  var state = {
    game: 'holdem',
    opponents: 1,
    hole: [null, null],           // length follows game
    board: [null, null, null, null, null] // flop1,flop2,flop3,turn,river
  };

  function loadState() {
    try {
      var s = JSON.parse(localStorage.getItem('pokerOdds'));
      if (s && s.game && HOLE_COUNT[s.game]) {
        state.game = s.game;
        state.opponents = Math.min(9, Math.max(1, s.opponents | 0)) || 1;
        state.hole = (s.hole || []).slice(0, HOLE_COUNT[s.game]);
        while (state.hole.length < HOLE_COUNT[s.game]) state.hole.push(null);
        state.board = (s.board || []).slice(0, 5);
        while (state.board.length < 5) state.board.push(null);
      }
    } catch (e) { /* ignore */ }
  }
  function saveState() {
    try { localStorage.setItem('pokerOdds', JSON.stringify(state)); } catch (e) { /* ignore */ }
  }

  // ---- Helpers --------------------------------------------------------------
  function usedCards(exclude) {
    // Set of all assigned cards, optionally excluding one slot ref.
    var set = {};
    var i;
    for (i = 0; i < state.hole.length; i++) {
      if (state.hole[i] != null && !(exclude && exclude.type === 'hole' && exclude.index === i))
        set[state.hole[i]] = true;
    }
    for (i = 0; i < state.board.length; i++) {
      if (state.board[i] != null && !(exclude && exclude.type === 'board' && exclude.index === i))
        set[state.board[i]] = true;
    }
    return set;
  }

  function getSlot(target) {
    return target.type === 'hole' ? state.hole[target.index] : state.board[target.index];
  }
  function setSlot(target, card) {
    if (target.type === 'hole') state.hole[target.index] = card;
    else state.board[target.index] = card;
  }

  // ---- Rendering ------------------------------------------------------------
  var handRow = document.getElementById('handRow');
  var flopRow = document.getElementById('flopRow');
  var turnRow = document.getElementById('turnRow');
  var riverRow = document.getElementById('riverRow');

  function makeSlotEl(target) {
    var card = getSlot(target);
    var el = document.createElement('div');
    el.className = 'card-slot ' + (card == null ? 'empty' : 'filled');
    if (card != null) {
      var rank = card >> 2, suit = card & 3;
      el.classList.add(SUIT_RED[suit] ? 'red' : 'black');
      var r = document.createElement('div'); r.className = 'c-rank'; r.textContent = RANK_LBL[rank];
      var s = document.createElement('div'); s.className = 'c-suit'; s.textContent = SUIT_SYM[suit];
      el.appendChild(r); el.appendChild(s);
    }
    el.addEventListener('click', function () { openPicker(target); });
    return el;
  }

  function render() {
    // Game segments
    var segs = document.querySelectorAll('#gameSeg .seg');
    segs.forEach(function (b) { b.classList.toggle('active', b.dataset.game === state.game); });

    // Opponents
    document.getElementById('oppVal').textContent = state.opponents;
    document.getElementById('oppPlural').textContent = state.opponents === 1 ? '' : 's';

    // Hand slots
    handRow.innerHTML = '';
    for (var i = 0; i < state.hole.length; i++) handRow.appendChild(makeSlotEl({ type: 'hole', index: i }));

    // Board slots
    flopRow.innerHTML = ''; turnRow.innerHTML = ''; riverRow.innerHTML = '';
    flopRow.appendChild(makeSlotEl({ type: 'board', index: 0 }));
    flopRow.appendChild(makeSlotEl({ type: 'board', index: 1 }));
    flopRow.appendChild(makeSlotEl({ type: 'board', index: 2 }));
    turnRow.appendChild(makeSlotEl({ type: 'board', index: 3 }));
    riverRow.appendChild(makeSlotEl({ type: 'board', index: 4 }));
  }

  // ---- Picker ---------------------------------------------------------------
  var picker = document.getElementById('picker');
  var suitRow = document.getElementById('suitRow');
  var rankGrid = document.getElementById('rankGrid');
  var removeBtn = document.getElementById('removeCard');
  var pickerTitle = document.getElementById('pickerTitle');
  var pickerTarget = null;
  var pickerSuit = 0;

  function buildSuitRow() {
    suitRow.innerHTML = '';
    SUIT_SYM.forEach(function (sym, suit) {
      var b = document.createElement('button');
      b.className = 'suit-btn ' + (SUIT_RED[suit] ? 'red' : 'black');
      b.textContent = sym;
      b.addEventListener('click', function () { pickerSuit = suit; refreshPicker(); });
      suitRow.appendChild(b);
    });
  }

  function refreshPicker() {
    // Highlight active suit
    Array.prototype.forEach.call(suitRow.children, function (b, i) {
      b.classList.toggle('active', i === pickerSuit);
    });
    // Rank grid for chosen suit
    var used = usedCards(pickerTarget);
    var current = getSlot(pickerTarget);
    rankGrid.innerHTML = '';
    RANK_ORDER.forEach(function (rank) {
      var card = rank * 4 + pickerSuit;
      var b = document.createElement('button');
      b.className = 'rank-btn';
      b.textContent = RANK_LBL[rank];
      if (used[card]) b.classList.add('used');
      if (card === current) b.style.outline = '2px solid var(--gold)';
      b.addEventListener('click', function () {
        setSlot(pickerTarget, card);
        closePicker();
        onChange();
      });
      rankGrid.appendChild(b);
    });
  }

  function openPicker(target) {
    pickerTarget = target;
    var existing = getSlot(target);
    pickerSuit = existing != null ? (existing & 3) : 0;
    var name = target.type === 'hole' ? 'hand card' :
      (target.index < 3 ? 'flop card' : target.index === 3 ? 'turn card' : 'river card');
    pickerTitle.textContent = 'Select ' + name;
    removeBtn.classList.toggle('hidden', existing == null);
    buildSuitRow();
    refreshPicker();
    picker.classList.remove('hidden');
  }

  function closePicker() {
    picker.classList.add('hidden');
    pickerTarget = null;
  }

  document.getElementById('pickerClose').addEventListener('click', closePicker);
  picker.addEventListener('click', function (e) { if (e.target === picker) closePicker(); });
  removeBtn.addEventListener('click', function () {
    if (pickerTarget) { setSlot(pickerTarget, null); }
    closePicker();
    onChange();
  });

  // ---- Controls -------------------------------------------------------------
  document.querySelectorAll('#gameSeg .seg').forEach(function (b) {
    b.addEventListener('click', function () {
      var game = b.dataset.game;
      if (game === state.game) return;
      state.game = game;
      var n = HOLE_COUNT[game];
      state.hole = state.hole.slice(0, n);
      while (state.hole.length < n) state.hole.push(null);
      onChange();
    });
  });

  document.getElementById('oppPlus').addEventListener('click', function () {
    if (state.opponents < 9) { state.opponents++; onChange(); }
  });
  document.getElementById('oppMinus').addEventListener('click', function () {
    if (state.opponents > 1) { state.opponents--; onChange(); }
  });
  document.getElementById('clearBtn').addEventListener('click', function () {
    for (var i = 0; i < state.hole.length; i++) state.hole[i] = null;
    for (var j = 0; j < state.board.length; j++) state.board[j] = null;
    onChange();
  });

  // ---- Compute (worker) -----------------------------------------------------
  var worker = null;
  var reqId = 0;
  var debounceTimer = null;

  function initWorker() {
    try {
      worker = new Worker('worker.js');
      worker.onmessage = function (e) {
        var d = e.data;
        if (d.id !== reqId) return; // stale
        if (d.ok) showResult(d.res);
      };
    } catch (e) { worker = null; }
  }

  var equityVal = document.getElementById('equityVal');
  var equityLabel = document.getElementById('equityLabel');
  var winVal = document.getElementById('winVal');
  var tieVal = document.getElementById('tieVal');
  var loseVal = document.getElementById('loseVal');

  function fmt(x) { return (Math.round(x * 10) / 10).toFixed(1); }

  function showResult(res) {
    equityVal.textContent = fmt(res.equity);
    winVal.textContent = fmt(res.win) + '%';
    tieVal.textContent = fmt(res.tie) + '%';
    loseVal.textContent = fmt(res.lose) + '%';
    equityLabel.classList.remove('computing');
    equityLabel.textContent = 'Win probability vs ' + state.opponents +
      ' opponent' + (state.opponents === 1 ? '' : 's');
  }

  function setIdle(msg) {
    equityVal.textContent = '—';
    winVal.textContent = '—'; tieVal.textContent = '—'; loseVal.textContent = '—';
    equityLabel.classList.remove('computing');
    equityLabel.textContent = msg;
  }

  function compute() {
    var hole = state.hole.filter(function (c) { return c != null; });
    if (hole.length < HOLE_COUNT[state.game]) {
      setIdle('Enter all ' + HOLE_COUNT[state.game] + ' of your cards to begin');
      return;
    }
    var board = state.board.filter(function (c) { return c != null; });

    equityLabel.classList.add('computing');
    equityLabel.textContent = 'Calculating…';

    var msg = {
      id: ++reqId,
      hole: hole, board: board, game: state.game,
      opponents: state.opponents, holeCount: HOLE_COUNT[state.game], iters: ITERS
    };

    if (worker) {
      worker.postMessage(msg);
    } else {
      // Fallback: run on main thread.
      setTimeout(function () {
        var res = simulate(hole, board, state.game, state.opponents, HOLE_COUNT[state.game], ITERS);
        showResult(res);
      }, 10);
    }
  }

  function onChange() {
    saveState();
    render();
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(compute, 180);
  }

  // ---- Boot -----------------------------------------------------------------
  loadState();
  initWorker();
  render();
  compute();

  // Service worker registration.
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function () { /* ignore */ });
    });
  }
})();
