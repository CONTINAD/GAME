# Bank Run: Old West Concept

**Pitch:** An Old West sandbox you play in the browser, a bit like GTA. Every
town has a bank, and every bank is a stock. Defend a town's bank and you earn
shares in it. Raid a bank and you crash its stock, and every depositor feels
it. You can be a lawman, an outlaw, or anything in between, and you can
switch whenever you want. Servers hold 10 to 200 players.

The name still fits. Bank runs were real in the Old West (the panics of 1873
and 1893), and in this game, if everyone pulls their money out at once, the
bank collapses.

---

## The World
- **A frontier territory** made of towns linked by dirt roads and one rail
  line, with canyons, rivers and gold mines in between.
- **The number of towns scales with players.** A server with 10 players has 3
  towns. Add about one town per 20 extra players, up to 12 towns at 200.
- **Every town has:** a bank, a sheriff's office, a saloon, a telegraph office
  (the stock exchange), a general store, stables, a train station, and a
  church bell that rings the alarm.
- **Outlaw hideouts** are hidden in the canyons. They're where stolen gold
  gets fenced.

## The Money
| Thing | How it works |
|---|---|
| **Gold price** | One global price shared by every server, shown as a live telegraph ticker. It sets what mined and stolen gold is worth. |
| **Bank stock** | Each town's bank is its own stock. You buy and sell shares at the telegraph office. |
| **What raises a bank's stock** | New deposits, mining in the area, successful defenses, and the gold train arriving safely. |
| **What crashes it** | A robbery (the drop matches the share of the vault that was stolen), or a **bank run**: if withdrawals pass a set limit within a short window, panic sets in and the price crashes. The bank can even fail for the rest of the day. |
| **Dividends** | At the **closing bell** (the end of each short "trading day"), banks that weren't robbed pay dividends to their shareholders. |
| **Deposits** | Bank your gold to keep it safe when you die. But if that bank gets robbed, every depositor loses a cut, so you have a reason to defend the bank that holds your money. |
| **Carried gold** | Not safe. Die and you drop it. |

## How Stocks Work (OTC to Exchange)
This is based on how real stocks work. **OTC** ("over-the-counter") stocks
trade directly between buyers and sellers instead of on a big exchange. They're
usually small companies' penny stocks: cheap, wild price swings, easy to pump.
When a company grows enough, it **uplists** to a major exchange. The game
copies that path.

1. **Founding:** when a camp grows into a settlement, its bank opens with a
   fixed number of shares (for example 10,000).
2. **OTC stage:** the bank starts as an **OTC penny stock**, traded at the
   town's telegraph office. It's cheap, thinly traded, and swings wildly. This
   is where people get rich or wiped out.
3. **How shares get handed out:**
   - Buy them at the telegraph office.
   - Lawmen earn them as a **defense bonus**.
   - The biggest depositors get an allocation at **listing day**.
   - When the bank expands, it **issues new shares**, which lowers the price a
     little for everyone (dilution, just like real stocks).
4. **Uplisting:** when a bank passes a deposit threshold and survives a set
   number of trading days without a successful raid, it **lists on the
   Territory Exchange**. There's a listing-day event (a bell and fireworks),
   the price becomes steadier, and dividends get bigger.
5. **Delisting:** if raids drain the vault below a set level, the bank drops
   back to OTC and the chaos starts again.

Emergent plays this allows:
- A gang raids Town A, buys its crashed stock cheap, then defends the town
  until the price recovers.
- A sheriff invests heavily in the bank they protect.

## Paths (switch any time, GTA-style)

### Lawman
- Take a deputy badge at any sheriff's office.
- Get paid for defending banks, escorting the gold train, and bringing in
  outlaws. Bringing someone in alive with the lasso pays more than killing
  them.
- A defended bank awards **bonus shares** to the lawmen who defended it.
- Commit a crime and you lose your badge for the rest of that trading day.

### Outlaw
- Raid banks, rob stagecoaches, and hit the gold train.
- Stolen gold is **hot**. You can't deposit it until you fence it at a hideout,
  and the fence takes about a 20% cut.
- Form a gang of up to 6 players.

### Everyone else
- **Prospector:** stake a claim and mine gold, which is worth whatever the
  gold price is.
- **Trader:** buy dips and sell peaks at the telegraph office.
- **Bounty hunter:** no badge needed. Just collect the bounties on the
  bounty board.

## Wanted System
- Crimes add **wanted stars (1–5)** and raise the **bounty** on your head.
- At **3 stars or more**, you show up on everyone's map, the same way Hunt:
  Showdown reveals bounty carriers.
