# Game Ideas: Win Real Tech

Game concepts where the prizes are real tech: earbuds, keyboards, SSDs, GPUs,
consoles, gift cards. Each one is built so the reward fits the game's theme.

---

## 1. Speedrun Assembly (recommended starting point)
**Pitch:** A timed "build the PC" game. You get a pile of parts and have to
seat the CPU, apply thermal paste, route cables and pick parts that work
together before the clock runs out. Wrong RAM for the board means a time
penalty.

- **Win condition:** Fastest clean build on the weekly leaderboard.
- **Reward tie-in:** The top player wins a real part from that week's build
  (SSD one week, GPU another). The prize is the thing you just built.
- **Why it works:** Pure skill, short sessions, obvious sponsor fit
  (hardware brands, retailers).
- **Build effort:** Low to medium. A 2D drag-and-drop web game.

## 2. Circuit Breaker (daily puzzle)
**Pitch:** A daily puzzle like Wordle. Route power from the battery to every
component on a circuit board in the fewest moves, using wires, resistors and
switches.

- **Win condition:** Streaks and move-efficiency score. Monthly champions.
- **Reward tie-in:** Monthly top 3 win gadgets. A 30-day streak unlocks a
  small reward (for example a $10 gift card) for anyone who reaches it.
- **Why it works:** Daily habit loop, shareable results grid.
- **Build effort:** Low.

## 3. Bug Bounty Hunter
**Pitch:** You're shown a short code snippet that has a bug in it. Find it
fast. Levels get harder: off-by-one errors, race conditions, security holes.

- **Win condition:** Points for speed and accuracy. Seasonal ranks.
- **Reward tie-in:** Developer gear: mechanical keyboards, Raspberry Pi kits,
  monitors.
- **Why it works:** Teaches something useful, which appeals to schools,
  bootcamps and tech employers as sponsors.
- **Build effort:** Low to medium. The main work is writing the puzzles.

## 4. Crack the Vault
**Pitch:** A light escape-room or capture-the-flag game. Each vault holds a
real prize and is locked behind layered puzzles: ciphers, logic, hidden
clues in images.

- **Win condition:** First player to crack a vault gets what's inside.
- **Reward tie-in:** Every vault shows its prize up front ("Vault #7:
  Nintendo Switch").
- **Why it works:** High hype and community solving. A new vault drop is an
  event.
- **Build effort:** Medium. Needs server-side answer checking so nobody can
  cheat by reading the page source.

## 5. Scrapyard Engineer
**Pitch:** Build battle robots from salvaged parts, then fight other players'
builds automatically (you set up the bot, the fight plays out without you).

- **Win condition:** Seasonal tournament bracket.
- **Reward tie-in:** In-game parts are named after real gear, and champions
  win the real version.
- **Why it works:** Deep replay value and room for a long-running community.
- **Build effort:** High.

## 6. Signal Hunt (in-person / events)
**Pitch:** A real-world scavenger hunt. Scan QR codes or NFC tags hidden
around a campus, venue or city, and each scan unlocks a clue to the next.

- **Win condition:** Finish the route. The fastest finishers or the first N
  to finish win.
- **Reward tie-in:** Tech prizes handed out at a booth at the finish.
- **Why it works:** Great for conventions, school events and store openings.
- **Build effort:** Low. A mobile web app plus printed tags.

## 7. Startup Tycoon
**Pitch:** An idle/management game. Grow a tech startup from a garage to an
IPO by hiring, shipping products and surviving market crashes.

- **Win condition:** Reaching milestones (Series A, first 1M users).
- **Reward tie-in:** Milestones earn credits you can spend in a real prize
  shop.
- **Why it works:** Long-term engagement.
- **Build effort:** Medium. The in-game economy needs careful balancing so
  credits don't come too easily.

---

## Reward System Options

| Model | How it works | Pros | Watch out for |
|---|---|---|---|
| **Leaderboard seasons** | Top N each week or month win | Simple, skill-based, easy to explain | Cheaters and bots, so validate scores on the server |
| **First to finish** | First N to beat a challenge win | Creates hype and urgency | Time zones feel unfair, so stagger the drops |
| **Prize shop** | Earn credits and redeem them for gift cards or gear | Rewards everyone, not just the top players | Economy inflation, farming, cost control |
| **Milestone unlocks** | Hitting X (a streak, a level) earns a set reward | Clear goals | Budget: cap how many can be claimed |
| **Sponsor drops** | Brands supply the prizes | Free prizes, marketing reach | Sponsor obligations and branding rules |

**Suggested tiers:**
- Everyone: badges and cosmetics (free to give out)
- Regulars: small gift cards, stickers, cables
- Top players: earbuds, keyboards, controllers
- Champions: consoles, GPUs, phones

---

## Legal and Practical Notes (not legal advice)

- **Avoid "pay + chance + prize".** In the US, if players pay to enter *and*
  the winner is picked by luck, that is generally an illegal lottery. Keep
  winning **skill-based**, or if there's any random draw, offer a
  **free way to enter** ("no purchase necessary").
- **Taxes:** In the US, a winner who receives $600 or more in prizes in a
  year typically gets a 1099. Collect winner info before shipping.
- **Official rules page:** eligibility (age, countries), dates, how winners
  are chosen, prize values.
- **Anti-cheat:** Validate scores on the server, rate-limit, and review top
  scores before paying out.
- **Shipping:** Decide early whether you'll ship internationally. Customs and
  cost add up fast.
- Talk to a lawyer before running prizes at real scale.

---

## Recommended First Build

**Speedrun Assembly** is the one to start with:
1. Small scope: a single-screen web game, and a prototype is realistic in a
   weekend.
2. Pure skill, so it's the cleanest legally.
3. The prize is the same kind of part the player just installed.
4. Easy to pitch to hardware sponsors.

**Minimum playable version:** one PC case, 6 to 8 parts to place, a
compatibility check, a timer, and a leaderboard.
