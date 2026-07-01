"""
Author-made figure for the dev-workflow-blueprint article.

Visual analogy (inspired by the "full-stack in a demo vs in production" meme):
  - LEFT  : what building with an AI agent looks like in a DEMO  -> 2 layers
  - RIGHT : what it looks like when you SHIP IT FOR REAL         -> the 8-stage stack,
            each layer labelled with the stage + the actual skill/spec used.

Restrained sequential palette (no rainbow), matching PB's "clean, minimal chartjunk" style.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib import font_manager

plt.rcParams["font.family"] = "DejaVu Sans"

# ---------------------------------------------------------------- content
demo_layers = [
    ("Prompt the agent", ""),
    ("Working code\n“it runs on my machine”", ""),
]

real_layers = [
    ("1 · Ideate & scope",      "gstack: /office-hours"),
    ("2 · Spec (the WHAT)",     "spec-kit: /specify → spec.md"),
    ("3 · Plan (the HOW)",      "spec-kit: /plan, reviewed by gstack: /plan-eng-review"),
    ("4 · Break into tasks",    "spec-kit: /tasks → tasks.md"),
    ("5 · Build",               "spec-kit: /implement, sliced one PR at a time"),
    ("6 · Review & secure",     "gstack: /review, then /cso for security"),
    ("7 · Test & verify",       "gstack: /qa  +  a verification log"),
    ("8 · Ship & watch",        "gstack: /ship → /land-and-deploy → /canary"),
]

# muted sequential palette (deep blue -> teal -> green), intentional not rainbow
real_colors = [
    "#1f4e79", "#245a80", "#2a6f86", "#2f8481", "#369b74",
    "#54a15f", "#7aa64d", "#9aa544",
]
demo_colors = ["#1f4e79", "#2f8481"]

# ---------------------------------------------------------------- layout
fig, ax = plt.subplots(figsize=(11, 8.2))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.axis("off")

band_h = 1.55           # height of one production band
gap = 0.14
top_y = 16.6            # top of both towers aligned

def draw_tower(x0, width, layers, colors, y_top, band_height):
    n = len(layers)
    for i, ((title, sub), col) in enumerate(zip(layers, colors)):
        y = y_top - (i + 1) * (band_height + gap)
        box = FancyBboxPatch(
            (x0, y), width, band_height,
            boxstyle="round,pad=0.0,rounding_size=0.12",
            linewidth=0, facecolor=col, edgecolor="none",
        )
        ax.add_patch(box)
        cy = y + band_height / 2
        if sub:
            ax.text(x0 + 0.45, cy + 0.30, title, ha="left", va="center",
                    color="white", fontsize=12.5, fontweight="bold")
            ax.text(x0 + 0.45, cy - 0.34, sub, ha="left", va="center",
                    color="#eaf2f8", fontsize=9.6, style="italic")
        else:
            ax.text(x0 + width / 2, cy, title, ha="center", va="center",
                    color="white", fontsize=13.5, fontweight="bold",
                    linespacing=1.5)
    # bottom shadow line
    return

# left (demo) tower: tall single blocks so it reads as "just two things"
demo_band_h = (len(real_layers) * (band_h + gap) - gap) / 2 - gap / 2
draw_tower(1.0, 6.2, demo_layers, demo_colors, top_y, demo_band_h)

# right (real) tower
draw_tower(9.4, 9.6, real_layers, real_colors, top_y, band_h)

# ---------------------------------------------------------------- titles
ax.text(1.0 + 6.2 / 2, top_y + 0.9, "In a demo", ha="center", va="bottom",
        fontsize=16, fontweight="bold", color="#1a202c")
ax.text(1.0 + 6.2 / 2, top_y + 0.35, "prompt → code", ha="center", va="bottom",
        fontsize=11, color="#5a6472", style="italic")

ax.text(9.4 + 9.6 / 2, top_y + 0.9, "When you ship it for real", ha="center", va="bottom",
        fontsize=16, fontweight="bold", color="#1a202c")
ax.text(9.4 + 9.6 / 2, top_y + 0.35, "the same build, minus the wishful thinking",
        ha="center", va="bottom", fontsize=11, color="#5a6472", style="italic")

plt.tight_layout()
plt.savefig("assets/demo-vs-real.png", dpi=150, bbox_inches="tight",
            facecolor="white")
print("saved assets/demo-vs-real.png")
