# PB_Writer

A Cowork / Claude Code **plugin** that drafts technical content in Prateek Bhatnagar's own
writing voice — practitioner-led, hands-on, honest about trade-offs, and deliberately free of
generic GenAI filler.

It is built from a study of PB's published Medium articles (synthetic data, Explainable AI,
running LLMs locally, R `targets` workflows, LangChain conversational analytics) plus the voice
of his CV and cover letter. The skill is scoped to **technical** writing only — data science,
machine learning, generative & agentic AI, MLOps, responsible AI, and technology. It is **not**
a philosophical or creative writer.

## What it does

- Drafts **long-form technical articles / tutorials** with PB's structure: motivate-the-why
  intro, question-headed sections, a brief primer, real runnable code in numbered steps, honest
  trade-offs throughout, and a "Learnings + References" close.
- Drafts **short LinkedIn posts** for visibility — one idea, first-person, concrete, no hype,
  no emoji spam.
- **Lift-and-shift output**: every article is delivered as a clean Markdown file that pastes
  straight into Medium or Substack — never asks what format to use.
- **Handles images end-to-end**: sources real open-license hero/thematic photos (Unsplash etc.)
  with correct attribution, AND generates original diagrams/workflows/plots ("Image by Author")
  via Mermaid, Graphviz, or matplotlib — placed inline in `assets/` with captions.
- Actively strips the "sounds like AI" tells so the output reads like PB wrote it.

## Structure

```
Writer/
├── .claude-plugin/
│   └── plugin.json                     # plugin manifest (name: pb-writer)
├── skills/
│   └── pb-writer/
│       ├── SKILL.md                    # the skill: voice, rules, workflow
│       └── references/
│           ├── voice-and-style.md      # detailed tone / rhythm / vocabulary
│           ├── article-blueprint.md    # article skeleton + annotated example
│           ├── linkedin-posts.md       # post formats, templates, examples
│           ├── code-conventions.md     # how PB writes & presents code
│           ├── images-and-visuals.md   # sourcing photos + generating diagrams/plots
│           └── avoid-genai-tells.md    # anti-patterns to strip out
├── corpus/                             # the 5 source articles + manifest
├── analysis/                           # style fingerprint + concept knowledge graph
│   ├── PB_Writer_Style_Analysis.html   # open in a browser
│   └── analysis_data.json              # raw computed metrics
└── README.md
```

## What the skill learned (analysis)

`analysis/PB_Writer_Style_Analysis.html` is a self-contained report computed from the corpus:
readability fingerprint (your technical writing sits at ~Flesch 40 / graduate grade, vs. a much
lighter Flesch ~75 for your personal essay — which is why the skill is technical-only), your
signature phrases ("basis", trade-off framing, opinion disclaimers, "etc."), your working
vocabulary, and a concept knowledge graph showing the five pillars you write across
(Generative & Agentic AI, Local/Small LLMs, Explainable AI, Responsible Data & Privacy,
Engineering Craft). Open it in any browser.

## Install

Two ways to use it:

1. **Install the packaged plugin** — take the `pb-writer.plugin` file and install it from the
   Cowork desktop app under **Settings → Capabilities** (or via the plugin install flow in
   Claude Code). Once installed, the skill triggers automatically on writing requests, or you can
   invoke it directly (`/pb-writer`).
2. **Point at this repo** — keep the folder as a plugin source in your Claude Code/Cowork plugin
   configuration.

> Note on naming: the internal skill/plugin id is `pb-writer` (kebab-case is required by the
> plugin format). It is the "PB_Writer" skill you asked for — same thing, valid id.

## How to use

Just ask, e.g.:

- "Write a LinkedIn post about the on-prem RAG thing I built this weekend."
- "Draft a hands-on article on fine-tuning a small model, in my style."
- "Turn these notes into a Medium tutorial with code."
- "Outline a comparison article on three vector databases."

The skill will confirm scope (type, length, angle, whether it's hands-on, any repo/dataset),
then draft in PB's voice.

## Maintaining the voice

As PB publishes more, add representative pieces to a `corpus/` folder and refresh the reference
files — especially `voice-and-style.md` and `avoid-genai-tells.md`. The more grounded the
references stay in real published work, the more faithful the output.

## License

MIT
