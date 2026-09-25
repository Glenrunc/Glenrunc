#!/usr/bin/env python3
"""
Generate the SVG cards used by the profile README — no third-party services.

  python3 scripts/gen_cards.py [--user Glenrunc] [--out assets]

Produces, in both a dark and a light variant:
  assets/stats-*.svg     headline metrics + language distribution
  assets/heatmap-*.svg   the last twelve months of contributions

Data comes from the public GitHub REST API and the public contributions
calendar. A GITHUB_TOKEN in the environment is optional and only used to
raise the API rate limit.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import date, datetime

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
UA = "Mozilla/5.0 (compatible; profile-card-generator)"

THEMES = {
    "dark": dict(
        bg0="#080b14", bg1="#0d1222", bg2="#05070e", grid="#1b2440", rule="#18233e",
        line="#1c2742", chip="#0f1730", ink0="#a78bfa", ink1="#22d3ee",
        text="#e6edf3", sub="#8ea0c4", dim="#4d5f85", track="#151d33",
        heat=["#141c31", "#3b2f8f", "#5b4bd6", "#7c5cff", "#22d3ee"],
    ),
    "light": dict(
        bg0="#ffffff", bg1="#f5f7fd", bg2="#eef1fb", grid="#dbe1f2", rule="#e2e8f7",
        line="#d5ddf2", chip="#eaeffd", ink0="#6d28d9", ink1="#0891b2",
        text="#111827", sub="#3b4766", dim="#75839f", track="#e6ebf8",
        heat=["#e8ecf8", "#c9bcf7", "#a78bfa", "#7c5cff", "#0891b2"],
    ),
}

# linguist-ish colours for the languages that actually show up
LANG_COLORS = {
    "Python": "#3572A5", "C++": "#f34b7d", "C": "#555555", "Jupyter Notebook": "#DA5B0B",
    "TeX": "#3D6117", "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "PHP": "#4F5D95",
    "HTML": "#e34c26", "CSS": "#563d7c", "Java": "#b07219", "Shell": "#89e051",
    "CMake": "#DA3434", "Makefile": "#427819", "Dockerfile": "#384d54", "SCSS": "#c6538c",
    "Rust": "#dea584", "Go": "#00ADD8", "Ruby": "#701516", "Assembly": "#6E4C13",
    "Cuda": "#3A4E3A", "Batchfile": "#C1F12E", "Vue": "#41b883", "Svelte": "#ff3e00",
}
FALLBACK_COLORS = ["#7c5cff", "#22d3ee", "#ff4d8d", "#f59e0b", "#34d399", "#60a5fa"]


# ---------------------------------------------------------------- fetching

def _get(url: str, raw: bool = False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read().decode("utf-8", "replace")
    return data if raw else json.loads(data)


def fetch_profile(user: str) -> dict:
    return _get(f"https://api.github.com/users/{user}")


def fetch_repos(user: str) -> list:
    repos, page = [], 1
    while True:
        batch = _get(f"https://api.github.com/users/{user}/repos?per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def fetch_languages(repos: list) -> "OrderedDict[str, int]":
    """Byte counts across every non-fork repository, largest first."""
    totals: dict[str, int] = {}
    for r in repos:
        if r.get("fork"):
            continue
        try:
            for lang, n in _get(r["languages_url"]).items():
                totals[lang] = totals.get(lang, 0) + n
        except urllib.error.HTTPError as e:      # rate limit or an empty repo
            print(f"  ! languages for {r['name']}: {e}", file=sys.stderr)
    return OrderedDict(sorted(totals.items(), key=lambda kv: -kv[1]))


def fetch_calendar(user: str) -> list:
    """[(date, level, count)] for the last ~53 weeks, from the public calendar."""
    page = _get(f"https://github.com/users/{user}/contributions", raw=True)

    counts: dict[str, int] = {}
    for m in re.finditer(r'for="(contribution-day-component-[\d-]+)"[^>]*>([^<]*)<', page):
        cell_id, label = m.group(1), html.unescape(m.group(2))
        n = re.match(r"(\d[\d,]*)\s+contribution", label)
        counts[cell_id] = int(n.group(1).replace(",", "")) if n else 0

    days = []
    for m in re.finditer(r'<td[^>]*data-date="(\d{4}-\d{2}-\d{2})"[^>]*>', page):
        tag, day = m.group(0), m.group(1)
        level = int(re.search(r'data-level="(\d)"', tag).group(1))
        cell_id = re.search(r'id="([^"]+)"', tag).group(1)
        days.append((date.fromisoformat(day), level, counts.get(cell_id, 0)))
    days.sort(key=lambda d: d[0])
    return days


def streaks(days: list) -> tuple[int, int]:
    """(current, longest) streak of days with at least one contribution."""
    longest = run = 0
    today = date.today()
    for d, _lvl, n in days:
        if d > today:
            break
        run = run + 1 if n else 0
        longest = max(longest, run)
    current = 0
    for d, _lvl, n in reversed([x for x in days if x[0] <= today]):
        if n:
            current += 1
        elif current or d != today:      # today still counts as pending, not broken
            break
    return current, longest


# ---------------------------------------------------------------- drawing

def shell(w: int, h: int, t: dict, body: str, label: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"
     role="img" aria-label="{label}">
  <title>{label}</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/><stop offset="0.6" stop-color="{t['bg0']}"/>
      <stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
    <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['ink0']}"/><stop offset="1" stop-color="{t['ink1']}"/>
    </linearGradient>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1" fill="{t['grid']}" opacity="0.5"/>
    </pattern>
    <clipPath id="frame"><rect x="0.5" y="0.5" rx="16" width="{w-1}" height="{h-1}"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    <rect width="{w}" height="{h}" fill="url(#grid)"/>
{body}
    <rect x="0.5" y="0.5" rx="16" width="{w-1}" height="{h-1}" fill="none" stroke="{t['rule']}"/>
  </g>
</svg>
'''


def heading(x: int, y: int, text: str, t: dict) -> str:
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="12.5" letter-spacing="2.4" '
            f'fill="{t["dim"]}"><tspan fill="{t["ink1"]}">~</tspan> <tspan fill="{t["dim"]}">$</tspan> '
            f'<tspan fill="{t["sub"]}">{text}</tspan></text>')


def fmt(n: int) -> str:
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 10000 else f"{n:,}".replace(",", " ")


def card_stats(user: str, prof: dict, repos: list, langs: dict, days: list, t: dict) -> str:
    W, H = 1200, 250
    own = [r for r in repos if not r.get("fork")]
    stars = sum(r["stargazers_count"] for r in repos)
    year = sum(n for _d, _l, n in days)
    cur, best = streaks(days)

    metrics = [
        (fmt(len(own)), "repositories"),
        (fmt(stars), "stars earned"),
        (fmt(prof.get("followers", 0)), "followers"),
        (fmt(year), "contributions · 12 mo"),
        (fmt(best), "longest streak"),
        (fmt(cur), "current streak"),
    ]

    out = [heading(44, 44, f"stat --user {user}", t)]

    step = (W - 88) / len(metrics)
    for i, (value, label) in enumerate(metrics):
        x = 44 + step * i
        if i:
            out.append(f'<line x1="{x-18:.0f}" y1="60" x2="{x-18:.0f}" y2="126" stroke="{t["line"]}"/>')
        out.append(
            f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.7s" '
            f'begin="{0.15*i:.2f}s" fill="freeze"/>'
            f'<text x="{x:.0f}" y="102" font-family="{MONO}" font-size="40" font-weight="700" '
            f'fill="url(#ink)">{value}</text>'
            f'<text x="{x:.0f}" y="122" font-family="{MONO}" font-size="11" letter-spacing="0.8" '
            f'fill="{t["dim"]}">{label}</text></g>')

    # language distribution
    total = sum(langs.values()) or 1
    shown = list(langs.items())[:7]
    rest = total - sum(v for _k, v in shown)
    if rest > 0:
        shown.append(("other", rest))

    out.append(f'<line x1="44" y1="152" x2="{W-44}" y2="152" stroke="{t["line"]}"/>')
    out.append(f'<text x="44" y="180" font-family="{MONO}" font-size="11.5" letter-spacing="1.6" '
               f'fill="{t["dim"]}">LANGUAGE DISTRIBUTION</text>')

    bar_x, bar_y, bar_w, bar_h = 44, 192, W - 88, 12
    out.append(f'<rect x="{bar_x}" y="{bar_y}" rx="6" width="{bar_w}" height="{bar_h}" fill="{t["track"]}"/>')
    out.append(f'<clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" rx="6" width="{bar_w}" height="{bar_h}"/></clipPath>')

    x = bar_x
    segs, legend = [], []
    lx, fb = bar_x, 0
    for i, (lang, n) in enumerate(shown):
        frac = n / total
        w = bar_w * frac
        if lang == "other":
            color = t["dim"]
        else:
            color = LANG_COLORS.get(lang)
            if not color:
                color, fb = FALLBACK_COLORS[fb % len(FALLBACK_COLORS)], fb + 1
        segs.append(
            f'<rect x="{x:.1f}" y="{bar_y}" width="0" height="{bar_h}" fill="{color}">'
            f'<animate attributeName="width" values="0;{w:.1f}" dur="0.9s" begin="{0.5+0.09*i:.2f}s" '
            f'fill="freeze" calcMode="spline" keySplines="0.2 0 0 1"/></rect>')
        x += w

        label = f"{lang} {frac*100:.1f}%"
        segs_w = len(label) * 6.9 + 22
        legend.append(
            f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur="0.6s" '
            f'begin="{0.9+0.07*i:.2f}s" fill="freeze"/>'
            f'<circle cx="{lx+8:.0f}" cy="{bar_y+38}" r="4" fill="{color}"/>'
            f'<text x="{lx+19:.0f}" y="{bar_y+42}" font-family="{MONO}" font-size="11.5" '
            f'fill="{t["sub"]}">{html.escape(label)}</text></g>')
        lx += segs_w

    out.append(f'<g clip-path="url(#bar)">{"".join(segs)}</g>')
    out.append("".join(legend))

    return shell(W, H, t, "\n    ".join(out), f"{user} — GitHub statistics")


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def card_heatmap(user: str, days: list, t: dict) -> str:
    W, H = 1200, 260
    cell, gap = 16, 4
    ox, oy = 62, 84

    total = sum(n for _d, _l, n in days)
    by_week: list[list] = []
    week: list = []
    for d, lvl, n in days:
        if d.weekday() == 6 and week:        # GitHub weeks start on Sunday
            by_week.append(week)
            week = []
        week.append((d, lvl, n))
    if week:
        by_week.append(week)
    by_week = by_week[-53:]

    out = [heading(44, 44, f"contributions --last 12mo   # {fmt(total)} total", t)]

    # month labels
    seen = set()
    for wi, wk in enumerate(by_week):
        first = wk[0][0]
        if first.day <= 7 and first.month not in seen:
            seen.add(first.month)
            out.append(f'<text x="{ox + wi*(cell+gap)}" y="{oy-10}" font-family="{MONO}" '
                       f'font-size="10.5" fill="{t["dim"]}">{MONTHS[first.month-1]}</text>')

    for i, lbl in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="44" y="{oy + i*(cell+gap) + cell - 4}" text-anchor="end" '
                   f'font-family="{MONO}" font-size="10" fill="{t["dim"]}">{lbl}</text>')

    today = date.today()
    for wi, wk in enumerate(by_week):
        for (d, lvl, n) in wk:
            row = (d.weekday() + 1) % 7      # Sunday-first rows
            x = ox + wi * (cell + gap)
            y = oy + row * (cell + gap)
            future = d > today
            fill = t["heat"][lvl] if not future else "none"
            stroke = f' stroke="{t["line"]}" stroke-dasharray="2 2"' if future else ""
            delay = 0.25 + wi * 0.022 + row * 0.012
            out.append(
                f'<rect x="{x}" y="{y}" rx="4" width="{cell}" height="{cell}" fill="{fill}"'
                f'{stroke} opacity="0">'
                f'<animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay:.2f}s" fill="freeze"/>'
                + (f'<animate attributeName="rx" values="8;4" dur="0.5s" begin="{delay:.2f}s" fill="freeze"/>'
                   if lvl else "")
                + f'<title>{n} contribution{"" if n == 1 else "s"} on {d.isoformat()}</title></rect>')

    # legend
    lx = W - 44 - (len(t["heat"]) * (cell + gap)) - 92
    out.append(f'<text x="{lx-8}" y="{oy + 7*(cell+gap) + 18}" text-anchor="end" font-family="{MONO}" '
               f'font-size="10.5" fill="{t["dim"]}">less</text>')
    for i, c in enumerate(t["heat"]):
        out.append(f'<rect x="{lx + i*(cell+gap)}" y="{oy + 7*(cell+gap) + 6}" rx="4" '
                   f'width="{cell}" height="{cell}" fill="{c}"/>')
    out.append(f'<text x="{lx + len(t["heat"])*(cell+gap) + 8}" y="{oy + 7*(cell+gap) + 18}" '
               f'font-family="{MONO}" font-size="10.5" fill="{t["dim"]}">more</text>')

    stamp = datetime.now().strftime("%Y-%m-%d")
    out.append(f'<text x="44" y="{oy + 7*(cell+gap) + 18}" font-family="{MONO}" font-size="10.5" '
               f'fill="{t["dim"]}">updated {stamp}</text>')

    return shell(W, H, t, "\n    ".join(out), f"{user} — contribution calendar")


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="Glenrunc")
    ap.add_argument("--out", default="assets")
    args = ap.parse_args()

    print(f"· profile      {args.user}")
    prof = fetch_profile(args.user)
    repos = fetch_repos(args.user)
    print(f"· repositories {len(repos)}")
    langs = fetch_languages(repos)
    print(f"· languages    {', '.join(list(langs)[:6])}")
    days = fetch_calendar(args.user)
    print(f"· calendar     {len(days)} days, {sum(n for *_ , n in days)} contributions")

    os.makedirs(args.out, exist_ok=True)
    for name, t in THEMES.items():
        for kind, svg in (("stats", card_stats(args.user, prof, repos, langs, days, t)),
                          ("heatmap", card_heatmap(args.user, days, t))):
            path = os.path.join(args.out, f"{kind}-{name}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"  → {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
