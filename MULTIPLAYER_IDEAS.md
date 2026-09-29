# Multiplayer Ideas: Hold the Coin

The core hook: a coin whose price swings like a stock. You win by holding it
at the right time and not getting wrecked while you do. At the end of each
season, the players with the highest net worth win real tech prizes.

This version is based on research into what has actually worked and failed
in the past (see the bottom of this file).

---

## What the research says

### What worked

| Game / product | Result | Why it worked |
|---|---|---|
| **ARC Raiders** (extraction, Oct 2025) | 16M+ copies sold, 482K Steam peak | Extraction games are the hottest multiplayer genre right now. Risk what you carry, then get out alive. |
| **Hunt: Showdown** | Long-running extraction hit | Whoever carries the bounty **gets revealed on the map**, so the hunter becomes the hunted. Proven tension mechanic. |
| **Counter-Strike skins** | ~$6–7B item market, $1B+/yr from cases | The market sits on top of a game people already love. It even survived a $2B crash in 30 hours (Oct 2025). |
| **Roblox DevEx** | $1.5B paid to creators in 2025 | Real money out, earned by *building*, not by speculating on a token. |
| **Agar.io / Slither.io** | Agar.io was 2015's most popular game | Browser, no signup, one click to play. Simple to learn, hard to master. Spread through YouTube. |
| **Among Us** | 447K Steam peak, ~500M monthly players | Social deduction plus streamers. Every match makes a funny clip. |
| **Manifold Markets** | Active community trading *play money* | People trade hard for bragging rights even with fake money. |
| **Notcoin** | Token hit a $1.1B market cap | Zero friction (inside Telegram) and viral invite loops. One of the few token launches that worked. |

### What failed

| Game / product | Result | Why it failed |
|---|---|---|
| **Axie Infinity** | 2.7M → 250K daily players; token −99% | Unlimited token supply. Players farmed and sold, and the economy needed a constant flow of new money. |
| **Hamster Kombat** | 300M → 41M users in a month; token −76% | Boring gameplay, and the token payouts were worth less than $10 after months of play. |
| **Friend.tech** (people as stocks) | Volume −95% in weeks; 15 daily users by mid-2024 | Nothing to do once the trading stopped paying. Shut down while the creators kept $44M. |
| **Web3 games overall** | 90%+ are dead; average lifespan ~4 months | $12–15B spent chasing tokens. Gamers never showed up. |
| **Diablo 3 real-money auction house** | Removed in 2014 | Buying gear beat playing for it, which "short-circuited the core reward loop". |
| **HQ Trivia** | 2.38M live players, then shut down in 2020 | The prize pot was split among too many winners, so each payout was tiny. The format got repetitive and the money ran out. |
| **Pump.fun memecoins** | 60% of users lost money; 311 wallets made $1M+ | Early insiders win and late retail loses. |

### Lessons for our game

1. **Make it fun with fake money first.** Every real-value success (CS skins,
   Roblox) was a great game first. Every failure made the token the point.
