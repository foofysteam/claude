/* Web Worker: runs Monte Carlo equity off the main thread. */
importScripts('poker.js');

self.onmessage = function (e) {
  var d = e.data;
  try {
    var res = simulate(d.hole, d.board, d.game, d.opponents, d.holeCount, d.iters);
    self.postMessage({ id: d.id, ok: true, res: res, iters: d.iters });
  } catch (err) {
    self.postMessage({ id: d.id, ok: false, error: String(err && err.message || err) });
  }
};
