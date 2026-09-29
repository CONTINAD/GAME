# Multiplayer Ideas: Hold the Coin

Every idea here uses the same core hook. There is a coin, and its price swings
up and down like a stock. You win by holding it at the right time and not
getting wrecked while you do. At the end of each season, the players with the
highest net worth win real tech prizes.

---

## 1. Diamond Hands (recommended)
**Genre:** Top-down 2D extraction battle game in the browser, 20–40 players
per match, about 10-minute rounds.

**Loop:**
1. Drop into the map with nothing.
2. Collect coin from mining rigs, loot crates and players you knock out.
3. Everyone watches **one shared live price chart** at the top of the screen.
4. Coin you're carrying isn't safe. If you get knocked out, you drop your bag
   and anyone can grab it.
5. Run to an **extraction terminal** to sell at the current price. What you
   sell becomes banked money that counts toward your season net worth.

**What moves the price:**
- **Sell pressure:** when lots of players sell at once, the price drops. If
  everyone panics and sells, it crashes for everyone.
- **Market events:** random pop-ups like "🐋 Whale Alert +40%" or
  "📉 Flash Crash −60%".
- **Upward drift:** the price tends to rise the longer the match goes, so
  holding pays off, if you survive.

**Why you "gotta hold":**
- **Diamond Hands multiplier:** the longer you carry without selling, the
  bigger your bonus when you finally sell.
- **Bag holder glow:** players carrying huge bags show up on the minimap, so
  everyone comes hunting them.
- The result is a constant sell-now-or-hold choice. Selling early is safe but
  small. Holding pays big, but you can crash or get hunted.

**Rewards:** Season net-worth leaderboard. Top players win tech (earbuds,
keyboards, GPUs, consoles). Cosmetic badges for everyone else.

---

## 2. Rug Pull (easiest to build)
**Genre:** Social deduction party game (like Among Us), 6–10 players.

Everyone puts money into a shared coin and the price climbs each round. One
or two players are secretly **Rug Pullers**. They win if they dump their coin
at the peak without getting caught. Everyone else talks, reads the chart and
votes to kick out the suspect. Kick the right person and the price pumps.
Kick the wrong one and the price tanks.

- **Build effort:** Low. Small lobbies, simple visuals, mostly UI.

---

## 3. Miner Wars
**Genre:** Team territory control.

Teams capture **GPU mining rigs** across the map, and each rig generates coin.
The more coin that gets mined in total, the lower the price goes (supply and
demand). There are **halving events**, where mining output gets cut in half.
Teams choose between upgrading their rigs, selling coin, or holding it through
a halving to cash in on the spike.

- **Build effort:** Medium.

---

## 4. Pump or Dump
**Genre:** Arena brawler.

**Every player is their own coin.** Your price goes up when you win fights and
drops when you lose. Other players can buy into your coin with in-game money,
so they're rooting for you. Betray the people holding your coin and your price
crashes.

- **Build effort:** Medium.

---

## Real Crypto / NFTs: Read Before Deciding (not legal advice)

The recommendation is to **start with an in-game coin** (fake money, but the
chart and the drama are real). Add real crypto or NFTs later only if the game
proves fun without them.

- **Securities risk:** if people buy your token hoping it goes up because of
  your work, US regulators (the SEC) may treat it as a security.
- **Gambling risk:** if the coin is bought with real money, can be cashed out,
  and luck is involved, it can count as gambling.
- **Play-to-earn collapse:** games like Axie Infinity crashed once new players
  stopped buying in. The token only held value while new money kept flowing.
- **Steam bans** games that use crypto or NFTs, which cuts off the biggest PC
  store. (Epic allows them.)
- **Many gamers dislike NFTs**, and announcing them can hurt your launch.
- **A safer NFT option later:** cosmetic-only skins or trophies that don't
  affect gameplay.

**Why the in-game coin is the safer default:** there's no purchase, winning
takes skill, and prizes come from the leaderboard. That keeps the whole
"hold the coin" experience with none of the legal risk.

---

## Brief to Give Grok / ChatGPT

Paste this into Grok or ChatGPT to get a design doc back. Then bring the doc
here to build.

```
Write a complete, buildable game design document for a multiplayer browser game called "Diamond Hands".

CONCEPT: Top-down 2D extraction battle game. 20-40 players per match, ~10 minute rounds. Players collect an in-game coin whose price swings like a stock on ONE shared live chart everyone sees. Carried coin is dropped if you get knocked out. You must reach an extraction terminal to sell coin at the current price; sold coin becomes banked net worth for the season. Core tension: sell early (safe, small) vs. hold (bigger payout, risk of crash or getting hunted).

REQUIRED MECHANICS:
- Price model: sell pressure from players cashing out lowers price; random market events (whale pump, flash crash); upward drift over the match. Give an exact formula and tick rate.
- "Diamond Hands" multiplier: bonus for holding longer without selling. Give exact numbers.
- "Bag holder glow": players carrying big bags are revealed on the minimap. Give thresholds.
- Coin sources: mining rigs, loot crates, knocked-out players. Give spawn rates and amounts.
- Combat: simple (e.g., shoot + dash), easy to learn. Give health, damage, cooldowns.
- Extraction terminals: count, locations, and whether they open/close during the match.
- Season: net-worth leaderboard; top players win real tech prizes (skill-based, no purchase required).
- In-game coin only. NO real-money purchases, crypto, or NFTs in version 1.

DELIVER:
1. One-paragraph pitch
2. Match flow minute by minute
3. Controls (keyboard/mouse + mobile touch)
4. Map layout description (size, zones, terminal and rig placement)
5. Full economy with exact numbers and the price formula
6. Combat stats table
7. UI screens list and what each shows (lobby, HUD, price chart, results, leaderboard)
8. Art style direction (simple 2D, readable at small size)
9. Anti-cheat considerations (server-authoritative)
10. An MVP scope: the smallest version that is fun, to build first

Be specific. Use concrete numbers everywhere so a developer can implement it directly.
```

## Suggested Tech Stack (for when we build)
- **Client:** Phaser 3 (2D browser game engine) + TypeScript
- **Server:** Node.js + Colyseus (multiplayer rooms, server-authoritative
  state)
- **Database:** Postgres for accounts, the season leaderboard and banked net
  worth
- **Hosting:** any Node host. Runs on desktop and mobile browsers with no
  install.