2. **Volatility works as a game mechanic.** Price swings are exciting when
   they happen inside a game (Tarkov's flea market, EVE, CS crashes).
3. **Carrying value and being revealed is proven tension** (Hunt: Showdown).
4. **Zero friction:** browser, no download, click to play (.io games).
5. **Prizes: fewer, bigger, funded.** HQ Trivia died splitting pots too thin.
   Use sponsors and give a clear top-N.
6. **Money must never buy winning** (Diablo 3).
7. **Don't make players into stocks.** Friend.tech showed it dies fast.

---

## Ideas (renamed)

### 1. Bank Run (recommended)
The name describes the mechanic. If everyone runs to cash out at once, the
price crashes for everybody.

**Genre:** Top-down 2D extraction game in the browser, 20–40 players, about
10-minute rounds.

**Loop:**
1. Drop in with nothing and collect coin from mining rigs, crates and players
   you knock out.
2. **One shared live price chart** sits on everyone's screen.
3. Coin you're carrying isn't safe. Get knocked out and you drop your bag.
4. Reach an extraction terminal to sell at the current price. What you sell
   becomes banked, permanent season net worth.

**What moves the price:**
- **Sell pressure:** mass cash-outs crash the price (the bank run).
- **Market events:** a sudden spike or a flash crash, announced to everyone.
- **Upward drift** over the match, so holding pays, if you survive.

**Why you have to hold:**
- The longer you carry without selling, the bigger your payout multiplier.
- Players carrying big bags get **revealed on the map**, the Hunt: Showdown
  bounty mechanic.

**Rewards:** Season net-worth leaderboard. The top players win tech.

### 2. Inside Job (easiest to build)
**Genre:** Social deduction for 6–10 players, like Among Us.

Everyone buys into a shared coin and the price climbs each round. One or two
players are secret **insiders** who win by dumping at the peak without getting
caught. Everyone else reads the chart, argues and votes someone out. Built for
streamer clips, which is what made Among Us blow up.

### 3. Rigged
**Genre:** Team territory control.

Teams capture GPU mining rigs, and each rig generates coin. The more coin that
gets mined in total, the lower the price goes. **Halving events** cut mining
output in half and make the price spike. Teams decide whether to upgrade rigs,
sell, or hold through the halving.

*(The old "every player is a coin" idea was cut. Friend.tech showed it
doesn't last.)*

> Names are working titles. A quick Steam search found no game called
> "Bank Run", but do a trademark check before launch.

---

## Real Crypto / NFTs (not legal advice)

- **Start with an in-game coin.** Add crypto later only if the game is proven
  fun without it.
- If people buy a token hoping it rises because of your work, US regulators
  may treat it as a **security**.
- Real money plus luck can count as **gambling**.
- **Steam bans** games that use crypto or NFTs (still in effect). Epic
  allows them.
- If you want NFTs later, make them **cosmetic only**, and ideally tied to
  something players already care about. That approach is why Sorare works:
  its cards are licensed real football players.

---

## Brief to Give Grok / ChatGPT

```
Write a complete, buildable game design document for a multiplayer browser game called "Bank Run".

CONCEPT: Top-down 2D extraction game. 20-40 players per match, ~10 minute rounds. Players collect an in-game coin whose price swings like a stock on ONE shared live chart everyone sees. Carried coin is dropped if you get knocked out. You must reach an extraction terminal to sell at the current price; sold coin becomes banked season net worth. The name is the core mechanic: if many players cash out at once, sell pressure crashes the price for everyone. Core tension: sell early (safe, small) vs. hold (bigger payout, risk of a crash or getting hunted).

REFERENCES: ARC Raiders and Escape from Tarkov (extraction risk), Hunt: Showdown (bounty carriers are revealed on the map), agar.io (instant browser play, no signup, simple to learn but deep), Among Us (moments that make good streamer clips).

REQUIRED MECHANICS:
- Price model: sell pressure from cash-outs lowers price; random market events (sudden spike, flash crash) announced to all players; upward drift over the match. Give an exact formula and tick rate.
- Hold multiplier: bonus for carrying longer without selling. Exact numbers.
- Reveal: players carrying big bags are revealed on the minimap. Exact thresholds.
- Coin sources: mining rigs, loot crates, knocked-out players. Spawn rates and amounts.
- Combat: simple (e.g., shoot + dash), easy to learn. Health, damage, cooldowns.
- Extraction terminals: count, placement, and whether they open/close during the match.
- Season: net-worth leaderboard; the top players win real tech prizes (skill-based, no purchase required). Prizes are few and large, not split thin.
- In-game coin only. NO real-money purchases, crypto, or NFTs in version 1. Nothing money can buy may affect winning.

DELIVER:
1. One-paragraph pitch
2. Match flow minute by minute
3. Controls (keyboard/mouse + mobile touch)
4. Map layout (size, zones, terminal and rig placement)
5. Full economy with exact numbers and the price formula
6. Combat stats table
7. UI screens and what each shows (lobby, HUD, price chart, results, leaderboard)
8. Art style direction (simple 2D, readable at small size)
9. Anti-cheat (server-authoritative)
10. MVP scope: the smallest version that is fun, to build first

Be specific. Use concrete numbers everywhere so a developer can implement it directly.
```

## Suggested Tech Stack
- **Client:** Phaser 3 + TypeScript (2D, browser, desktop and mobile)
- **Server:** Node.js + Colyseus (multiplayer rooms, server-authoritative)
- **Database:** Postgres (accounts, season leaderboard)

---

## Sources
- Axie Infinity: [Reason](https://reason.com/2022/02/01/the-biggest-nft-video-games-economy-is-collapsing-because-nft-games-dont-work/), [Axios](https://www.axios.com/2022/04/12/fall-of-play-to-earn-gaming-p2e-axie-infinity-slp)
- Hamster Kombat: [Cryptopolitan](https://www.cryptopolitan.com/hamster-kombat-loses-260-million-players/), [MoneyCheck](https://moneycheck.com/hamster-kombat-token-drops-43-on-launch-day-hmstr-marred-by-price-plunge-and-user-discontent/)
- Friend.tech: [CoinDesk](https://www.coindesk.com/tech/2023/08/31/scores-of-friendtech-users-remain-active-even-as-trading-volumes-drop-95), [DL News](https://www.dlnews.com/articles/defi/friend-tech-shuts-down-after-revenue-and-users-plummet/)
- Web3 games 90%+ dead: [CoinDesk / Caladan](https://www.coindesk.com/markets/2026/04/23/more-than-90-of-web3-games-failed-after-usd15-billion-boom-as-gamers-never-showed-up-caladan)
- ARC Raiders: [SteamDB](https://steamdb.info/app/1808500/charts/), [Beebom](https://beebom.com/arc-raiders-player-count/)
- Hunt: Showdown bounty: [Hunt Wiki](https://huntshowdown.wiki.gg/wiki/Game_Modes/Bounty_Hunt)
- CS skins: [Esports News UK](https://esports-news.co.uk/2025/10/08/counter-strike-skins-market-soars-to-new-peak-of-5-78-billion/), [VGTimes](https://vgtimes.com/articles/164703-cs2-skins-economy-billions.html)
- Roblox payouts: [RoLearn](https://rolearn.dev/trend-reports/creator-economy-2025-report/)
- .io games: [Slither.io – Wikipedia](https://en.wikipedia.org/wiki/Slither.io), [Bonk.io history](https://bonk-io.com/blog/history-of-io-games/)
- Among Us: [SteamDB](https://steamdb.info/app/945360/graphs/)
- Diablo 3 auction house: [Forbes](https://www.forbes.com/sites/paultassi/2023/04/16/remembering-diablos-biggest-mistake-the-auction-house/)
- HQ Trivia: [Wikipedia](https://en.wikipedia.org/wiki/HQ_(video_game)), [CBS News](https://www.cbsnews.com/news/hq-trivia-app-shuts-down-runs-out-of-money/)
- Pump.fun: [Crypto Times](https://www.cryptotimes.io/2025/06/06/over-300k-pump-fun-users-lose-money-on-memecoins/)
- Notcoin: [Decrypt](https://decrypt.co/resources/what-is-notcoin-telegram-based-game-airdrop)
- Manifold: [Manifold About](https://manifold.markets/about)
- Steam crypto/NFT ban: [PC Gamer](https://www.pcgamer.com/steam-bans-nfts-cryptocurrencies-blockchain/)
- Sorare: [TechCrunch](https://techcrunch.com/2023/01/30/sorare-teams-up-with-the-premier-league-for-its-nft-fantasy-football-game/)