- You can clear your stars by laying low, paying off the fence at a hideout,
  or dying. If you die, whoever killed you collects the bounty.

## How a Bank Raid Works
1. **Scout** the town: how many lawmen are there, and where are the guards?
2. **Break in** one of two ways:
   - **Dynamite the vault.** Fast, but loud enough that the whole map hears it.
   - **Crack the safe.** Quiet, but slow, and you can be interrupted.
3. **Alarm:** the church bell rings, lawmen get a notification, and the
   raiders are revealed.
4. **Grab the gold.** Bags are heavy and slow you down. A horse's saddlebags
   carry more, and a wagon carries the most but moves the slowest.
5. **Escape to a hideout** and fence the gold.
6. The town's stock drops, depositors take a loss, and the telegraph ticker
   announces the robbery.

## Defending a Town
- Lawmen respond to the alarm.
- Towns can spend bank funds to **hire NPC deputies**.
- Players can build **barricades** and put a **Gatling gun on the bank roof**.

## Other Activities
- **Gold train:** runs between towns on a schedule. Escort it or rob it.
- **Stagecoaches:** carry deposits between towns.
- **High noon duels:** challenge anyone to an opt-in 1v1 on main street. Great
  clip material.
- **Horse racing** between towns.

## Dying
- You drop your carried gold and hot loot. Your bank deposits and stock
  holdings are safe, but their value can still crash.
- You respawn at the last town you visited (lawmen) or at your hideout
  (outlaws).
- **Boot Hill:** every town has a graveyard, and each death leaves a
  tombstone showing how much gold that player died carrying.

## Scaling From 10 to 200 Players
- Drop-in servers. There's no lobby wait.
- The number of towns and the map size scale with the player count.
- **NPC outlaw gangs** raid banks when few players are online, so the market
  keeps moving even with only 10 people.
- The gold price is global, so every server feels the whole player base.
- Each player only receives updates about what's near them, which keeps 200
  players smooth in a browser.

## Rewards (Season)
Separate leaderboards, so every playstyle can win:
- **Tycoon:** highest net worth
- **Top Sheriff:** most bank defenses and arrests
- **Most Wanted:** biggest bounty survived

The top of each board wins real tech. Prizes are few and big, not split thin.
Everyone else earns titles and cosmetics (hats, badges, horse skins).

**Rule:** nothing you can buy, including our coin, affects winning.

## Progression (why players keep coming back)
- **Ranks:**
  - Lawmen go Deputy, then Sheriff, then Marshal.
  - Outlaws go Drifter, then Bandit, then Gang Leader, then Legend.
  - Each rank unlocks horses, tools and cosmetics. Tools are sidegrades, not
    raw power. A faster safe-cracking kit is one example.
- **Town reputation:** every town remembers you. Be a hero in one town and
  most wanted in the next.
- **Property (like GTA Online businesses):** buy a ranch, a mining claim, a
  saloon, or a stagecoach line. Each one earns gold every trading day, and
  each one can be raided.
- **Towns grow:** Camp, then Settlement, then Town, then City. Bigger towns
  have bigger vaults, more buildings, a train station, and a listed bank
  stock. Towns that keep getting raided shrink.
- **Seasons (about 8–10 weeks):** a new frontier map each season. Gold and
  property reset. Ranks, titles and cosmetics carry over. Resets like this are
  how Tarkov and Rust keep their economies fresh.

---

## Our Coin and Creator Rewards

There are **two separate layers.**

| Layer | What it is | Who it's for |
|---|---|---|
| **The game** | In-game gold and bank stocks, not on any blockchain | Everyone. Free, and no coin needed to play or to win prizes |
| **Our coin** | A real token launched on a launchpad | Optional. Its creator fees pay for rewards |

### How the money flows
1. We launch our coin on a launchpad (options below).
2. Every trade pays a small **creator fee** into our **Rewards Treasury**.
3. The treasury is a public multisig wallet (for example Squads on Solana,
   which needs multiple signers to move funds) with a **monthly public
   report**. Showing that is how you earn trust. Friend.tech's creators walked
   off with $44M, so people will be watching.
4. The treasury pays for:
   - **~50% Season prize pool:** tech prizes plus SOL or USDC for the top
     Tycoon, Sheriff and Most Wanted players. Winning is skill-based, and you
     don't need to hold the coin to win.
   - **~30% Servers and development.**
   - **~20% Community:** tournaments, events, and giveaways for players.

### What holders get (the safe way)
- **Cosmetic perks:** a gold-trimmed "Shareholder" hat, a unique horse skin,
  and a holder badge on your name.
