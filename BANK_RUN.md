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

**Rules:** in-game gold only. No real-money purchases, no crypto or NFTs in
version 1, and nothing you can buy affects winning.

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
- In-game gold only. NO real-money purchases, crypto, or NFTs in version 1. Nothing money can buy may affect winning.

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
10. Anti-cheat and server authority
11. MVP scope: the smallest fun version to build first (suggest: 1 server, 3 towns, bank raids and defense, bank stocks, wanted system)

Be specific. Concrete numbers everywhere so a developer can implement it directly.
```

Image prompts for all the art are in [`ART_PROMPTS.md`](ART_PROMPTS.md).
