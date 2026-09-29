# Bank Run: build status

Playable file: `index.html` (open it directly in a browser, or use the hosted link).
Automated test: `cd tests && npm install && npm run playtest` (plays two minutes headless and fails on any console error).

## Checklist

- [x] Prompt 1: the loop. One town, WASD + E, carried vs bank gold, K to die and drop gold, deposit/withdraw, raid every 45 s for 20 s, stock and deposits drop by the percent stolen, Law/Outlaw buttons, lawman share when the vault ends over half, hot gold fenced at the hideout east of town, 4 outlaw + 2 lawman bots per town.
- [x] Prompt 2: the look. Sandy ochre ground, red-brick bank, navy lawmen with silver stars, black-and-red-bandana outlaws, bright gold, brown wood, white church, top ticker with green/red arrows, 5-bullet health, 5 wanted stars with a minimap marker at 3+.
- [x] Prompt 3: prospector claim north of each town (1 oz every 3 s at the gold price), bounty board at the sheriff (pay = stars), closing bell every 60 s with dividends for unrobbed banks, bank run at 40% withdrawals (crash + deposit freeze until the bell).
- [x] Prompt 4: Red Rock, a second town on a dirt road with its own cheaper stock (RRT) and its own raid timer.
- [x] Title screen with job picker, 30-second how-to (auto-shown on first ride), Frontier Gazette results screen, local high scores.
- [x] Scored 6-minute trading day (6 bells). Goals: lawman holds 3 raids, outlaw fences $400, prospector mines $250, hunter brings in 4. Score = net worth + $150 per goal met.
- [x] Bots feel alive: the gang gathers, plants dynamite, loots, flees the law and fences at the hideout. Lawmen patrol, answer the bell, guard the blast hole, and chase and shoot wanted players. Townsfolk wander and scatter at gunfire.
- [x] Game feel: trauma screen shake, hit-stop and flash on dynamite, 60 coins bursting from the vault, debris, smoke, drifting dust, tumbleweeds, smooth look-ahead camera with raid zoom, GSAP-animated HUD and ticker, Web Audio SFX (boom, shots, coins, church bell, fuse, cash register).
- [x] Visuals match bankrun_art (palette, silhouettes, team colours; checked at phone size).
- [~] Phone play: touch joystick, context action button, portrait + landscape layouts verified in screenshots. Adaptive quality drops resolution if frames sag. Not measured on a real mid-range phone yet.
- [x] Balance: headless bot-only sims (`BR.simDay(role)`), four roles within about 25% of each other; stocks swing 20-130% of open without breaking (floor at 22%).
- [x] Zero console errors; `tests/playtest.mjs` plays 2 minutes (keyboard walk + deposit, then all four jobs) and passes.
- [x] First-time-player review by a subagent. Top 3 fixed: (1) roles were passive/AFK-able, so lawmen now cuff raiders and claims thin out; (2) unseen punishment, so the blast radius shows during the fuse and dying keeps half your clean gold; (3) walled-off hideout, now opened toward town, with a target arrow everywhere.
- [x] Decluttered HUD after player feedback: one stock price, one objective line with an arrow to the target, money + health, stars only when wanted.

## Balance log (average of 4 simulated days per role, autopilot player)

| Role | Score | Notes |
| --- | --- | --- |
| Lawman | 813 | ~6 defenses/day; a defended bank's stock climbs, so shares carry the lawman |
| Outlaw | 653 | ~$730 fenced, ~1 death/day |
| Prospector | 518 (before a small claim buff) | switches claims as veins thin |
| Bounty hunter | 569 | ~6 catches/day |

Out of scope on purpose (from BankRun_ClaudePrompts.md): servers, accounts, wallets, coin, seasons, ranks, gold train, Boot Hill, uplisting.
