# Bank Run — prompts for Claude

Art is in `BankRun_ArtBible.pdf` and `bankrun_art/`. Attach `03_town.jpg`, `04_lawman.jpg`, and `05_outlaw.jpg` to the chat. Do not ask for the whole game in one message.

## What v1 is

One HTML file. One town. Top-down. Fake stocks. No wallet, no token, no server. Colored shapes first. Pictures are the look, not the sprites.

Loop: carry gold, deposit it, raid crashes the stock, lawmen who held the bank earn a share, outlaws fence hot gold at a hideout.

## Prompt 1 — the loop

Build a single index.html Old West game I can open in a browser. No build step, no libraries. Canvas, top-down. One town: dirt street, brick bank, saloon, sheriff office, telegraph, stables. WASD moves a player. E uses the building you are touching. Player has carried gold and bank gold. Die (press K for now) and drop carried gold. Deposit and withdraw at the bank. Every 45 seconds a raid starts for 20 seconds: vault opens, stock price of this bank drops based on gold stolen, depositors lose the same percent. A Law button and an Outlaw button. Lawman standing at the bank when the raid ends and the vault is over half full earns 1 share. Outlaw inside the vault during the raid can press E to take a sack. That gold is hot and cannot be deposited until they press E at a hideout marker east of town. Draw navy rectangles for law and red rectangles for outlaws. Four bot outlaws and two bot lawmen walk simple paths. Show carried gold, bank gold, shares, stock price, and wanted stars as plain text. No wallet. No server.

## Prompt 2 — the look

Keep the same file and the same rules. Restyle only. Background sandy ochre. Bank is red brick. Lawmen are navy with a silver star. Outlaws are black with a red bandana. Gold is bright yellow. Wood buildings brown. Church white. Add a top ticker with this bank price and a green or red arrow. Health is 5 bullets. Wanted is 5 stars, 3 or more draws a marker on the minimap. Do not add new game modes.

## Prompt 3 — the other jobs

Still one file. Add two more roles I can switch to any time. Prospector: stand on a claim marker north of town and press E to mine 1 gold every 3 seconds, worth the global gold price. Bounty hunter: a board at the sheriff lists bots with stars. Catch one by touching them and press E. Pay matches their stars. Closing bell every 60 seconds: if the bank was not raided this cycle, each share pays 1 gold into bank gold. If withdrawals in a cycle pass 40 percent of deposits, call it a bank run, crash the price, and freeze deposits until the next bell.

## Prompt 4 — only after it is fun

Add a second town on the same map, linked by a dirt road. Its bank is a separate stock, starts cheaper, and can be raided on its own timer. Do not add accounts, sockets, or a coin. If you need multiplayer later, say so and stop.

## Do not ask for this yet

200-player servers, seasons, ranks, ranches, the gold train, Boot Hill, uplisting, a pump.fun coin, holder payouts, a multisig treasury. Holder payouts from fees the game generates are the legally risky part. Fake gold until a lawyer says otherwise.
