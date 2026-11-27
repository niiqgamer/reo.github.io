#!/usr/bin/env python3
"""Copy the code-drawn hero (drawHero8 and the creator palettes) from index.html into hero-poses.html.
Run after any change to the main character's drawing:  python3 hero-poses-sync.py"""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent
src = (root / "index.html").read_text(encoding="utf-8").split("\n")

def find(pred, start=0):
    for i in range(start, len(src)):
        if pred(src[i]):
            return i
    raise SystemExit("hero-poses-sync: marker not found in index.html")

a = find(lambda l: l.startswith("const HERO_SUITS="))           # suit palettes, colour helpers, heroPose, drawHero8
b = find(lambda l: l == "}", find(lambda l: l.startswith("function drawHero8(")))
c = find(lambda l: l.startswith("const APP_HAIR="))             # creator palettes and styles
d = find(lambda l: l.startswith("const APP_DEF="))
e = find(lambda l: l.startswith("const appOpts="))
code = "\n".join(src[a:b + 1] + src[c:d + 1] + [src[e]])

page = root / "hero-poses.html"
html = page.read_text(encoding="utf-8")
new, n = re.subn(r"(/\* BEGIN HERO CODE[^\n]*\*/\n).*?(/\* END HERO CODE \*/)",
                 lambda m: m.group(1) + code + "\n" + m.group(2), html, flags=re.S)
if n != 1:
    raise SystemExit("hero-poses-sync: BEGIN/END markers not found in hero-poses.html")
page.write_text(new, encoding="utf-8")
print(f"hero-poses.html: copied {code.count(chr(10)) + 1} lines from index.html")