- **Spend the coin on cosmetics in-game.** Never on power.
- **A voice:** vote on next season's town names or the map theme.
- **Early access** to new seasons and test servers.

### Launchpad options
| Launchpad | Creator rewards | Fits us because |
|---|---|---|
| **pump.fun** | 0.05%–0.95% of every trade, set by market cap: highest (0.95%) at $88K–$300K, dropping to 0.05% at $20M. Can split across up to 10 wallets. At launch you permanently choose **Creator Fees** or **Trader Cashback**. | The biggest audience, and fees go to our treasury so we control how rewards are paid. Pick **Creator Fees**. |
| **StonkFun** | Creator sets a fee from 0% to 50%. Fees go into a reward vault paid **automatically to holders in a tokenized stock** (like NVDAx or SPYx). | Holders literally receive "stocks", which matches the theme. But paying holders just for holding is the riskiest part legally (see below). |
| **Bags** | 1% of every trade to the creator, forever | A simple, steady treasury income. |

### Reality checks (not legal advice)
- **Fees depend on trading volume.** For example, $1M of daily volume at a
  0.3% fee is about $3,000 a day. But memecoin volume usually collapses after
  launch (pump.fun's revenue fell 80% in 2025). **Only promise prizes the
  treasury already holds.** HQ Trivia died from overpromising.
- **Paying holders just for holding** (automatic dividends) looks like a
  security. The SEC's 2025 staff statement said typical meme coins aren't
  securities *because* holders don't expect profit from the team's work. A
  game coin that pays holders out of fees the team's game generates may not
  get that treatment. **Talk to a crypto lawyer before turning on holder
  payouts.**
- **Keep a free way to win.** If buying the coin were required to win prizes,
  it could count as a paid contest or gambling. Keeping prize eligibility
  free avoids that.
- **Browser game = no Steam problem.** Steam bans crypto games, but we're not
  on Steam.
- **Game first, then coin.** 90%+ of web3 games died because the token came
  first. Launch the coin once there's a playable demo and real players, so the
  hype has something behind it.

### Precedents to study
- **Supersize** (Solana): agar.io-style, where players pay tokens to enter a
  match.
- **Greedy World:** a browser battle royale where players stake memecoins and
  losers drop their tokens as loot.
- Both are paid entry with real tokens, which is the riskiest model. Ours
  keeps the game free and uses creator fees to pay for prizes.

---

## Brief to Give Grok / ChatGPT

```
Write a complete, buildable game design document for a multiplayer browser game called "Bank Run".

CONCEPT: Top-down 2D Old West sandbox (GTA-like freedom). 10 to 200 players per server, drop-in/drop-out (no lobby waiting). Every town has a bank, and every bank is a stock. Players can freely be lawmen (defend banks, escort gold, arrest outlaws, earn bank shares), outlaws (raid banks, rob stagecoaches and the gold train, fence stolen gold at hideouts), or neutral (prospect gold, trade stocks, hunt bounties). Raids crash a town's stock and cost depositors. Mass withdrawals trigger a bank run that crashes the price. Carried gold drops on death; deposits and stocks are safe but can lose value.

REFERENCES: Red Dead Online (Old West sandbox), GTA Online (wanted levels, freedom), Hunt: Showdown (high-bounty players revealed on the map), Escape from Tarkov / ARC Raiders (risk what you carry), agar.io (instant browser play, no signup).

REQUIRED SYSTEMS (give exact numbers and formulas for all):
- Global gold price shared across all servers: formula, tick rate, random events.
- Bank stock price per town: what raises it (deposits, mining, defenses, gold train arrivals) and what lowers it (robberies proportional to vault % stolen, bank-run withdrawals above a threshold). Bank failure rules.
- Trading days: short cycles ending at a "closing bell"; dividends paid by banks not robbed that day.
- Deposits: safe on death; depositors lose a % when their bank is robbed.
- Wanted system: 1-5 stars, bounty amounts, reveal on map at 3+ stars, how to clear stars.
- Hot gold: stolen gold must be fenced at a hideout (fence cut %) before it can be deposited.
- Bank raid flow: scout, dynamite (loud, fast) vs. safe-cracking (quiet, slow), alarm, carry weight and speed penalties, escape, fence.
- Defense: lawman pay, bonus shares for defenders, NPC deputies hired from bank funds, barricades, rooftop Gatling gun.
- Lawman badge: lost for the trading day if the player commits a crime.
- Gangs/posses: max size 6.
- Combat: revolver, rifle, dynamite, lasso (arrest alive = bigger bounty). Health, damage, cooldowns. Horses (speed, can be shot) and wagons (carry more, slow).
- Other activities: gold train schedule, stagecoaches, opt-in high noon duels, horse racing, gold mining claims.
- Death: drop carried gold; respawn at last town (lawmen) or hideout (outlaws); Boot Hill tombstones show gold lost.
- Scaling: 3 towns at 10 players, about +1 town per 20 players, max 12 at 200. NPC outlaw gangs raid banks at low population. Each player only receives updates for entities near them.
- Season rewards: three leaderboards (Tycoon net worth, Top Sheriff, Most Wanted); top players win real tech prizes (skill-based, no purchase required, few and large prizes). Cosmetics for everyone else.
- Bank stocks, OTC to exchange: each bank founds with a fixed share count and starts as a volatile OTC penny stock traded at the telegraph office. Shares are distributed by purchase, lawman defense bonuses, listing-day allocations to top depositors, and new share issuance when a bank expands (dilution). A bank uplists to the "Territory Exchange" after passing a deposit threshold and surviving N trading days unraided (steadier price, bigger dividends); it is delisted back to OTC if its vault is drained below a threshold. Give all numbers.
- Progression: lawman ranks (Deputy, Sheriff, Marshal) and outlaw ranks (Drifter, Bandit, Gang Leader, Legend) with unlocks (horses, sidegrade tools, cosmetics, never raw power); per-town reputation; buyable property (ranch, mining claim, saloon, stagecoach line) that earns gold each trading day and can be raided; towns grow Camp, Settlement, Town, City; seasons of 8-10 weeks where gold and property reset but ranks, titles, and cosmetics carry over.

REAL COIN LAYER (keep separate from gameplay):
- In-game gold and bank stocks are off-chain and free. A separate real coin, launched on a Solana launchpad, earns creator fees into a public multisig Rewards Treasury.
- Treasury split: ~50% season prize pool (tech + SOL/USDC to top players of each leaderboard), ~30% servers/development, ~20% community events.
- The game must be fully playable, and prizes fully winnable, WITHOUT owning the coin. Winning is skill-based only.
- Coin holders get cosmetic-only perks (Shareholder hat, horse skin, name badge), can spend the coin on cosmetics, vote on season themes/town names, and get early access. Nothing bought with the coin may affect winning.
- Design the in-game "Treasury" screen showing the public wallet balance, current prize pool, and monthly report.

DELIVER:
1. One-paragraph pitch
2. First 10 minutes for a new player
3. A trading day minute by minute
4. Controls (keyboard/mouse + mobile touch)
5. Territory and town layout (sizes, building list, hideout and mine placement)
6. Full economy with every formula and number
7. Combat, horse, and wagon stats tables
8. Wanted system table
9. UI screens and what each shows (HUD, telegraph stock ticker, map, bank, hideout, leaderboards)
10. Progression tables (ranks, unlocks, property income, town growth thresholds, season length)
11. Anti-cheat and server authority
12. MVP scope: the smallest fun version to build first (suggest: 1 server, 3 towns, bank raids and defense, OTC bank stocks, wanted system; the coin and treasury come after the MVP has players)

Be specific. Concrete numbers everywhere so a developer can implement it directly.
```

Image prompts for all the art are in [`ART_PROMPTS.md`](ART_PROMPTS.md).

---

## Sources (coin and launchpad facts)
- pump.fun creator fees: [DEXTools](https://www.dextools.io/tutorials/what-are-pump-fun-creator-rewards-how-they-work-2026), [crypto.news](https://crypto.news/pump-fun-flips-creator-fees-launches-trader-cashback/), [Yahoo Finance](https://finance.yahoo.com/news/pump-fun-overhauls-creator-fees-212457627.html)
- StonkFun: [CoinMarketCap](https://coinmarketcap.com/cmc-ai/stonk-fun/what-is/), [Phemex](https://phemex.com/blogs/stonkfun-stonk-tokenized-stocks-trading)
- Bags: [DEV Community](https://dev.to/sivarampg/bagsfm-the-solana-launchpad-thats-changing-creator-monetization-4g7n)
- SEC meme coin staff statement: [SEC.gov](https://www.sec.gov/newsroom/speeches-statements/staff-statement-meme-coins), [WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20250313-the-state-of-meme-coin-regulation-sec-staffs-statement-and-other-considerations)
- pump.fun revenue drop: [CoinMarketCap](https://coinmarketcap.com/academy/article/pumpfun-news-pumpfun-revenue-crashes-80percent-as-meme-coin-mania-fades)
- Supersize / Greedy World: [Solana Compass](https://solanacompass.com/projects/category/gaming/play-to-earn), [Greedy World](https://www.greedyworld.io/)
