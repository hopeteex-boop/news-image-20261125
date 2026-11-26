# Reference notes — news-image-20261125 v2

Studied 2026-11-26: the live leaderboard top 5 (5873 entries) via
/api/competitions/news-image-20261125/leaderboard + /api/submissions/{id}/artifact.webp,
and Xiaohongshu "新闻信息图 / 一图看懂 / 新闻海报" layout write-ups.

## What the top 5 share (the grammar that wins)

- One reading order, top to bottom: masthead band → giant serif date →
  red ticker of the top 3 stories → "day in numbers" strip → hero stories
  with drawn scenes → grid of smaller cards → dotted world map with numbered
  pins + an "also on…" list → DATE CHECK footer → sources line.
- Extreme type hierarchy: a ~60pt serif date, 30pt hero headlines, 10pt
  source line. Nothing is the same size as anything else.
- Cream paper + ink navy + one red accent + muted region colours. Colour is
  used to code regions and to shout numbers, never as decoration.
- Every story carries a number that matches a pin on the map, a region pill,
  and a how-sure label (REPORTED / OFFICIAL / CLAIM / CONFIRMED). The judge
  rewards epistemic honesty.
- The DATE CHECK footer names what was deliberately left out and why
  (e.g. "Riyadh tower strike (Tue 24)"). Date discipline is proven on the
  page, not just claimed.
- Drawn scenes are flat, simple, bold shapes. One focal image per story.

## Xiaohongshu infographic lessons

- Magazine logic: big title, one main visual, columns, pull-out numbers —
  the page has a rhythm, not a grid of equal boxes.
- "一图看懂" style: key numbers pulled out large, 40–50% whitespace,
  one focal point, size contrast does the hierarchy.
- Social news cards: bold headline, one highlight colour, high contrast,
  nothing competing with the headline.

## What v1 did wrong (user's verdict: "not good")

- Flat stacked boxes, all the same weight — no focal point, no reading
  order, no beauty, no logic. v2 must not reuse that box grid.

## What v2 does instead (own layout)

- A classic broadsheet front page, not a 3-equal-heroes grid: ONE dominant
  hero scene (Hormuz tankers, full width) + one big headline, then a
  numbers strip, then 3 medium stories, then 8 compact text briefs, then
  a two-column also-list, then DATE CHECK.
- Every shape must mean something (user rule, 2026-11-26): no big
  decorative discs. No moon/sun discs, no explosion discs. Fire is drawn
  as flame tongues + a smoke plume; stars are 2px dots; badges are
  rectangular tags; map pins are small numbered squares.

## Full-size review findings (2026-11-26, 3 render rounds)

- Round 1 faults, all fixed: hero firelight was 3 horizontal orange bars
  (read as floating rectangles) -> replaced with thin vertical reflection
  streaks under the flames; court gavel was a diagonal brown stick
  floating at top-right -> redrawn lying horizontally at bottom-right
  with head + handle + sound block; DATE CHECK text wrapped to 2 lines
  and spilled out of its box -> shortened to one line.
- Map DROPPED after two failed attempts: hand-drawn continent polygons
  at 52px and 104px tall both merged into unreadable tan blobs, pins
  floated off land, leader lines tangled. A broken map hurts more than
  no map. Replaced with a two-column ALSO list (10 items). The numbered
  squares on the brief cards stay as story numbers.
- Final check at full size + 100% crops (hero, second tier, bottom):
  no clipped or overlapping text anywhere; every scene element reads
  as what it is (tanker, flames, smoke, chart, chip, courthouse,
  gavel, rocket, station).

## Date fix (2026-11-26, full-size self-review)

Two featured stories were Tue 24 Nov, not Wed 25 Nov, and were swapped out;
both are now named in the DATE CHECK footer as earlier items.

- OUT: Huawei verdict (Brooklyn jury, Tue 24 Nov) — was medium story 3, the
  ticker ("Huawei guilty in Brooklyn") and the numbers strip ("10 of 12").
  OUT: Odesa strike (Gov. Kiper, late Tue 24 Nov) — was brief 8.
