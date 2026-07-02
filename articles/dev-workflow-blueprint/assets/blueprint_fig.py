"""
Blueprint diagram (redraw): a high-resolution, LinkedIn-ready portrait of the
8-stage flow, with the feedback loop that makes it a loop and not a line.
Replaces the low-res wide Mermaid render. Matches the palette of demo_vs_real.py.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"

stages = [
    ("1", "Ideate & scope",   "gstack: /office-hours"),
    ("2", "Spec (the WHAT)",  "spec-kit: /specify → spec.md"),
    ("3", "Plan (the HOW)",   "spec-kit: /plan, reviewed by gstack"),
    ("4", "Break into tasks", "spec-kit: /tasks → tasks.md"),
    ("5", "Build",            "spec-kit: /implement + superpowers: test-first"),
    ("6", "Review & secure",  "gstack: /review, /cso, /codex"),
    ("7", "Test & verify",    "gstack: /qa + a verification log"),
    ("8", "Ship & watch",     "gstack: /ship → /land-and-deploy → /canary"),
]
colors = ["#1f4e79", "#245a80", "#2a6f86", "#2f8481",
          "#369b74", "#54a15f", "#7aa64d", "#9aa544"]

fig, ax = plt.subplots(figsize=(10, 12.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 13)
ax.axis("off")

# ---- title
ax.text(0.55, 12.5, "The blueprint", ha="left", va="center",
        fontsize=27, fontweight="bold", color="#12202f")
ax.text(0.6, 11.95, "idea to shipped, in eight stages",
        ha="left", va="center", fontsize=14.5, style="italic", color="#5a6472")

# ---- geometry
box_x, box_w, box_h = 1.55, 6.65, 1.10
n = len(stages)
top = 10.95
step = 1.365
ys = [top - i * step for i in range(n)]

# spine behind the number circles
ax.plot([1.0, 1.0], [ys[-1] - 0.1, ys[0] + 0.1], color="#c7d0db",
        lw=2.4, zorder=0, solid_capstyle="round")

for (num, title, tool), col, y in zip(stages, colors, ys):
    # connector arrow to next box
    box = FancyBboxPatch((box_x, y - box_h / 2), box_w, box_h,
                         boxstyle="round,pad=0.02,rounding_size=0.14",
                         linewidth=0, facecolor=col, zorder=2)
    ax.add_patch(box)
    # number circle on the spine
    ax.add_patch(Circle((1.0, y), 0.36, facecolor="white",
                        edgecolor=col, linewidth=3, zorder=3))
    ax.text(1.0, y, num, ha="center", va="center", fontsize=15,
            fontweight="bold", color=col, zorder=4)
    # stage text
    ax.text(box_x + 0.4, y + 0.24, title, ha="left", va="center",
            fontsize=16.5, fontweight="bold", color="white", zorder=4)
    ax.text(box_x + 0.4, y - 0.30, tool, ha="left", va="center",
            fontsize=11, style="italic", color="#eef4f8", zorder=4)

# ---- downward flow chevrons between stages
for y in ys[:-1]:
    ax.annotate("", xy=(1.0, y - step + 0.36), xytext=(1.0, y - 0.36),
                arrowprops=dict(arrowstyle="-|>", color="#9aa5b1",
                                lw=2.0, shrinkA=0, shrinkB=0), zorder=1)

# ---- feedback loop: from Review/Test (6,7) back up to Build (5)
loop = FancyArrowPatch((box_x + box_w + 0.02, ys[6]),
                       (box_x + box_w + 0.02, ys[4]),
                       connectionstyle="arc3,rad=0.42",
                       arrowstyle="-|>", mutation_scale=22,
                       lw=2.6, color="#c0504d", zorder=5)
ax.add_patch(loop)
ax.text(9.35, (ys[4] + ys[6]) / 2, "bug or fail:\nfix that\nslice, loop\nback",
        ha="center", va="center", fontsize=11.5, color="#c0504d",
        fontweight="bold", linespacing=1.35, clip_on=False)

# ---- footer line
ax.text(0.6, ys[-1] - 0.95,
        "Skip the stages your work hasn't earned. Everything else, an agent will skip for you.",
        ha="left", va="center", fontsize=11.5, style="italic", color="#5a6472")

plt.tight_layout()
plt.savefig("assets/blueprint.png", dpi=180, bbox_inches="tight", facecolor="white")
print("saved assets/blueprint.png")
