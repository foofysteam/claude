/* Session manager: players, buy-ins, cash-outs, settle-up. Plus tab switching. */
(function () {
  'use strict';

  // ---- Tab switching --------------------------------------------------------
  var tabs = document.getElementById('tabs');
  tabs.addEventListener('click', function (e) {
    var btn = e.target.closest('.tab');
    if (!btn) return;
    var name = btn.dataset.tab;
    document.querySelectorAll('#tabs .tab').forEach(function (b) {
      b.classList.toggle('active', b === btn);
    });
    document.getElementById('panel-odds').classList.toggle('active', name === 'odds');
    document.getElementById('panel-session').classList.toggle('active', name === 'session');
    document.body.className = 'tab-' + name;
  });

  // ---- State ----------------------------------------------------------------
  var nextId = 1;
  var CURRENCY = '₹';
  var session = {
    name: "Kingar's Poker Session",
    date: '',
    buyIn: 500,
    currency: CURRENCY,
    players: [] // { id, name, buyIns, cashOut }
  };

  function todayStr() {
    var d = new Date();
    return d.toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' });
  }

  function load() {
    try {
      var s = JSON.parse(localStorage.getItem('kingarSession'));
      if (s && Array.isArray(s.players)) {
        session.name = s.name || session.name;
        session.date = s.date || todayStr();
        session.buyIn = s.buyIn > 0 ? s.buyIn : 500;
        session.currency = CURRENCY; // always rupees
        session.players = s.players.map(function (p) {
          return { id: p.id, name: p.name, buyIns: p.buyIns | 0, cashOut: (p.cashOut == null ? null : +p.cashOut) };
        });
        session.players.forEach(function (p) { if (p.id >= nextId) nextId = p.id + 1; });
      }
    } catch (e) { /* ignore */ }
    if (!session.date) session.date = todayStr();
  }
  function save() {
    try { localStorage.setItem('kingarSession', JSON.stringify(session)); } catch (e) { /* ignore */ }
    // Let the odds tab know the table size.
    if (window.KingarOdds && window.KingarOdds.onSessionUpdate) {
      window.KingarOdds.onSessionUpdate(session.players.length);
    }
  }

  // ---- Money helpers --------------------------------------------------------
  function money(n) {
    var v = Math.round(n * 100) / 100;
    var s = Number.isInteger(v) ? String(v) : v.toFixed(2);
    return session.currency + s;
  }
  function totalIn(p) { return p.buyIns * session.buyIn; }
  function net(p) { return (p.cashOut == null ? 0 : p.cashOut) - totalIn(p); }

  // ---- Settlement (greedy minimal transfers) --------------------------------
  function settle() {
    var nets = session.players
      .filter(function (p) { return p.cashOut != null; })
      .map(function (p) { return { name: p.name, net: net(p) }; });
    var creditors = nets.filter(function (n) { return n.net > 0.005; })
      .map(function (n) { return { name: n.name, amt: n.net }; })
      .sort(function (a, b) { return b.amt - a.amt; });
    var debtors = nets.filter(function (n) { return n.net < -0.005; })
      .map(function (n) { return { name: n.name, amt: -n.net }; })
      .sort(function (a, b) { return b.amt - a.amt; });
    var res = [], i = 0, j = 0;
    while (i < debtors.length && j < creditors.length) {
      var pay = Math.min(debtors[i].amt, creditors[j].amt);
      res.push({ from: debtors[i].name, to: creditors[j].name, amt: pay });
      debtors[i].amt -= pay; creditors[j].amt -= pay;
      if (debtors[i].amt < 0.005) i++;
      if (creditors[j].amt < 0.005) j++;
    }
    return res;
  }

  // ---- DOM refs -------------------------------------------------------------
  var sessName = document.getElementById('sessName');
  var sessDate = document.getElementById('sessDate');
  var buyinVal = document.getElementById('buyinVal');
  var playersList = document.getElementById('playersList');
  var newPlayerName = document.getElementById('newPlayerName');
  var summary = document.getElementById('sessionSummary');

  // ---- Render ---------------------------------------------------------------
  function renderPlayers() {
    playersList.innerHTML = '';
    if (!session.players.length) {
      var empty = document.createElement('div');
      empty.className = 'empty-hint';
      empty.textContent = 'No players yet — add everyone at the table below.';
      playersList.appendChild(empty);
      return;
    }
    session.players.forEach(function (p) {
      var card = document.createElement('div');
      card.className = 'player-card';

      // Header: name + net badge
      var head = document.createElement('div');
      head.className = 'player-head';
      var nm = document.createElement('div');
      nm.className = 'player-name';
      nm.textContent = p.name;
      var badge = document.createElement('div');
      var nv = net(p);
      badge.className = 'net-badge ' + (p.cashOut == null ? 'pending' : nv > 0 ? 'up' : nv < 0 ? 'down' : 'even');
      badge.textContent = p.cashOut == null ? 'in play' : (nv >= 0 ? '+' : '') + money(nv).replace(session.currency, session.currency);
      head.appendChild(nm); head.appendChild(badge);

      // Buy-ins row
      var biRow = document.createElement('div');
      biRow.className = 'player-row';
      var biLabel = document.createElement('div');
      biLabel.className = 'pr-label';
      biLabel.innerHTML = 'Buy-ins<small>' + money(totalIn(p)) + ' in</small>';
      var biCtrl = document.createElement('div');
      biCtrl.className = 'mini-stepper';
      var minus = document.createElement('button'); minus.className = 'mini-btn'; minus.textContent = '−';
      var cnt = document.createElement('span'); cnt.className = 'mini-val'; cnt.textContent = p.buyIns;
      var plus = document.createElement('button'); plus.className = 'mini-btn'; plus.textContent = '+';
      minus.addEventListener('click', function () { if (p.buyIns > 0) { p.buyIns--; save(); renderPlayers(); renderSummary(); } });
      plus.addEventListener('click', function () { p.buyIns++; save(); renderPlayers(); renderSummary(); });
      biCtrl.appendChild(minus); biCtrl.appendChild(cnt); biCtrl.appendChild(plus);
      biRow.appendChild(biLabel); biRow.appendChild(biCtrl);

      // Cash-out row
      var coRow = document.createElement('div');
      coRow.className = 'player-row';
      var coLabel = document.createElement('div');
      coLabel.className = 'pr-label';
      coLabel.textContent = 'Cash out';
      var coWrap = document.createElement('div');
      coWrap.className = 'cash-wrap';
      var cur = document.createElement('span'); cur.className = 'cash-cur'; cur.textContent = session.currency;
      var co = document.createElement('input');
      co.type = 'text'; co.inputMode = 'decimal'; co.className = 'cash-input';
      co.placeholder = '—';
      co.value = p.cashOut == null ? '' : String(p.cashOut);
      co.addEventListener('input', function () {
        var v = co.value.replace(/[^0-9.]/g, '');
        p.cashOut = v === '' ? null : parseFloat(v);
        if (isNaN(p.cashOut)) p.cashOut = null;
        save(); renderSummary();
        // update just this badge without losing focus
        var newNet = net(p);
        badge.className = 'net-badge ' + (p.cashOut == null ? 'pending' : newNet > 0 ? 'up' : newNet < 0 ? 'down' : 'even');
        badge.textContent = p.cashOut == null ? 'in play' : (newNet >= 0 ? '+' : '') + money(newNet);
      });
      coWrap.appendChild(cur); coWrap.appendChild(co);
      coRow.appendChild(coLabel); coRow.appendChild(coWrap);

      // Remove
      var rm = document.createElement('button');
      rm.className = 'remove-player';
      rm.textContent = 'Remove player';
      rm.addEventListener('click', function () {
        session.players = session.players.filter(function (x) { return x.id !== p.id; });
        save(); renderPlayers(); renderSummary();
      });

      card.appendChild(head);
      card.appendChild(biRow);
      card.appendChild(coRow);
      card.appendChild(rm);
      playersList.appendChild(card);
    });
  }

  function renderSummary() {
    var totalPot = session.players.reduce(function (a, p) { return a + totalIn(p); }, 0);
    var cashedPlayers = session.players.filter(function (p) { return p.cashOut != null; });
    var totalCashed = cashedPlayers.reduce(function (a, p) { return a + p.cashOut; }, 0);

    var html = '';
    html += '<div class="sum-row"><span>Total in pot</span><strong>' + money(totalPot) + '</strong></div>';
    html += '<div class="sum-row"><span>Players</span><strong>' + session.players.length + '</strong></div>';

    if (cashedPlayers.length) {
      var diff = totalCashed - session.players.reduce(function (a, p) {
        return a + (p.cashOut != null ? totalIn(p) : 0);
      }, 0);
      html += '<div class="sum-row"><span>Cashed out (' + cashedPlayers.length + ')</span><strong>' + money(totalCashed) + '</strong></div>';
      if (Math.abs(diff) > 0.005) {
        html += '<div class="balance ' + (diff > 0 ? 'warn' : 'warn') + '">' +
          (diff > 0 ? 'Cash-outs exceed buy-ins by ' + money(diff) : 'Cash-outs short of buy-ins by ' + money(-diff)) +
          ' — check the numbers.</div>';
      } else {
        html += '<div class="balance ok">Books balance ✓</div>';
      }

      var transfers = settle();
      if (transfers.length) {
        html += '<div class="settle-title">Settle up</div>';
        transfers.forEach(function (t) {
          html += '<div class="settle-row"><span class="s-from">' + esc(t.from) + '</span>' +
            '<span class="s-arrow">→</span><span class="s-to">' + esc(t.to) + '</span>' +
            '<span class="s-amt">' + money(t.amt) + '</span></div>';
        });
      }
    } else {
      html += '<div class="sum-hint">Enter each player\'s cash-out at the end to see who pays whom.</div>';
    }
    summary.innerHTML = html;
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function renderHeader() {
    sessName.value = session.name;
    sessDate.textContent = session.date;
    buyinVal.textContent = session.currency + session.buyIn;
  }

  function renderAll() { renderHeader(); renderPlayers(); renderSummary(); }

  // ---- Events ---------------------------------------------------------------
  sessName.addEventListener('input', function () { session.name = sessName.value; save(); });

  document.getElementById('buyinPlus').addEventListener('click', function () {
    session.buyIn += 100; save(); renderAll();
  });
  document.getElementById('buyinMinus').addEventListener('click', function () {
    if (session.buyIn > 100) { session.buyIn -= 100; save(); renderAll(); }
  });

  function addPlayer() {
    var name = newPlayerName.value.trim();
    if (!name) return;
    session.players.push({ id: nextId++, name: name, buyIns: 1, cashOut: null });
    newPlayerName.value = '';
    save(); renderPlayers(); renderSummary();
  }
  document.getElementById('addPlayerBtn').addEventListener('click', addPlayer);
  newPlayerName.addEventListener('keydown', function (e) { if (e.key === 'Enter') addPlayer(); });

  document.getElementById('resetSession').addEventListener('click', function () {
    if (!confirm('Reset the session? This clears all players and buy-ins.')) return;
    session.players = [];
    session.name = "Kingar's Poker Session";
    session.date = todayStr();
    save(); renderAll();
  });

  // ---- Boot -----------------------------------------------------------------
  load();
  renderAll();
  save(); // pushes initial table size to the odds tab
})();
