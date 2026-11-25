#!/usr/bin/env python3
"""Draw entry.png: a newspaper front page summing up 25 Nov 2026 world news.
Pure PIL drawing + DejaVu text. Output: 1024x1024 PNG."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
NAVY = (20, 36, 62)
NAVY2 = (22, 50, 79)
GOLD = (217, 164, 65)
RED = (178, 34, 24)
INK = (24, 24, 24)
GREY = (90, 90, 86)
SEA = (22, 50, 79)
FLAME = (242, 107, 29)
FLAME2 = (255, 197, 61)
CARD = (255, 255, 255)
BORDER = (200, 192, 176)

F = "/usr/share/fonts/truetype/dejavu/"

def font(name, size):
    return ImageFont.truetype(F + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
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

def rot_rect(draw, cx, cy, w, h, angle_deg, fill):
    a = math.radians(angle_deg)
    ca, sa = math.cos(a), math.sin(a)
    pts = []
    for dx, dy in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]:
        pts.append((cx + dx*ca - dy*sa, cy + dx*sa + dy*ca))
    draw.polygon(pts, fill=fill)

def flame(draw, cx, base_y, w, h, col1=FLAME, col2=FLAME2):
    # simple teardrop flame: polygon with wavy sides
    pts = [
        (cx, base_y - h),
        (cx + w*0.42, base_y - h*0.55),
        (cx + w*0.30, base_y - h*0.28),
        (cx + w*0.48, base_y),
        (cx - w*0.48, base_y),
        (cx - w*0.30, base_y - h*0.28),
        (cx - w*0.42, base_y - h*0.55),
    ]
    draw.polygon(pts, fill=col1)
    # inner flame
    iw, ih = w*0.5, h*0.55
    pts2 = [
        (cx, base_y - ih),
        (cx + iw*0.42, base_y - ih*0.55),
        (cx + iw*0.48, base_y),
        (cx - iw*0.48, base_y),
        (cx - iw*0.42, base_y - ih*0.55),
    ]
    draw.polygon(pts2, fill=col2)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 128], fill=NAVY)
center(d, W//2, 18, "THE WORLD IN ONE IMAGE", SERIF_B(58), (255, 255, 255))
center(d, W//2, 88, "WEDNESDAY  25  NOVEMBER  2026", SANS_B(30), GOLD)
d.rectangle([0, 128, W, 133], fill=GOLD)

# ---------- lead story ----------
LX, LY, LW, LH = 16, 140, 992, 272
d.rectangle([LX, LY, LX+LW, LY+LH], fill=CARD, outline=BORDER, width=2)
# illustration: sea + tanker, left half
IX, IY, IW, IH = LX+8, LY+8, 500, LH-16
d.rectangle([IX, IY, IX+IW, IY+IH], fill=SEA)
# waves
for wx in range(IX, IX+IW, 46):
    d.arc([wx, IY+IH-58, wx+44, IY+IH-30], 180, 360, fill=(90, 140, 190), width=3)
# tanker hull
hx0, hy0 = IX+40, IY+IH-108
hull = [(hx0, hy0), (hx0+380, hy0), (hx0+420, hy0+34), (hx0+400, hy0+62),
        (hx0+20, hy0+62), (hx0, hy0+34)]
d.polygon(hull, fill=(30, 30, 34))
d.rectangle([hx0+6, hy0+6, hx0+396, hy0+14], fill=(70, 70, 76))
# deck structures
d.rectangle([hx0+60, hy0-52, hx0+130, hy0], fill=(200, 200, 204))
d.rectangle([hx0+150, hy0-38, hx0+210, hy0], fill=(200, 200, 204))
d.rectangle([hx0+250, hy0-64, hx0+286, hy0], fill=(200, 200, 204))  # funnel
d.rectangle([hx0+250, hy0-64, hx0+286, hy0-52], fill=RED)
# flames on deck
flame(d, hx0+95, hy0-52, 46, 78)
flame(d, hx0+180, hy0-38, 40, 66)
flame(d, hx0+330, hy0, 52, 88)
# smoke
for sx, sy, sr in [(hx0+95, IY+58, 26), (hx0+150, IY+34, 32), (hx0+215, IY+16, 36),
                   (hx0+330, IY+52, 28), (hx0+385, IY+28, 30)]:
    d.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(120, 124, 128))
# re-draw flame tops over smoke bottoms for depth
flame(d, hx0+95, hy0-52, 46, 78)
flame(d, hx0+180, hy0-38, 40, 66)
flame(d, hx0+330, hy0, 52, 88)
# lead text, right half
TX = LX+8+IW+20
d.text((TX, LY+14), "LEAD STORY", font=SANS_B(22), fill=RED)
headline = "TANKERS ABLAZE IN THE STRAIT OF HORMUZ"
for i, line in enumerate(wrap(headline, SERIF_B(38), 992-8-IW-20-16, d)):
    d.text((TX, LY+46+i*46), line, font=SERIF_B(38), fill=INK)
cap = ("Two tankers hit naval mines, exploded and caught fire, "
       "Iran's IRGC says.")
cy = LY+46+3*46+8
for i, line in enumerate(wrap(cap, SANS(22), 992-8-IW-20-16, d)):
    d.text((TX, cy+i*28), line, font=SANS(22), fill=(60, 60, 60))

# ---------- story panels ----------
def panel(x, y, w, h, pict, headline, caption, head_size=24, cap_size=18):
    d.rectangle([x, y, x+w, y+h], fill=CARD, outline=BORDER, width=2)
    pict(x+10, y+8, w-20, 70)
    lines = wrap(headline, SANS_B(head_size), w-24, d)
    ty = y+86
    for line in lines:
        d.text((x+12, ty), line, font=SANS_B(head_size), fill=INK)
        ty += head_size+6
    ty += 6
    for line in wrap(caption, SANS(cap_size), w-24, d):
        d.text((x+12, ty), line, font=SANS(cap_size), fill=(60, 60, 60))
        ty += cap_size+5

def pict_refinery(x, y, w, h):
    base = y+h-8
    d.rectangle([x+8, base-46, x+52, base], fill=(90, 96, 104))
    d.rectangle([x+60, base-34, x+118, base], fill=(120, 126, 134))
    d.ellipse([x+126, base-40, x+168, base], fill=(150, 156, 164))
    d.rectangle([x+176, base-34, x+192, base], fill=(90, 96, 104))
    flame(d, x+184, base-34, 24, 18)
    d.rectangle([x+200, base-30, x+w-8, base], fill=(70, 76, 84))

def pict_broken_building(x, y, w, h):
    base = y+h-8
    pts = [(x+30, base), (x+30, base-52), (x+52, base-44), (x+70, base-58),
           (x+92, base-46), (x+110, base-56), (x+128, base-48), (x+128, base)]
    d.polygon(pts, fill=(96, 96, 100))
    # windows
    for wx, wy in [(x+44, base-34), (x+66, base-30), (x+92, base-34), (x+108, base-26)]:
        d.rectangle([wx, wy, wx+12, wy+12], fill=GOLD)
    # crack
    d.line([(x+80, base-58), (x+74, base-30), (x+84, base-14)], fill=RED, width=3)
    # rubble
    for rx, ry, rs in [(x+150, base-6, 12), (x+172, base-4, 9), (x+190, base-6, 11)]:
        d.polygon([(rx, ry-rs), (rx+rs, ry), (rx-rs, ry)], fill=(140, 140, 136))

def pict_explosion(x, y, w, h):
    cx, cy = x+w//2-40, y+h//2
    pts = []
    for i in range(16):
        ang = math.pi*i/8
        r = 40 if i % 2 == 0 else 20
        pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
    d.polygon(pts, fill=FLAME2, outline=FLAME)
    d.ellipse([cx-13, cy-13, cx+13, cy+13], fill=FLAME)
    for sx, sy, sr in [(x+w-70, y+12, 5), (x+w-46, y+34, 4), (x+16, y+10, 4)]:
        d.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(120, 124, 128))

def pict_chart(x, y, w, h):
    ox, oy = x+16, y+h-14
    d.line([(ox, y+6), (ox, oy)], fill=INK, width=2)
    d.line([(ox, oy), (x+w-14, oy)], fill=INK, width=2)
    pts = [(ox+8, y+16), (ox+60, y+30), (ox+110, y+22), (ox+160, y+46),
           (ox+205, y+34), (ox+250, y+52)]
    d.line(pts, fill=RED, width=4)
    # up arrow at end
    d.line([(ox+250, y+52), (ox+268, y+30)], fill=(34, 139, 34), width=4)
    d.polygon([(ox+268, y+18), (ox+258, y+34), (ox+278, y+32)], fill=(34, 139, 34))

def pict_gavel(x, y, w, h):
    # gavel: head (short thick bar, steep angle) crossed by handle (shallow angle)
    cx, cy = x+w//2, y+h//2+4
    rot_rect(d, cx-8, cy-4, 58, 22, 70, (120, 84, 40))    # head
    rot_rect(d, cx+7, cy-10, 96, 11, -20, (150, 110, 60))  # handle
    d.rectangle([cx-50, cy+28, cx+50, cy+36], fill=(90, 64, 30))  # sound block
    d.rectangle([cx-50, cy+28, cx+50, cy+31], fill=(60, 42, 20))

PW, PH = 320, 218
PY = 422
panel(16, PY, PW, PH, pict_refinery,
      "HOUTHIS HIT SAUDI REFINERY",
      "Fires at Ras Tanura; a drone hits a Riyadh skyscraper, 11 injured.")
panel(352, PY, PW, PH, pict_broken_building,
      "HAMAS SECURITY CHIEF KILLED",
      "Israeli strike in Gaza kills Mohammad Abuelouf, his wife and two children.")
panel(688, PY, PW, PH, pict_explosion,
      "WAR HITS BOTH WAYS",
      "Odesa strike kills 2; Kyiv block ablaze; Ukraine drones torch two Rosneft refineries.")

PY2 = 650
panel(16, PY2, 488, PH, pict_chart,
      "ASIA TUMBLES, DOW TOPS 50,000",
      "KOSPI -6.16%, Nikkei -2.78%; Dow closes above 50,000 at 50,018.70, Nasdaq -1.5%.",
      head_size=26)
panel(520, PY2, 488, PH, pict_gavel,
      "HUAWEI CONVICTED IN BROOKLYN",
      "Guilty on 10 of 12 counts: bank and wire fraud, sanctions violations, trade-secret theft.",
      head_size=26)

# ---------- bottom strip ----------
SY = 878
d.rectangle([0, SY, W, 1008], fill=NAVY)
d.text((16, SY+8), "ALSO TODAY", font=SANS_B(22), fill=GOLD)
strip_lines = [
    "Sudan: RSF drone strikes kill 19 civilians  \u2022  COP31 climate talks fail to reach a deal",
    "Shenzhou-24 docks with China's Tiangong station",
    "Colombia: hostages freed in Cartagena supermarket storming",
]
for i, line in enumerate(strip_lines):
    d.text((16, SY+38+i*26), line, font=SANS(19), fill=(235, 235, 235))
center(d, W//2, 1010, "Drawn summary of the day's news \u2014 25 November 2026",
       SANS(13), GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
