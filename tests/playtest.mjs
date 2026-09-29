// Plays two minutes of Bank Run in headless Chromium and fails on any console error or broken state.
// Usage: cd tests && npm install && npm run playtest     (SECONDS=120 SPEED=1 by default)
import { chromium } from 'playwright';
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';

const here = path.dirname(fileURLToPath(import.meta.url));
const game = path.join(here, '..', 'index.html');
const SECONDS = +(process.env.SECONDS || 120), SPEED = +(process.env.SPEED || 1);
const gsapLocal = path.join(here, 'node_modules', 'gsap', 'dist', 'gsap.min.js');
const exe = ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => fs.existsSync(p));

const browser = await chromium.launch(exe ? { executablePath: exe } : {});
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
const errors = [];
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', e => errors.push('pageerror: ' + e.message));
// Serve GSAP locally when installed (CI boxes often can't reach the CDN); fonts fall back to serif.
await page.route('https://cdnjs.cloudflare.com/**', r => fs.existsSync(gsapLocal) ? r.fulfill({ path: gsapLocal, contentType: 'application/javascript' }) : r.continue());
// Stand-in for Google Fonts so offline runs log no errors (text falls back to the serif stack).
await page.route(u => u.hostname.startsWith('fonts.'), r => r.fulfill({ body: '', contentType: 'text/css' }));
await page.goto('file://' + game);
await page.waitForFunction(() => window.BR && BR.G.mode === 'title');

const fail = msg => { console.error('FAIL:', msg); process.exitCode = 1; };
const state = () => page.evaluate(() => BR.state());

// 1) real input: start from the title, walk to the Silver Creek bank with the keyboard, deposit with E then 1
await page.click('.rcard[data-role="law"]');
await page.evaluate(() => { try { localStorage.setItem('bankrun.seenHow', '1'); } catch (e) {} });
await page.click('#startBtn');
await page.waitForFunction(() => BR.G.mode === 'play');
const bankDoor = await page.evaluate(() => { const b = BR.G.banks[0].T.b.bank.door; return { x: b.x, y: b.y }; });
// hold WASD like a player: down into the street, west along it, then up to the bank door
const start = await page.evaluate(() => ({ x: BR.P.x, y: BR.P.y }));
const legs = [{ x: start.x, y: 1000 }, { x: bankDoor.x, y: 1000 }, { x: bankDoor.x, y: bankDoor.y }];
let leg = 0;
for (let i = 0; i < 160 && leg < legs.length; i++) {
  const p = await page.evaluate(() => ({ x: BR.P.x, y: BR.P.y }));
  const goal = legs[leg], dx = goal.x - p.x, dy = goal.y - p.y;
  if (Math.hypot(dx, dy) < 24) { leg++; continue; }
  const keys = [];
  if (dx < -12) keys.push('a'); if (dx > 12) keys.push('d'); if (dy < -12) keys.push('w'); if (dy > 12) keys.push('s');
  for (const k of keys) await page.keyboard.down(k);
  await page.waitForTimeout(120);
  for (const k of keys) await page.keyboard.up(k);
}
await page.keyboard.press('e'); await page.waitForTimeout(250);
const panelOpen = await page.evaluate(() => !document.querySelector('#panel').hidden);
await page.keyboard.press('1'); await page.waitForTimeout(250);
let s = await state();
if (!panelOpen) fail('bank counter did not open on E');
if (s.bank < 1) fail('keyboard deposit did not land in the bank (bank=' + s.bank + ')');
await page.keyboard.press('Escape');

// 2) autopilot through every job for the rest of the run
await page.evaluate(k => { BR.autopilot(true); BR.speed(k); }, SPEED);
const roles = ['outlaw', 'law', 'prospector', 'hunter'];
const slice = SECONDS / roles.length;
for (const role of roles) {
  await page.evaluate(r => { if (BR.P.role !== r && !(r === 'law' && BR.P.stars > 0)) BR.autopilot(true, r); }, role);
  const until = (await state()).t + slice;
  await page.waitForFunction(t => BR.G.t >= t || BR.G.mode !== 'play', until, { timeout: (slice / SPEED + 30) * 1000 });
  s = await state();
  console.log(`t=${s.t.toFixed(0)}s role=${s.role} worth=$${s.worth} carried=$${s.carried} hot=$${s.hot} bank=$${s.bank} shares=${s.shares} stars=${s.stars} hp=${s.hp} fps=${(await page.evaluate(() => BR.FPS())).toFixed(0)}`);
}
s = await state();
await page.screenshot({ path: path.join(here, 'playtest-final.png') });

// 3) checks
const finite = JSON.stringify(s).match(/NaN|Infinity|null/);
if (finite) fail('non-finite value in state: ' + finite[0]);
if (s.t < SECONDS) fail('game clock stalled at ' + s.t);
if (s.bells < Math.floor(SECONDS / 60)) fail('closing bell did not ring: ' + s.bells);
const raids = s.banks.reduce((a, b) => a + b.raids, 0);
if (raids < 2) fail('expected at least 2 raids, saw ' + raids);
if (s.banks.some(b => b.price <= 0 || b.vault < 0)) fail('a bank broke: ' + JSON.stringify(s.banks));
const st = s.stats; const acted = st.sacks + st.fenced + st.mined + st.bounties + st.defenses;
if (!acted) fail('player never did anything useful in two minutes');
if (errors.length) fail('console errors:\n' + errors.join('\n'));
console.log(process.exitCode ? 'PLAYTEST FAILED' : `PLAYTEST PASSED · ${raids} raids · ${s.bells} bells · stats ${JSON.stringify({ sacks: st.sacks, fenced: Math.round(st.fenced), mined: Math.round(st.mined), bounties: st.bounties, defenses: st.defenses, deaths: st.deaths })}`);
await browser.close();
