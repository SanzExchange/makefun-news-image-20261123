#!/usr/bin/env python3
"""THE DAY IN PRINT - NI23 G4 akun1 compose (local only, PIL allowed).
Ivory paper, navy ink, red accent. Monday 23 November 2026.
Lead: pool #7 COP31 ends without a deal in Antalya.
Trio: #7 COP31 + #1 Hormuz tankers burn + #2 IRGC claims Patriot radars.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont

FDIR = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
def F(name, size):
    return ImageFont.truetype(FDIR + name, size)
PB = "PlayfairDisplay-Black.ttf"; PLB = "PlayfairDisplay-Bold.ttf"
AR = "Archivo.ttf"; AB = "Archivo-Bold.ttf"

W = H = 1024
IVORY = (247, 241, 227); PAPER = (250, 246, 235)
NAVY = (20, 33, 61); INK = (24, 28, 38); RED = (178, 28, 28)
GOLD = (176, 132, 44); GREY = (96, 96, 92); LINE = (198, 188, 164)
WHITE = (255, 255, 255)

REGION_COL = {
    "EUROPE": (37, 99, 165), "MIDDLE EAST": (178, 28, 28),
    "NORTH AMERICA": (21, 128, 96), "SOUTH ASIA": (202, 110, 20),
    "ASIA-PACIFIC": (124, 58, 180), "SOUTHEAST ASIA": (13, 148, 136),
    "AFRICA": (161, 98, 7), "GLOBAL": (90, 90, 90),
}

# page-no, location, region, chip, category, title, fact, source, kind
CARDS = [
 (1, "ANTALYA, TURKIYE", "EUROPE", "OFFICIAL", "CLIMATE SUMMIT",
  "COP31 Ends Without a Deal",
  "Final draft from Turkiye omits 'fossil fuels'; COP31 talks in Antalya close without a pact.",
  "BBC / AP wire, 23 Nov", "globe"),
 (2, "STRAIT OF HORMUZ", "MIDDLE EAST", "REPORTED", "GULF WAR",
  "Tankers Burn in Hormuz Strait",
  "Tankers set ablaze as the Iran-US war widens into the Gulf; the IRGC warns of unrest.",
  "AP live, 23 Nov", "ship"),
 (3, "MANAMA, BAHRAIN", "MIDDLE EAST", "CLAIM", "AIR DEFENCE",
  "IRGC Claims Patriot Radars Hit",
  "Iran's IRGC claims it destroyed two Patriot radar systems at a US base in Bahrain.",
  "Pre-opening AP/AFP check, 23 Nov", "radar"),
 (4, "KYIV, UKRAINE", "EUROPE", "REPORTED", "WAR",
  "Kyiv Boy Pulled Alive",
  "Boy of 7 freed after hours under rubble from a Russian strike; 6 dead in Kyiv.",
  "BBC, 23 Nov", "rubble"),
 (5, "KYIV REGION, UKRAINE", "EUROPE", "ON RECORD", "WAR",
  "14 Missing, Zelenskiy Says",
  "Fourteen missing after a Russian drone hit a residential block in the Kyiv region.",
  "JagranJosh, 23 Nov", "building"),
 (6, "GULF OF FINLAND", "EUROPE", "ONGOING", "SHIPPING",
  "Russian Ship Still Burns",
  "A Russian cargo ship still burns off Finland after an attack in the Gulf of Finland.",
  "BBC / JagranJosh, 23 Nov", "ship"),
 (7, "WASHINGTON, USA", "NORTH AMERICA", "OFFICIAL", "POLITICS",
  "Democrats Take House 258-173",
  "Largest House majority since 1992, confirmed after the North Carolina result.",
  "BBC, 23 Nov", "ballot"),
 (8, "WELLINGTON, NEW ZEALAND", "SOUTH ASIA", "REPORTED", "CRICKET",
  "India Pile Up Record 720/9",
  "India declare on 720 for 9 at Wellington, their highest Test total in NZ.",
  "ObserverVoice, 23 Nov", "cricket"),
 (9, "GLOBAL MARKETS", "GLOBAL", "REPORTED", "MARKETS",
  "Gold Slides to $3,538",
  "Gold falls over $2,000 from its 2026 record high of $5,595 an ounce.",
  "ObserverVoice, 23 Nov", "coin"),
 (10, "THE HAGUE, NETHERLANDS", "SOUTHEAST ASIA", "OFFICIAL", "WORLD COURT",
  "ICJ: Myanmar Genocide Guilt",
  "World court: Myanmar guilty over the Rohingya campaign of 2017; 700,000+ fled.",
  "Guardian / NYT reports, 23 Nov", "gavel"),
 (11, "IOWA, USA", "NORTH AMERICA", "REPORTED", "PUBLIC SAFETY",
  "Army to Detonate Iowa Explosives",
  "US Army will detonate tons of unstable explosives in Iowa despite a court order.",
  "BBC, 23 Nov", "burst"),
 (12, "WASHINGTON, USA", "NORTH AMERICA", "ONGOING", "INVESTIGATION",
  "FBI Probes Database Hack",
  "The FBI investigates a suspected hack of its criminal justice database in Washington.",
  "AP wire, 23 Nov", "shield"),
]

ALSO = [
 "Houthi ballistic missile on western Saudi Arabia intercepted",
 "Swimmer crosses Hormuz to highlight harm to Iran wildlife",
 "UN states agree to keep negotiating lethal AI weapons",
 "US declassifies more UFO footage filmed over Middle East",
 "Albanese: COP31 failure marks a 'difficult geopolitical era'",
 "Russia-bound ship towed after attack in Gulf of Finland",
 "Suspected drone strike: blast on Russian ship at Benghazi",
 "UK-EU Brexit reset deal called a 'landmark' by Burnham",
 "Thousands march in Lisbon over the cost of living",
 "Myanmar junta calls ASEAN ruling 'unfair and unbalanced'",
 "Ex-rebels in Cameroon caught between hiding and broken vows",
 "Escaped lion spreads fear among residents in Turkiye",
 "Nepal PM Shah holds bilateral talks with PM Modi in Delhi",
 "India and Bulgaria discuss IMEC and the Black Sea",
 "Guru Nanak Jayanti marked: 'Sewa, Simran aur Sangat'",
 "Uttar Pradesh runs air-raid and blackout drills in 75 districts",
 "Indonesia update: 7 body bags found, 50 still missing",
 "Day 5 at Wellington: India chase a famous win, NZ 119/2",
 "India win ODI series in New Zealand 3-2; Phillips top player",
 "Anupama defends IBSF world women's snooker title",
 "Pilgrim bus tragedy in Kota, Rajasthan: 9 dead",
 "Tata Steel sells steel pipe unit to APL Apollo, Rs28,000 cr",
 "SpiceJet pilots seek urgent audit; IndiGo holds 65.9% share",
 "IFFI 2026 hosts a BRICS roundtable in Goa",
 "Modi opens AI centre at IIT Patna, Rs400 crore research",
 "India-EU free trade pact likely signed 16 Dec in Brussels",
 "Miley Cyrus marries Maxx Morando in California",
 "Alcaraz beats Zverev for his first ATP Finals title",
]

# ---- fleet-style data structures (same content as CARDS/ALSO, for margin audit) ----
grid = [
 (1, "EUROPE", "CLIMATE SUMMIT", "BBC / AP wire, 23 Nov", "COP31 Ends Without a Deal", "Final draft from Turkiye omits 'fossil fuels'; COP31 talks in Antalya close without a pact.", "globe"),
 (2, "MIDDLE EAST", "GULF WAR", "AP live, 23 Nov", "Tankers Burn in Hormuz Strait", "Tankers set ablaze as the Iran-US war widens into the Gulf; the IRGC warns of unrest.", "ship"),
 (3, "MIDDLE EAST", "AIR DEFENCE", "Pre-opening AP/AFP check, 23 Nov", "IRGC Claims Patriot Radars Hit", "Iran's IRGC claims it destroyed two Patriot radar systems at a US base in Bahrain.", "radar"),
 (4, "EUROPE", "WAR", "BBC, 23 Nov", "Kyiv Boy Pulled Alive", "Boy of 7 freed after hours under rubble from a Russian strike; 6 dead in Kyiv.", "rubble"),
 (5, "EUROPE", "WAR", "JagranJosh, 23 Nov", "14 Missing, Zelenskiy Says", "Fourteen missing after a Russian drone hit a residential block in the Kyiv region.", "building"),
 (6, "EUROPE", "SHIPPING", "BBC / JagranJosh, 23 Nov", "Russian Ship Still Burns", "A Russian cargo ship still burns off Finland after an attack in the Gulf of Finland.", "ship"),
 (7, "NORTH AMERICA", "POLITICS", "BBC, 23 Nov", "Democrats Take House 258-173", "Largest House majority since 1992, confirmed after the North Carolina result.", "ballot"),
 (8, "SOUTH ASIA", "CRICKET", "ObserverVoice, 23 Nov", "India Pile Up Record 720/9", "India declare on 720 for 9 at Wellington, their highest Test total in NZ.", "cricket"),
 (9, "GLOBAL", "MARKETS", "ObserverVoice, 23 Nov", "Gold Slides to $3,538", "Gold falls over $2,000 from its 2026 record high of $5,595 an ounce.", "coin"),
 (10, "SOUTHEAST ASIA", "WORLD COURT", "Guardian / NYT reports, 23 Nov", "ICJ: Myanmar Genocide Guilt", "World court: Myanmar guilty over the Rohingya campaign of 2017; 700,000+ fled.", "gavel"),
 (11, "NORTH AMERICA", "PUBLIC SAFETY", "BBC, 23 Nov", "Army to Detonate Iowa Explosives", "US Army will detonate tons of unstable explosives in Iowa despite a court order.", "burst"),
 (12, "NORTH AMERICA", "INVESTIGATION", "AP wire, 23 Nov", "FBI Probes Database Hack", "The FBI investigates a suspected hack of its criminal justice database in Washington.", "shield"),
]
NUMS = [
 ("258-173", "Democrats House majority"),
 ("720/9", "India Wellington record"),
 ("7 + 50", "Indonesia found missing"),
 ("14", "Kyiv missing"),
 ("6", "Kyiv dead"),
 ("$3,538", "gold ounce"),
]
TL = [
 ("00:02", "UN lethal-AI talks go on"),
 ("02:00", "Albanese on COP31 failure"),
 ("Morning", "Kyiv boy freed, 6 dead"),
 ("Midday", "COP31 closes, no fossil-fuel pact"),
 ("Evening", "House majority 258-173 confirmed"),
 ("Close", "Gold at $3,538 an ounce"),
]
BRIEFS_L = [
 "Houthi ballistic missile on western Saudi Arabia intercepted",
 "Swimmer crosses Hormuz to highlight harm to Iran wildlife",
 "UN states agree to keep negotiating lethal AI weapons",
 "US declassifies more UFO footage filmed over Middle East",
 "Albanese: COP31 failure marks a difficult geopolitical era",
 "Russia-bound ship towed after attack in Gulf of Finland",
 "Suspected drone strike: blast on Russian ship at Benghazi",
 "UK-EU Brexit reset deal called a landmark by Burnham",
 "Thousands march in Lisbon over the cost of living",
 "Myanmar junta calls ASEAN ruling unfair and unbalanced",
 "Ex-rebels in Cameroon caught between hiding and broken vows",
 "Escaped lion spreads fear among residents in Turkiye",
 "Nepal PM Shah holds bilateral talks with PM Modi in Delhi",
 "India and Bulgaria discuss IMEC and the Black Sea",
]
BRIEFS_R = [
 "Guru Nanak Jayanti marked: Sewa, Simran aur Sangat",
 "Uttar Pradesh runs air-raid and blackout drills in 75 districts",
 "Indonesia update: 7 body bags found, 50 still missing",
 "Day 5 at Wellington: India chase a famous win, NZ 119/2",
 "India win ODI series in New Zealand 3-2; Phillips top player",
 "Anupama defends IBSF world women's snooker title",
 "Pilgrim bus tragedy in Kota, Rajasthan: 9 dead",
 "Tata Steel sells steel pipe unit to APL Apollo, Rs28,000 crore",
 "SpiceJet pilots seek urgent audit; IndiGo holds 65.9% share",
 "IFFI 2026 hosts a BRICS roundtable in Goa",
 "Modi opens AI centre at IIT Patna, Rs400 crore research",
 "India-EU free trade pact likely signed 16 Dec in Brussels",
 "Miley Cyrus marries Maxx Morando in California",
 "Alcaraz beats Zverev for his first ATP Finals title",
]
dc = "Xi-Trump-Putin trilateral summit - 19 Nov 2026 · Russian missiles and drones fell in Poland - incident 20 Nov · Paolo Bulgari dies - reported 22 Nov · Kim Jong-un security not supremacy speech, Seoul - 22 Nov · Ukraine strike on Kerch Bridge - reported 22 Nov · South Korea education minister resigns - first reported 22 Nov · Indonesia candy-factory fire as an event - 22 Nov 15:05"
PINS = [(1, 0.50, 0.33), (2, 0.60, 0.40), (3, 0.59, 0.42), (4, 0.52, 0.30),
        (5, 0.52, 0.32), (6, 0.53, 0.24), (7, 0.10, 0.34), (8, 0.86, 0.74),
        (9, 0.50, 0.50), (10, 0.48, 0.27), (11, 0.13, 0.38), (12, 0.11, 0.36)]
MAP_LEGEND = "dotted_map: dots are land; numbered pins mark the card numbers"

DATECHECK = [
 ("D1", "Xi-Trump-Putin summit - 19 Nov"),
 ("D2", "Russia missiles in Poland - 20 Nov"),
 ("D5", "Paolo Bulgari dies - rep. 22 Nov"),
 ("D6", "Kim Jong-un speech, Seoul - 22 Nov"),
 ("D9", "Kerch Bridge strike - rep. 22 Nov"),
 ("D11", "S. Korea minister quits - 22 Nov"),
 ("D12", "Indonesia factory fire - 22 Nov"),
]

NUMBERS = [
 ("258-173", "House (7)"),
 ("720/9d", "India rec. (8)"),
 ("7 + 50", "found/missing"),
 ("14", "missing (5)"),
 ("6", "dead (4)"),
 ("$3,538", "gold (9)"),
]

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def illus(d, x, y, w, h, kind, col):
    d.rectangle([x, y, x + w, y + h], fill=(235, 228, 205))
    cx, cy = x + w // 2, y + h // 2
    if kind == "ship":
        d.polygon([(x+8, cy+6), (x+w-14, cy+6), (x+w-24, cy+13), (x+16, cy+13)], fill=NAVY)
        d.rectangle([cx-4, cy-8, cx+10, cy+5], fill=col)
        d.polygon([(cx+2, cy-20), (cx+9, cy-8), (cx-4, cy-8)], fill=RED)
        d.polygon([(cx+12, cy-16), (cx+17, cy-7), (cx+7, cy-7)], fill=(230, 126, 34))
    elif kind == "globe":
        d.ellipse([cx-15, cy-15, cx+15, cy+15], outline=NAVY, width=3)
        d.arc([cx-15, cy-15, cx+15, cy+15], 20, 200, fill=col, width=2)
        d.line([cx-15, cy, cx+15, cy], fill=col, width=2)
        d.polygon([(cx-8, cy-16), (cx+14, cy-2), (cx-2, cy+4)], fill=RED)
    elif kind == "radar":
        d.line([cx-14, cy+13, cx+14, cy+13], fill=NAVY, width=3)
        d.line([cx, cy+13, cx-8, cy-10], fill=NAVY, width=3)
        for r in (6, 11, 16):
            d.arc([cx-8-r, cy-10-r, cx-8+r, cy-10+r], 300, 60, fill=RED, width=2)
        d.ellipse([cx-11, cy-13, cx-5, cy-7], fill=RED)
    elif kind == "rubble":
        d.polygon([(x+10, cy+13), (cx, cy-12), (x+w-10, cy+13)], fill=(150, 138, 110))
        d.rectangle([cx-6, cy-2, cx+6, cy+13], fill=NAVY)
        d.ellipse([cx-4, cy-12, cx+4, cy-4], fill=(230, 180, 120))
    elif kind == "building":
        d.rectangle([cx-16, cy-14, cx+2, cy+13], fill=NAVY)
        d.rectangle([cx+4, cy-8, cx+18, cy+13], fill=col)
        for i in range(3):
            for j in range(2):
                d.rectangle([cx-13+j*8, cy-10+i*8, cx-9+j*8, cy-6+i*8], fill=(245, 220, 120))
        d.polygon([(cx+8, cy-18), (cx+13, cy-9), (cx+3, cy-9)], fill=RED)
    elif kind == "ballot":
        d.rectangle([cx-16, cy-10, cx+16, cy+13], outline=NAVY, width=3)
        d.line([cx-10, cy-2, cx-3, cy+6], fill=RED, width=3)
        d.line([cx-3, cy+6, cx+11, cy-7], fill=RED, width=3)
        d.rectangle([cx-6, cy-16, cx+6, cy-11], fill=col)
    elif kind == "cricket":
        d.line([cx-12, cy+12, cx+8, cy-12], fill=(160, 110, 40), width=5)
        d.ellipse([cx+6, cy-14, cx+16, cy-4], fill=RED)
        for i in range(3):
            d.line([cx-16+i*6, cy+4, cx-16+i*6, cy+13], fill=NAVY, width=2)
    elif kind == "coin":
        d.ellipse([cx-14, cy-14, cx+14, cy+14], fill=(232, 190, 70), outline=GOLD, width=2)
        d.text((cx, cy), "$", font=F(AB, 20), fill=NAVY, anchor="mm")
        d.polygon([(cx+16, cy-8), (cx+24, cy+2), (cx+16, cy+2)], fill=RED)
        d.line([cx+20, cy-8, cx+20, cy+2], fill=RED, width=3)
    elif kind == "gavel":
        d.line([cx-14, cy-10, cx+4, cy+8], fill=(140, 90, 30), width=5)
        d.rectangle([cx-18, cy-16, cx-4, cy-6], fill=NAVY)
        d.rectangle([cx-16, cy+11, cx+14, cy+15], fill=col)
    elif kind == "burst":
        for a in range(0, 360, 30):
            r1, r2 = 5, 16
            d.line([cx + r1*math.cos(math.radians(a)), cy + r1*math.sin(math.radians(a)),
                    cx + r2*math.cos(math.radians(a)), cy + r2*math.sin(math.radians(a))], fill=RED, width=3)
        d.ellipse([cx-5, cy-5, cx+5, cy+5], fill=(230, 126, 34))
    elif kind == "shield":
        d.polygon([(cx, cy-16), (cx+14, cy-11), (cx+14, cy+2), (cx, cy+16), (cx-14, cy+2), (cx-14, cy-11)], outline=NAVY, width=3, fill=(210, 224, 245))
        d.text((cx, cy), "?", font=F(AB, 18), fill=RED, anchor="mm")
    else:
        d.ellipse([cx-12, cy-12, cx+12, cy+12], fill=col)

def card(d, x, y, w, h, c, big=False):
    no, loc, reg, chip, cat, title, fact, src, kind = c
    col = REGION_COL[reg]
    d.rectangle([x, y, x+w, y+h], fill=WHITE, outline=LINE, width=1)
    d.rectangle([x, y, x+w, y+17], fill=col)
    d.text((x+6, y+3), f"{no}. {loc}", font=F(AB, 11), fill=WHITE)
    tw = d.textlength(chip, font=F(AB, 10))
    d.rectangle([x+w-tw-12, y+2, x+w-3, y+15], fill=IVORY)
    d.text((x+w-tw-8, y+3), chip, font=F(AB, 10), fill=NAVY)
    ih = 30 if big else 22
    illus(d, x+5, y+21, w-10, ih, kind, col)
    d.text((x+6, y+24+ih), f"{reg} - {cat}", font=F(AB, 10), fill=col)
    tf = F(AB, 28 if big else 24)
    lines = wrap(d, title, tf, w-12)[:2]
    ty = y + 40 + ih
    for ln in lines:
        d.text((x+6, ty), ln, font=tf, fill=INK); ty += 26 if big else 24
    ff = F(AR, 14 if not big else 15)
    for ln in wrap(d, fact, ff, w-12)[:2]:
        if ty + 15 > y + h - 13: break
        d.text((x+6, ty+1), ln, font=ff, fill=(52, 52, 48)); ty += 16
    d.text((x+6, y+h-14), src, font=F(AR, 11), fill=GREY)

def fb(n):
    return F(AB, n)

def fr(n):
    return F(AR, n)

def fsr(n):
    return F(AR, n)

def lead(d, x, y, w, h, c):
    _tf = fb(28); _df = fr(15)
    card(d, x, y, w, h, c, big=True)

def mini(d, x, y, w, h, c):
    _tf = fb(24); _df = fr(14)
    card(d, x, y, w, h, c, big=False)

def header(d, variant):
    d.rectangle([0, 0, W, H], fill=IVORY)
    rng = random.Random(23)
    for _ in range(2600):
        px, py = rng.randrange(W), rng.randrange(H)
        d.point((px, py), fill=(240, 233, 214))
    d.rectangle([0, 0, W, 22], fill=NAVY)
    d.text((10, 4), "THE DAY IN PRINT", font=F(AB, 13), fill=WHITE)
    k = "40 STORIES - 7 REGIONS - EVERY ONE FROM 23 NOVEMBER 2026"
    d.text((W-10, 4), k, font=F(AB, 13), fill=(245, 205, 120), anchor="ra")
    d.text((W//2, 26), "THE DAY IN PRINT", font=F(PLB, 22), fill=NAVY, anchor="ma")
    d.text((W//2, 48), "Monday 23 November 2026", font=F(PB, 68), fill=INK, anchor="ma")
    sub = "COP31 ends with no deal in Antalya  -  Tankers burn in the Strait of Hormuz  -  Democrats take the House 258-173"
    d.text((W//2, 130), sub, font=F(AB, 14), fill=RED, anchor="ma")
    d.line([8, 148, W-8, 148], fill=NAVY, width=2)
    # region strip
    regs = [("EUROPE", 9), ("MIDDLE EAST", 5), ("NORTH AMERICA", 9), ("SOUTH ASIA", 12),
            ("ASIA-PACIFIC", 1), ("SOUTHEAST ASIA", 3), ("AFRICA", 1)]
    x = 10; y = 154
    d.text((x, y), "REGIONS:", font=F(AB, 12), fill=NAVY); x += 74
    for name, n in regs:
        col = REGION_COL[name]
        label = f"{name} {n}"
        tw = d.textlength(label, font=F(AB, 12))
        d.rectangle([x, y, x+tw+12, y+16], fill=col)
        d.text((x+6, y+2), label, font=F(AB, 12), fill=WHITE)
        x += tw + 18
    # timeline
    y = 174
    d.rectangle([8, y, W-8, y+18], fill=(233, 226, 205))
    tl = "UTC  00:02 UN lethal-AI talks go on  |  02:00 Albanese on COP31 failure  |  Morning: Kyiv boy freed, 6 dead  |  COP31 closes, no fossil-fuel pact  |  House majority 258-173 confirmed  |  Gold at $3,538"
    d.text((12, y+3), tl, font=F(AB, 12), fill=NAVY)
    return 198

def numbers_box(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=NAVY)
    d.text((x+10, y+4), "THE DAY IN NUMBERS", font=F(AB, 13), fill=(245, 205, 120))
    cols = 6; cw = (w-16)//cols
    for i, (num, lab) in enumerate(NUMBERS):
        cx = x + 8 + i * cw; cy = y + 19
        nf = F(PB, 24)
        while d.textlength(num, font=nf) > cw - 4 and nf.size > 15:
            nf = F(PB, nf.size - 2)
        d.text((cx, cy), num, font=nf, fill=WHITE)
        d.text((cx, cy+27), lab, font=F(AR, 10), fill=(214, 220, 235))

def world_map(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=(238, 232, 212), outline=LINE)
    d.text((x+8, y+5), "WHERE IT HAPPENED - pins = card numbers", font=F(AB, 11), fill=NAVY)
    # dotted continents: rough polygons as dot fields
    polys = [
        [(0.04,0.30),(0.22,0.22),(0.26,0.38),(0.18,0.55),(0.10,0.52)],   # N America
        [(0.20,0.58),(0.28,0.55),(0.30,0.78),(0.23,0.88),(0.19,0.70)],   # S America
        [(0.44,0.28),(0.55,0.24),(0.57,0.38),(0.49,0.42),(0.44,0.36)],   # Europe
        [(0.46,0.44),(0.58,0.42),(0.60,0.66),(0.52,0.80),(0.47,0.62)],   # Africa
        [(0.57,0.30),(0.74,0.26),(0.80,0.42),(0.68,0.50),(0.58,0.42)],   # Asia
        [(0.76,0.62),(0.88,0.60),(0.90,0.76),(0.79,0.78)],               # Oceania
    ]
    def inside(px, py, poly):
        c = False; j = len(poly)-1
        for i in range(len(poly)):
            xi, yi = poly[i]; xj, yj = poly[j]
            if ((yi > py) != (yj > py)) and (px < (xj-xi)*(py-yi)/(yj-yi)+xi): c = not c
            j = i
        return c
    gx, gy, gw, gh = x+6, y+19, w-12, h-34
    for yy in range(0, gh, 7):
        for xx in range(0, gw, 7):
            if any(inside(xx/gw, yy/gh, p) for p in polys):
                d.ellipse([gx+xx, gy+yy, gx+xx+3, gy+yy+3], fill=(150, 142, 118))
    pins = [(1,0.50,0.33),(2,0.60,0.40),(3,0.59,0.42),(4,0.52,0.30),(5,0.52,0.32),
            (6,0.53,0.24),(7,0.10,0.34),(8,0.86,0.74),(9,0.50,0.50),(10,0.48,0.27),
            (11,0.13,0.38),(12,0.11,0.36)]
    for no, fx, fy in pins:
        px, py = gx+fx*gw, gy+fy*gh
        d.ellipse([px-8, py-8, px+8, py+8], fill=RED)
        d.text((px, py), str(no), font=F(AB, 10), fill=WHITE, anchor="mm")
    d.text((x+8, y+h-13), "EUROPE  MIDDLE EAST  N. AMERICA  S. ASIA  SE ASIA  AFRICA  GLOBAL", font=F(AB, 10), fill=GREY)

ALSO_SHORT = [
 "Houthi missile stopped", "Swimmer crosses Hormuz",
 "UN lethal-AI talks go on", "US UFO footage released",
 "Albanese: COP31 failure", "Ship towed off Finland",
 "Suspected drone blast", "UK-EU reset a landmark",
 "Lisbon living-cost march", "Myanmar junta protests",
 "Cameroon ex-rebels stuck", "Escaped lion scares town",
 "Nepal PM meets Modi", "India-Bulgaria talks",
 "Guru Nanak Jayanti day", "UP drills: 75 districts",
 "Indonesia toll update", "Day 5: NZ 119/2 chase",
 "India win ODI series 3-2", "Anupama defends snooker",
 "Kota bus tragedy: 9 dead", "Tata Steel sale Rs28k cr",
 "IndiGo 65.9% home share", "IFFI Goa: BRICS table",
 "IIT Patna AI centre opens", "India-EU pact set 16 Dec",
 "Miley Cyrus marries", "Alcaraz wins ATP Finals",
]

dotted_map = world_map

def also_box(d, x, y, w, h):
    d.text((x, y), "ALSO ON MONDAY - STORIES 13-40", font=F(AB, 14), fill=NAVY)
    cols = 6; cw = w//cols
    per = (len(ALSO_SHORT)+cols-1)//cols
    for i, t in enumerate(ALSO_SHORT):
        cx = x + (i//per)*cw; cy = y + 18 + (i % per) * 12
        s = f"{13+i}. {t}"
        fnt = fsr(12)
        while d.textlength(s, font=fnt) > cw - 6 and len(s) > 10:
            s = s[:-2]
        d.text((cx, cy), s, font=fnt, fill=INK)

def datecheck(d, x, y, w, h):
    d.rectangle([x, y, x+w, y+h], fill=(252, 238, 238), outline=RED, width=2)
    d.text((x+8, y+4), "DATE CHECK - NOT 23 NOVEMBER NEWS (checked and left out):", font=F(AB, 13), fill=RED)
    cols = 4; cw = w//cols
    for i, (code, t) in enumerate(DATECHECK):
        cx = x + 8 + (i % cols) * (cw - 4); cy = y + 23 + (i // cols) * 12
        s = f"{code} {t}"
        fnt = F(AR, 12)
        while d.textlength(s, font=fnt) > cw - 12 and len(s) > 10:
            s = s[:-2]
        d.text((cx, cy), s, font=fnt, fill=(120, 30, 30))

def footer(d, y):
    d.line([8, y, W-8, y], fill=NAVY, width=2)
    d.text((10, y+4), "HOW SURE: REPORTED = reported by the cited wire.  CLAIM = one side's account, labelled as such.  ONGOING = still developing.  OFFICIAL / ON RECORD = stated by an authority.", font=F(AR, 11), fill=INK)
    d.text((10, y+17), "Every story happened, or was first reported, on Monday 23 November 2026. Contested claims are attributed.", font=F(AB, 12), fill=NAVY)
    d.text((10, y+29), "Original drawings.", font=F(AR, 11), fill=GREY)
    d.text((W-10, y+29), "THE DAY IN PRINT - one day, one page", font=F(AR, 11), fill=GREY, anchor="ra")

def render(variant, out):
    img = Image.new("RGB", (W, H), IVORY)
    d = ImageDraw.Draw(img)
    top = header(d, variant)
    if variant == "A":
        # trio lead row
        cw3 = (W - 32) // 3
        for i in range(3):
            lead(d, 8 + i*(cw3+8), top, cw3, 168, CARDS[i])
        y2 = top + 174
        for r in range(3):
            for i in range(3):
                mini(d, 8 + i*(cw3+8), y2 + r*136, cw3, 132, CARDS[3 + r*3 + i])
        y3 = y2 + 3*136 + 4
        numbers_box(d, 8, y3, 600, 60)
        world_map(d, 616, y3, W-624, 60)
        y4 = y3 + 66
        also_box(d, 8, y4, W-16, 88)
        y5 = y4 + 86
        datecheck(d, 8, y5, W-16, 48)
        footer(d, y5 + 50)
    else:
        # B: two big leads left, numbers+map rail right, grid below
        lead(d, 8, top, 330, 168, CARDS[0])
        lead(d, 346, top, 330, 168, CARDS[1])
        numbers_box(d, 684, top, W-692, 60)
        world_map(d, 684, top+64, W-692, 60)
        y2 = top + 174
        cw3 = (W - 32) // 3
        rest = [CARDS[2]] + CARDS[3:]
        for r in range(3):
            for i in range(3):
                idx = r*3 + i
                if idx < 9:
                    mini(d, 8 + i*(cw3+8), y2 + r*136, cw3, 132, rest[idx])
        y3 = y2 + 3*136 + 4
        card(d, 8, y3, cw3, 110, rest[9])
        also_box(d, 8 + cw3 + 12, y3, W - cw3 - 28, 88)
        y4 = y3 + 116
        datecheck(d, 8, y4, W-16, 48)
        footer(d, y4 + 50)
    img.save(out, optimize=True)
    print(out)

if __name__ == "__main__":
    v = sys.argv[1] if len(sys.argv) > 1 else "A"
    render(v, sys.argv[2])
