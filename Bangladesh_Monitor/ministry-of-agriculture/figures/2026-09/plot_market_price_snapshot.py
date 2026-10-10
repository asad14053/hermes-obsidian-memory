#!/usr/bin/env python3
"""Plot DAM month-end Dhaka market price ranges for Aug/Sep 2026."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "market_price_snapshot.csv"
OUT_PATH = HERE / "market_price_snapshot.png"

with CSV_PATH.open(encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))

categories = [
    ("Domestic onion", "Wholesale"),
    ("Domestic onion", "Retail"),
    ("Potato", "Wholesale"),
    ("Potato", "Retail"),
]
periods = ["2026-08-31", "2026-09-30"]
colors = {"2026-08-31": "#6B7280", "2026-09-30": "#C2410C"}
offsets = {"2026-08-31": -0.13, "2026-09-30": 0.13}
labels = {"2026-08-31": "31 Aug 2026", "2026-09-30": "30 Sep 2026"}

lookup = {(r["category"], r["market_level"], r["period"]): r for r in rows}
fig, ax = plt.subplots(figsize=(12, 7.5))
for i, (category, level) in enumerate(categories):
    for period in periods:
        r = lookup[(category, level, period)]
        low = float(r["low_tk_per_kg"])
        high = float(r["high_tk_per_kg"])
        y = i + offsets[period]
        ax.plot([low, high], [y, y], lw=7, color=colors[period], solid_capstyle="round",
                label=labels[period] if i == 0 else None)
        ax.scatter([low, high], [y, y], s=38, color=colors[period], zorder=3)
        ax.text(high + 0.7, y, f"{low:g}–{high:g}", va="center", fontsize=9, color=colors[period])

ax.set_yticks(range(len(categories)))
ax.set_yticklabels([f"{c}\n{m}" for c, m in categories])
ax.invert_yaxis()
ax.set_xlabel("Quoted price range (Tk per kg)")
ax.set_title("Dhaka onion and potato market-price ranges\nMonth-end snapshots: 31 August vs 30 September 2026", loc="left", weight="bold")
ax.grid(axis="x", alpha=0.25)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.legend(frameon=False, loc="lower right")
fig.text(0.01, 0.015,
         "Source: Bangladesh Department of Agricultural Marketing daily price sheets. "
         "Ranges are not weighted averages. Data extracted 6 Oct 2026.", fontsize=8.5)
plt.tight_layout(rect=(0, 0.055, 1, 1))
fig.savefig(OUT_PATH, dpi=180, bbox_inches="tight")
print(OUT_PATH)
