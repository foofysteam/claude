# Kingar's Poker Sessions — mobile PWA

An installable mobile web app for poker night. Two tabs:

1. **♠ Odds** — a tap-only win-probability calculator. Pick your hole cards,
   choose the game, optionally enter the flop / turn / river, and it shows your
   live equity. No keyboard ever appears for card entry — every card is a tap.
2. **Players & Buy-ins** — keep score for the table: add players, track their
   buy-ins and cash-outs, see each player's net, and get an automatic settle-up
   (who pays whom) at the end.

Everything is stored locally on the device and works offline once installed.

## Odds tab

- **Three games**: Texas Hold'em (2 cards), Pineapple (3 cards), Omaha (4 cards).
- **Tap-to-enter card picker** — a bottom sheet with suit + rank buttons. Cards
  already in play are greyed out so you can't pick a duplicate.
- **Community cards** entered street by street: flop, turn, river (all optional,
  so it works pre-flop too).
- **Opponents** selector (1–9), with a one-tap "Use table size from session"
  button that reads how many players are in your session.
- **Live results**: a big win-probability number plus a Win / Split / Lose
  breakdown, recalculated automatically as you tap. The math runs in a Web
  Worker so the UI never freezes.

### How the probability is calculated

For the cards you've entered, the app runs ~30,000 Monte Carlo trials. Each trial
deals random hole cards to the opponents, completes the board, evaluates every
player's best five-card hand, and tallies the outcome. **Equity** (the headline
number) is your outright-win rate plus your fair share of split pots.

Hand-evaluation rules per game:

- **Hold'em / Pineapple** — best five cards from your hole cards + the board.
  (Pineapple plays all three hole cards; if you play a discard variant the real
  showdown equity is slightly lower.)
- **Omaha** — exactly two hole cards + exactly three board cards, per Omaha rules.

The 5-card evaluator (`poker.js`) is unit-tested and benchmark equities match
known values (e.g. AA vs. one random hand ≈ 85%, AA vs. two ≈ 73%).

## Players & Buy-ins tab

- Name the session (defaults to "Kingar's Poker Session", dated automatically).
- Set the **buy-in amount** for the night.
- **Add players**, then tap +/− to record each player's buy-ins (rebuys). Each
  player's money-in updates live.
- Enter each player's **cash-out** at the end.
- The summary shows the **total pot**, whether the books balance, each player's
  **net** (green up / red down), and a minimal **settle-up** list of transfers.
- Everything persists in `localStorage` and survives reloads.

## Run it locally

It's a static site — no build step.

```bash
cd poker-pwa
python3 -m http.server 8000
# open http://localhost:8000 on your phone or browser
```

A service worker is used, so serve over `http://localhost` or HTTPS (not `file://`).

## Hosting

The app is just static files, so any static host works. Pick one:

### GitHub Pages (automated, included)

This repo ships a workflow at `.github/workflows/deploy-pages.yml` that publishes
the `poker-pwa/` folder to GitHub Pages.

**One-time setup:** in the repository, go to **Settings → Pages → Build and
deployment** and set **Source = "GitHub Actions"**. After that, every push that
touches the app deploys automatically (or trigger it from the **Actions** tab via
"Run workflow"). The site URL appears in the workflow run and at
`https://<owner>.github.io/<repo>/`.

### Other free options

- **Netlify Drop** — drag the `poker-pwa/` folder onto <https://app.netlify.com/drop>.
- **Cloudflare Pages / Vercel** — point either at this repo and set the output
  directory to `poker-pwa`.

Once it's hosted over HTTPS, open it on your phone and use **Add to Home Screen**
to install it as a standalone app.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Markup / layout (tabbed) |
| `styles.css` | Poker-felt mobile theme |
| `app.js` | Odds tab: state, card picker, worker orchestration |
| `session.js` | Players & Buy-ins tab + tab switching |
| `poker.js` | Hand evaluator + Monte Carlo engine (shared by page & worker) |
| `worker.js` | Runs the simulation off the main thread |
| `manifest.webmanifest`, `sw.js`, `icons/` | PWA install + offline support |

> Odds are estimates for study/entertainment. Not gambling advice.
