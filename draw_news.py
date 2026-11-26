#!/usr/bin/env python3
"""Draw entry.png v2: a broadsheet front page summing up 25 Nov 2026 world news.

Layout (own design, not the v1 flat box grid, not the winners' 3-equal-heroes
grid): one dominant hero scene + big headline, numbers strip, 3 medium
stories, 8 compact briefs, map + also-list, DATE CHECK footer.

Shape rule (user, 2026-11-26): every shape must mean something. No big
decorative discs. Fire = flame tongues + smoke plume. Stars = 2px dots.
Badges = rectangular tags. Map pins = small numbered squares.
Pure PIL drawing + DejaVu text. Output: 1024x1024 PNG.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
CARD = (253, 251, 245)
INK = (26, 26, 26)
NAVY = (18, 33, 58)
NAVY2 = (28, 52, 84)
RED = (178, 34, 24)
RED2 = (200, 48, 32)
GREY = (96, 96, 92)
LGREY = (205, 198, 182)
BORDER = (198, 190, 174)
OCHRE = (176, 124, 32)
TEAL = (38, 110, 96)
SLATE = (52, 84, 140)
PURPLE = (110, 70, 150)
GREEN = (70, 120, 70)
GOLD = (160, 120, 30)
RUST = (160, 60, 40)
TAN = (206, 192, 168)
TAN_LINE = (178, 162, 136)
SEA_TOP = (18, 44, 68)
SEA_BOT = (10, 26, 46)
SKY_TOP = (13, 24, 46)
SKY_MID = (36, 50, 82)
DUSK = (198, 112, 60)
FLAME = (242, 107, 29)
FLAME2 = (255, 197, 61)
SMOKE = (88, 88, 94)
SMOKE2 = (120, 120, 126)

F = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(F + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(text, fnt, max_w, draw):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def center(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def flame(draw, cx, base_y, w, h, col1=FLAME, col2=FLAME2):
    """Teardrop flame tongues. Outer flame + inner flame."""
    pts = [
        (cx, base_y - h),
        (cx + w * 0.42, base_y - h * 0.55),
        (cx + w * 0.30, base_y - h * 0.28),
        (cx + w * 0.48, base_y),
        (cx - w * 0.48, base_y),
        (cx - w * 0.30, base_y - h * 0.28),
        (cx - w * 0.42, base_y - h * 0.55),
    ]
    draw.polygon(pts, fill=col1)
    iw, ih = w * 0.5, h * 0.55
    pts2 = [
        (cx, base_y - ih),
        (cx + iw * 0.42, base_y - ih * 0.55),
        (cx + iw * 0.48, base_y),
        (cx - iw * 0.48, base_y),
        (cx - iw * 0.42, base_y - ih * 0.55),
    ]
    draw.polygon(pts2, fill=col2)


def smoke_plume(draw, x, top_y, base_y, w, drift=0):
    """A rising smoke plume: tapered wavy column, clearly attached to a fire.
    One continuous polygon, not stacked discs."""
    steps = 6
    left, right = [], []
    for i in range(steps + 1):
        t = i / steps
        y = base_y - t * (base_y - top_y)
        half = w * (0.5 + 0.35 * t) * (1 - 0.25 * t)
        wob = math.sin(t * 9.0) * w * 0.18
        cx = x + drift * t + wob
        left.append((cx - half, y))
        right.append((cx + half, y))
    draw.polygon(left + right[::-1], fill=SMOKE)
    left2, right2 = [], []
    for i in range(steps + 1):
        t = i / steps
        y = base_y - t * (base_y - top_y)
        half = w * 0.28 * (1 - 0.2 * t)
        wob = math.sin(t * 9.0 + 1.2) * w * 0.12
        cx = x + drift * t + wob
        left2.append((cx - half, y))
        right2.append((cx + half, y))
    draw.polygon(left2 + right2[::-1], fill=SMOKE2)


def pill(draw, x, y, text, fnt, fg, outline):
    """Small outlined label (how-sure tag). Returns width used."""
    tw = draw.textlength(text, font=fnt)
    w = tw + 10
    h = 15
    draw.rectangle([x, y, x + w, y + h], outline=outline, width=1)
    draw.text((x + 5, y + 2), text, font=fnt, fill=fg)
    return w


def num_square(draw, x, y, n, size=15):
    draw.rectangle([x, y, x + size, y + size], fill=RED)
    f = SANS_B(10)
    t = str(n)
    draw.text((x + (size - draw.textlength(t, font=f)) / 2, y + 2), t, font=f, fill=(255, 255, 255))


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
X0, X1 = 28, 996
CW = X1 - X0

# ---------------------------------------------------------------- top band
d.rectangle([0, 0, W, 26], fill=NAVY)
d.text((28, 6), "THE WORLD IN ONE DAY", font=SANS_B(13), fill=(250, 246, 238))
rt = "12 STORIES  ·  ALL FIRST REPORTED WED 25 NOV 2026"
d.text((X1 - d.textlength(rt, font=SANS(10)), 7), rt, font=SANS(10), fill=(210, 208, 198))

# ---------------------------------------------------------------- masthead
size = 56
while d.textlength("Wednesday 25 November 2026", font=SERIF_B(size)) > CW and size > 40:
    size -= 2
center(d, W // 2, 32, "Wednesday 25 November 2026", SERIF_B(size), NAVY)

# ---------------------------------------------------------------- ticker
tick = "Tankers burn in Hormuz  ·  Asian chip stocks crash  ·  Sydney officer guilty of murder"
center(d, W // 2, 98, tick, SANS_B(13), RED)
d.rectangle([X0, 120, X1, 122], fill=NAVY)

# ---------------------------------------------------------------- hero scene
hx0, hy0, hx1, hy1 = X0, 128, X1, 288
horizon = 230
stops = [(SKY_TOP, 0.0), (SKY_MID, 0.55), (DUSK, 0.86), ((232, 148, 84), 1.0)]
for yy in range(hy0, horizon):
    t = (yy - hy0) / (horizon - hy0)
    for i in range(len(stops) - 1):
        c0, t0 = stops[i]
        c1, t1 = stops[i + 1]
        if t0 <= t <= t1:
            f = (t - t0) / (t1 - t0) if t1 > t0 else 0
            col = tuple(int(c0[k] + (c1[k] - c0[k]) * f) for k in range(3))
            break
    else:
        col = stops[-1][0]
    d.line([(hx0, yy), (hx1, yy)], fill=col)
# stars: tiny 2px dots, upper sky only (they are stars, nothing else)
rnd = random.Random(7)
for _ in range(46):
    sx = rnd.randint(hx0 + 6, hx1 - 6)
    sy = rnd.randint(hy0 + 6, hy0 + 70)
    d.rectangle([sx, sy, sx + 1, sy + 1], fill=(205, 210, 225))
# sea
for yy in range(horizon, hy1):
    t = (yy - horizon) / (hy1 - horizon)
    col = tuple(int(SEA_TOP[k] + (SEA_BOT[k] - SEA_TOP[k]) * t) for k in range(3))
    d.line([(hx0, yy), (hx1, yy)], fill=col)
d.line([(hx0, horizon), (hx1, horizon)], fill=(150, 120, 90), width=1)
# (ChatGPT review: the two orange vertical streaks under the water had no
# label and read as mines/pipes/hull — removed.)
# distant second tanker (small silhouette, right)
d.polygon([(806, horizon), (806, horizon - 14), (822, horizon - 14), (822, horizon - 20),
           (836, horizon - 20), (836, horizon - 14), (918, horizon - 14), (926, horizon)],
          fill=(12, 22, 38))
d.rectangle([848, horizon - 26, 862, horizon - 14], fill=(12, 22, 38))
flame(d, 872, horizon - 14, 16, 22)
smoke_plume(d, 876, horizon - 56, horizon - 20, 9, drift=10)
# main tanker (centre-left): hull + containers + bridge
d.polygon([(330, horizon), (330, horizon - 20), (700, horizon - 20), (716, horizon)], fill=(14, 24, 40))
d.rectangle([330, horizon - 20, 700, horizon - 15], fill=(20, 32, 52))
d.rectangle([330, horizon - 5, 716, horizon - 2], fill=(210, 210, 205))
d.rectangle([352, horizon - 38, 402, horizon - 16], fill=(158, 74, 44))
d.rectangle([408, horizon - 32, 452, horizon - 16], fill=(52, 96, 92))
d.rectangle([458, horizon - 44, 512, horizon - 16], fill=(176, 124, 32))
# bridge tower with lit windows (small yellow squares = windows)
d.rectangle([640, horizon - 56, 688, horizon - 16], fill=(228, 226, 220))
for wy in (horizon - 50, horizon - 40, horizon - 30):
    for wx in (646, 658, 670):
        d.rectangle([wx, wy, wx + 6, wy + 5], fill=(255, 197, 61))
d.rectangle([640, horizon - 62, 688, horizon - 56], fill=RED)
# fire at mid-ship: three flame tongues + smoke plume
flame(d, 560, horizon - 16, 44, 62)
flame(d, 528, horizon - 16, 28, 40)
flame(d, 594, horizon - 16, 30, 46)
smoke_plume(d, 566, horizon - 88, horizon - 42, 26, drift=16)
# wave lines
for wy in (horizon + 14, horizon + 28, horizon + 42):
    d.line([(hx0 + 30, wy), (hx1 - 60, wy)], fill=(52, 84, 112), width=1)
# tags on the scene
d.rectangle([hx0 + 10, hy0 + 10, hx0 + 10 + 168, hy0 + 30], fill=RED)
d.text((hx0 + 20, hy0 + 14), "2 TANKERS ABLAZE", font=SANS_B(12), fill=(255, 255, 255))
d.rectangle([hx1 - 158, hy1 - 26, hx1 - 10, hy1 - 8], fill=(10, 20, 35))
d.text((hx1 - 148, hy1 - 23), "STRAIT OF HORMUZ", font=SANS_B(10), fill=(255, 255, 255))

# ---------------------------------------------------------------- hero text
kick = "STRAIT OF HORMUZ  ·  GULF"
d.text((X0, 296), kick, font=SANS_B(11), fill=OCHRE)
pw = pill(d, X0 + d.textlength(kick, font=SANS_B(11)) + 12, 296, "CLAIM", SANS_B(9), RED, RED)
d.text((X0 + d.textlength(kick, font=SANS_B(11)) + 12 + pw + 8, 298), "Reuters", font=SANS(9), fill=GREY)
hl = ["Iran says mines set two tankers", "on fire in the Strait of Hormuz"]
y = 314
for line in hl:
    d.text((X0, y), line, font=SERIF_B(30), fill=INK)
    y += 36
deck = "The IRGC navy says the ships took an \u2018unauthorised route\u2019 and their engine rooms caught fire in the early hours. The claim could not be independently verified."
y = 390
for line in wrap(deck, SANS(13), CW, d):
    d.text((X0, y), line, font=SANS(13), fill=(60, 60, 58))
    y += 16

# ---------------------------------------------------------------- numbers strip
d.line([(X0, 430), (X1, 430)], fill=LGREY, width=1)
nums = [
    ("-6.2%", RED, "Kospi close, worst day of the AI sell-off"),
    ("2", NAVY, "tankers hit mines in the Strait of Hormuz"),
    ("£2,166", NAVY, "Ofgem energy cap Jan–Mar 2027"),
    ("19", RED, "19 killed, 20 wounded across Blue Nile state"),
    ("1st", OCHRE, "foreigner to fly to China's space station"),
]
cellw = CW / 5
for i, (num, col, cap) in enumerate(nums):
    cx = X0 + i * cellw
    d.text((cx + 8, 436), num, font=SANS_B(26), fill=col)
    cy = 470
    for line in wrap(cap, SANS(10), cellw - 16, d)[:2]:
        d.text((cx + 8, cy), line, font=SANS(10), fill=GREY)
        cy += 12
    if i:
        d.line([(cx, 436), (cx, 492)], fill=LGREY, width=1)
d.line([(X0, 500), (X1, 500)], fill=LGREY, width=1)

# ---------------------------------------------------------------- second tier (3 medium stories)
def chip_icon(draw, x, y, s=26):
    """A microchip: square body + pins. Reads as a chip, not a disc."""
    draw.rectangle([x, y, x + s, y + s], fill=(228, 228, 224), outline=(255, 255, 255), width=1)
    draw.rectangle([x + 7, y + 7, x + s - 7, y + s - 7], outline=(16, 28, 48), width=1)
    for k in range(3):
        px = x + 5 + k * 8
        draw.line([(px, y - 4), (px, y)], fill=(228, 228, 224), width=2)
        draw.line([(px, y + s), (px, y + s + 4)], fill=(228, 228, 224), width=2)
        py = y + 5 + k * 8
        draw.line([(x - 4, py), (x, py)], fill=(228, 228, 224), width=2)
        draw.line([(x + s, py), (x + s + 4, py)], fill=(228, 228, 224), width=2)


def scene_markets(draw, x0, y0, w, h):
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(16, 28, 48))
    for gy in (y0 + 20, y0 + 40, y0 + 60):
        draw.line([(x0 + 8, gy), (x0 + w - 8, gy)], fill=(38, 56, 84), width=1)
    pts = [(x0 + 10, y0 + 16), (x0 + 60, y0 + 28), (x0 + 110, y0 + 24),
           (x0 + 160, y0 + 40), (x0 + 210, y0 + 48), (x0 + 250, y0 + 62)]
    draw.line(pts, fill=RED2, width=3, joint="curve")
    ax, ay = pts[-1]
    draw.polygon([(ax, ay), (ax - 12, ay - 2), (ax - 4, ay - 10)], fill=RED2)
    chip_icon(draw, x0 + w - 44, y0 + 12, s=20)
    draw.rectangle([x0 + 10, y0 + 8, x0 + 118, y0 + 28], fill=RED)
    draw.text((x0 + 18, y0 + 11), "KOSPI -6.2%", font=SANS_B(11), fill=(255, 255, 255))


def scene_court(draw, x0, y0, w, h):
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(232, 226, 210))
    # courthouse: narrower pediment + thick columns + steps
    draw.polygon([(x0 + 100, y0 + 6), (x0 + w - 100, y0 + 6), (x0 + w // 2, y0 + 26)], fill=NAVY2)
    draw.rectangle([x0 + 92, y0 + 26, x0 + w - 92, y0 + 34], fill=NAVY2)
    for cx in (x0 + 104, x0 + 140, x0 + 176, x0 + 212):
        draw.rectangle([cx, y0 + 34, cx + 14, y0 + 62], fill=(250, 248, 242), outline=NAVY2, width=1)
    for i, sy in enumerate((y0 + 62, y0 + 67, y0 + 72)):
        draw.rectangle([x0 + 80, sy, x0 + w - 80, sy + 4], fill=(198, 190, 174))
    # gavel lying horizontally at bottom-right, enlarged so it reads clearly:
    # head + handle + sound block
    draw.rectangle([x0 + w - 108, y0 + 48, x0 + w - 66, y0 + 62], fill=(110, 72, 40))
    draw.rectangle([x0 + w - 66, y0 + 53, x0 + w - 14, y0 + 58], fill=(140, 100, 52))
    draw.rectangle([x0 + w - 104, y0 + 64, x0 + w - 72, y0 + 70], fill=(90, 64, 30))
    draw.rectangle([x0 + 10, y0 + 8, x0 + 92, y0 + 28], fill=RED)
    draw.text((x0 + 18, y0 + 11), "GUILTY", font=SANS_B(11), fill=(255, 255, 255))


def scene_space(draw, x0, y0, w, h):
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=(12, 22, 44))
    rnd = random.Random(11)
    for _ in range(26):
        sx = rnd.randint(x0 + 6, x0 + w - 6)
        sy = rnd.randint(y0 + 6, y0 + h - 6)
        draw.rectangle([sx, sy, sx + 1, sy + 1], fill=(205, 210, 225))
    # Docked side view: Shenzhou capsule (left) joined to the Tiangong
    # station module (right) through a visible docking ring. No flame —
    # the craft is docked, engines off.
    # Shenzhou capsule: body + tapered nose pointing right
    draw.rectangle([x0 + 84, y0 + 30, x0 + 148, y0 + 48], fill=(240, 240, 236))
    draw.polygon([(x0 + 148, y0 + 30), (x0 + 160, y0 + 39), (x0 + 148, y0 + 48)], fill=(224, 224, 220))
    draw.rectangle([x0 + 96, y0 + 36, x0 + 104, y0 + 42], fill=(28, 52, 84))
    # docking ring
    draw.rectangle([x0 + 160, y0 + 33, x0 + 168, y0 + 45], fill=(120, 120, 116))
    # Tiangong station module with solar panels
    draw.rectangle([x0 + 168, y0 + 28, x0 + 282, y0 + 50], fill=(210, 210, 206))
    draw.rectangle([x0 + 168, y0 + 28, x0 + 176, y0 + 50], fill=(170, 170, 166))
    draw.rectangle([x0 + 196, y0 + 14, x0 + 252, y0 + 26], fill=(52, 84, 140))
    draw.rectangle([x0 + 196, y0 + 52, x0 + 252, y0 + 64], fill=(52, 84, 140))
    for px in (210, 224, 238):
        draw.line([(px, y0 + 14), (px, y0 + 26)], fill=(30, 56, 100), width=1)
        draw.line([(px, y0 + 52), (px, y0 + 64)], fill=(30, 56, 100), width=1)
    draw.line([(x0 + 266, y0 + 28), (x0 + 266, y0 + 18)], fill=(210, 210, 206), width=2)
    draw.rectangle([x0 + 265, y0 + 16, x0 + 267, y0 + 18], fill=(255, 197, 61))
    d.text((x0 + 8, y0 + h - 18), "TIANGONG", font=SANS_B(10), fill=(255, 255, 255))


second = [
    ("SEOUL · TOKYO · TAIPEI — MARKETS", NAVY2, "REPORTED",
     "AI doubts crash Asia's chip stocks",
     "Kospi ends -6.2%; SK Hynix -11.1%, Samsung -9.9%, Nikkei -2.8%. — Yonhap", scene_markets),
    ("SYDNEY · TRIAL", NAVY2, "REPORTED",
     "Sydney ex-officer guilty of 2 murders",
     "Jury convicts Lamarre-Condon over Baird and Davies killings. — ABC", scene_court),
    ("JIUQUAN · SPACE", NAVY2, "OFFICIAL",
     "Shenzhou-24 docks at Tiangong",
     "Pakistan's Zeeshan Ali is the first foreigner aboard China's station. — Xinhua", scene_space),
]
ty = 506
colw = (CW - 2 * 14) // 3
for i, (kick, kcol, sure, head, deck2, scene) in enumerate(second):
    cx = X0 + i * (colw + 14)
    scene(d, cx, ty, colw, 78)
    d.text((cx, ty + 84), kick, font=SANS_B(10), fill=kcol)
    pill(d, cx + colw - 78, ty + 83, sure, SANS_B(8), NAVY, NAVY)
    hy = ty + 100
    for line in wrap(head, SERIF_B(17), colw, d)[:2]:
        d.text((cx, hy), line, font=SERIF_B(17), fill=INK)
        hy += 19
    dy = hy + 2
    for line in wrap(deck2, SANS(11), colw, d)[:2]:
        d.text((cx, dy), line, font=SANS(11), fill=(60, 60, 58))
        dy += 14

# ---------------------------------------------------------------- third tier (8 compact briefs)
third = [
    (5, "RAS TANURA · WAR", RUST, "REPORTED",
     "Saudi Arabia intercepts four drones near Ras Tanura",
     "Four downed, no casualties; Houthis claim refinery hit, unconfirmed.", "Reuters"),
    (6, "GAZA CITY · WAR", RUST, "REPORTED",
     "Israel kills Hamas security chief",
     "Hamas says Abu al-Awf died with his wife and two daughters.", "Times of Israel"),
    (7, "SAMARA · WAR", RUST, "REPORTED",
     "Ukraine drones set two refineries ablaze",
     "Syzran and Kuibyshev burn after overnight raid.", "Kyiv Independent"),
    (8, "LONDON · ECONOMY", NAVY2, "REPORTED",
     "UK energy bills to rise 26% from January",
     "Cap affects around 20m households on standard variable tariffs.", "Ofgem"),
    (9, "KHARTOUM · WAR", RUST, "REPORTED",
     "RSF drone strike kills 19 civilians",
     "19 killed and 20 wounded across Blue Nile state, rights group says.", "Reuters"),
    (10, "CANBERRA · DIPLOMACY", NAVY2, "OFFICIAL",
     "Solomons sign pact with Australia",
     "Australia and Solomon Islands sign landmark bilateral treaty.", "DFAT"),
    (11, "VATICAN · CLIMATE", NAVY2, "OFFICIAL",
     "Pope calls COP31 failure \u2018troubling\u2019",
     "Urges action after talks collapse in Antalya.", "Reuters"),
    (12, "CARTAGENA · CRIME", NAVY2, "REPORTED",
     "All hostages freed after Cartagena supermarket siege",
     "Siege began 24 Nov; police stormed it 25 Nov, all freed, one gunman dead.", "AP"),
]
tcolw = (CW - 3 * 12) // 4
trow_h = 100
for row in range(2):
    ry = 678 + row * (trow_h + 6)
    for col in range(4):
        n, kick, kcol, sure, head, deck3, src3 = third[row * 4 + col]
        cx = X0 + col * (tcolw + 12)
        d.rectangle([cx, ry, cx + tcolw, ry + trow_h], fill=CARD, outline=BORDER, width=1)
        d.rectangle([cx, ry, cx + tcolw, ry + 2], fill=kcol)
        num_square(d, cx + 8, ry + 10, n)
        d.text((cx + 29, ry + 11), kick, font=SANS_B(9), fill=kcol)
        sw = d.textlength(src3, font=SANS(8))
        d.text((cx + tcolw - 8 - sw, ry + 11), src3, font=SANS(8), fill=GREY)
        hy = ry + 30
        for line in wrap(head, SERIF_B(13), tcolw - 20, d)[:3]:
            d.text((cx + 10, hy), line, font=SERIF_B(13), fill=INK)
            hy += 14
        dy = hy + 2
        for line in wrap(deck3, SANS(10), tcolw - 20, d)[:2]:
            d.text((cx + 10, dy), line, font=SANS(10), fill=(70, 70, 66))
            dy += 12

# ---------------------------------------------------------------- bottom: also-list, two columns
# (No map: hand-drawn continents at this size merged into unreadable blobs
# in full-size review, twice. A clean two-column also-list reads better.)
d.line([(X0, 890), (X1, 890)], fill=LGREY, width=1)
d.text((X0, 896), "ALSO ON WEDNESDAY 25 NOVEMBER", font=SANS_B(10), fill=INK)
also_left = [
    "Bangladesh garment pay up 36% after unrest",
    "Australia inflation jumps to 4.9% in October",
    "26 trapped as river floods a Java gold mine",
    "Eurostar strike cancels Paris\u2013London trains",
]
also_right = [
    "Army destroys 5 tons of lead azide",
    "Five aircraft hit at Russian airfield",
    "Coalition strikes Hodeidah port",
]
for col_x, items in ((X0, also_left), (X0 + 500, also_right)):
    ay = 912
    for item in items:
        d.rectangle([col_x, ay + 3, col_x + 5, ay + 8], fill=RED)
        d.text((col_x + 11, ay), item, font=SANS(10), fill=INK)
        ay += 14

# ---------------------------------------------------------------- date check + sources
d.rectangle([X0, 974, X1, 1002], outline=RED, width=1)
d.text((X0 + 8, 978), "DATE CHECK", font=SANS_B(10), fill=RED)
dc1 = "Left out as earlier: Riyadh tower (Tue 24) · Huawei verdict (Tue 24) · Odesa strike (Tue 24) ·"
dc2 = "Dow 50,000 (Tue 24) · Dell $54.9bn (Tue 24) · Nvidia return (Mon 23)."
d.text((X0 + 100, 978), dc1, font=SANS(10), fill=(60, 60, 58))
d.text((X0 + 100, 990), dc2, font=SANS(10), fill=(60, 60, 58))
src = ("Sources: Reuters · AP · AFP · Vatican News · Al Jazeera · SCMP · Yonhap — drawings original, drawn in code.  "
       "REPORTED wire reports · OFFICIAL authority's own word · CLAIM one side's account")
d.text((X0, 1006), src, font=SANS(10), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
