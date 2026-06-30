# Poker Odds — mobile PWA

A tap-only, installable mobile web app that estimates your **probability of
winning a poker hand**. Pick your hole cards, choose the game, optionally enter
the flop / turn / river, and it runs a Monte Carlo simulation to show your
equity. No keyboard ever appears — every input is a tap.

## Features

- **Three games**: Texas Hold'em (2 cards), Pineapple (3 cards), Omaha (4 cards).
- **Tap-to-enter card picker** — a bottom sheet with suit + rank buttons. Cards
  already in play are greyed out so you can't pick a duplicate.
- **Community cards** entered street by street: flop, turn, river (all optional —
  works pre-flop too).
- **Opponents** selector (1–9). Equity is computed against that many random hands.
- **Live results**: big win-probability number plus a Win / Split / Lose
  breakdown, recalculated automatically as you tap.
- **Installable & offline**: web manifest + service worker, so you can add it to
  your home screen and use it with no connection.
- The math runs in a **Web Worker**, so the UI never freezes.

## How the probability is calculated

For the cards you've entered, the app runs ~30,000 Monte Carlo trials. Each trial
deals random hole cards to the opponents, completes the board, evaluates every
player's best five-card hand, and tallies the outcome. **Equity** (the headline
number) is your outright-win rate plus your fair share of split pots.

Hand-evaluation rules per game:

- **Hold'em / Pineapple** — best five cards from your hole cards + the board.
  (Pineapple is treated as "play your best": all three hole cards are available.
  This matches common pineapple odds tools; if you play a discard variant the
  real equity at showdown is slightly lower.)
- **Omaha** — exactly two hole cards + exactly three board cards, per Omaha rules.

The engine has a unit-tested 5-card evaluator (`poker.js`); equity for benchmark
spots matches known values (e.g. AA vs. one random hand ≈ 85%).

## Run it locally

It's a static site — no build step.

```bash
cd poker-pwa
python3 -m http.server 8000
# open http://localhost:8000 on your phone or browser
```

A service worker is used, so serve over `http://localhost` or HTTPS (not `file://`).

## Deploy

Any static host works. For **GitHub Pages**, publish the `poker-pwa/` folder (or
copy its contents to the site root) and open `index.html`. On your phone, use
the browser's **Add to Home Screen** to install it as a standalone app.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Markup / layout |
| `styles.css` | Poker-felt mobile theme |
| `app.js` | UI state, card picker, worker orchestration |
| `poker.js` | Hand evaluator + Monte Carlo engine (shared by page & worker) |
| `worker.js` | Runs the simulation off the main thread |
| `manifest.webmanifest`, `sw.js`, `icons/` | PWA install + offline support |

> Odds are estimates for study/entertainment. Not gambling advice.