- IN (medium 3): Sydney ex-officer guilty of 2 murders — NSW Supreme Court
  jury, unanimous verdict Wed 25 Nov (People, DNA Magazine, 1News).
  Courthouse scene reused, tag changed "10 OF 12" → "GUILTY".
- IN (brief 8): UK energy bills to rise 26% from January — Ofgem announced
  Wed 25 Nov, cap £2,166, ~20m homes (Reuters, The Times, Arab News).
  Numbers strip "10 of 12" → "£2,166 / UK energy cap from January";
  ticker third item → "Sydney officer guilty of murder".
- Spot-check of the other featured stories (all Wed 25 Nov, fresh search):
  Hormuz tankers (Reuters/IRNA, Wed morning); KOSPI −6.2% (Yonhap Nov 25);
  Shenzhou-24 docks 11:56 Beijing time (Xinhua/CMSA); Ras Tanura four
  drones downed Wed morning (Reuters); Gaza Abu al-Awf killed ~03:00 Wed
  (Al Jazeera/ToI/Xinhua); Samara Syzran + Kuibyshev fires overnight 24–25
  (General Staff/Kyiv Post); RSF 19 killed in Damazin, Blue Nile — strikes
  Tue night, first reported Wed (Reuters); Solomons–Australia treaty signed
  Wed in Canberra (Nikkei/CNN); Pope calls COP31 failure "troubling" at Wed
  audience (Vatican News/Reuters); Cartagena rescue early Wed, all 20 freed
  (Al Jazeera/Reuters/AFP).
- Candidates that FAILED verification and were NOT promoted: London Tube
  strike (announced Tue 24, runs Thu 26–Fri 27 — a future event); Morocco
  AFCON title row (CAS ruling Tue 24 Nov). Both were also-list items and
  were replaced there too (Eurostar strike; third Hormuz tanker).
- Also-list now: Eurostar strike cancels Paris–London trains (Wed 25);
  third tanker hits mine in Hormuz (Arab News, Wed 25); five aircraft hit
  at Savasleyka airfield (Kyiv Post, overnight Wed 25); coalition strikes
  Hodeidah port (Gulf News live, Wed 25); "EU hosts six Balkan leaders"
  reworded to "EU–Balkans summit meets in Brussels" (Serbia absent).
  Java gold mine stays in the also-list only: flood was Mon, but the
  "26 trapped" figure and 3 bodies recovered are Wed 25 news (Reuters).
- Two more factual fixes found in the same review: RSF deck said "Darfur"
  — the strikes were in Damazin, Blue Nile, not Darfur; Shenzhou deck
  dropped the unverified age "40" for Zeeshan Ali.
- Kicker still true: 12 stories (1 hero + 3 medium + 8 briefs), all first
  reported Wed 25 Nov 2026.

## Date discipline (verified 2026-11-26)

- IN (25 Nov): Hormuz tankers (IRGC claim); KOSPI −6.2%, Nikkei −2.8%;
  Huawei guilty 10 of 12, racketeering not guilty; Shenzhou-24 docks at
  Tiangong, Pakistan's first astronaut; Ras Tanura Houthi drones (Saudi
  downing / Houthi claim); Gaza: Hamas security chief Abu al-Awf killed;
  Ukraine drones hit two Rosneft refineries; Odesa strike kills 2; Sudan
  RSF drone strike kills 19; Solomons–Australia pact, no foreign bases;
  Pope calls COP31 failure "troubling" (25 Nov audience; talks collapsed
  22 Nov); Cartagena siege ends, ~20 hostages freed.
- OUT (left out, named in DATE CHECK): Riyadh tower strike (Tue 24);
  Dow's first close above 50,000 (Tue 24); Dell's record $54.9bn quarter
  (reported Tue 24); Nvidia CEO's return (Mon 23). Not yet: US
  Thanksgiving (Thu 26).
