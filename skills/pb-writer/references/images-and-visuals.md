# Images & Visuals

PB's articles are visual by default. An article without images is not finished. This file is the
working procedure for the two image capabilities the skill must provide, plus placement and
attribution rules. Read it whenever drafting an article (skip for LinkedIn posts unless a visual
is explicitly wanted).

## The two capabilities

### 1. Source real open-license images (hero + thematic photos)

Used for the top-of-article hero and the occasional mood/thematic shot — exactly like PB's
"Photo by <name> on Unsplash" openers.

Workflow:

1. Pick a concept for the image that fits the article's theme (e.g. an abstract "network/nodes"
   shot for an agents piece, "server racks" for local-LLM, "locks/keys" for privacy).
2. Find a real, free-to-use image. Preferred sources and how to reference them:
   - **Unsplash** — free to use, no permission needed; attribution appreciated. Use the photo
     page URL and the photographer's name.
   - **Pexels**, **Wikimedia Commons** (check the specific license, prefer CC0 / CC BY), **Pixabay**.
3. **Download the file into `assets/`** (e.g. `assets/hero-agents.jpg`) so the article is
   self-contained and lift-and-shift ready, AND keep the source URL for the caption/credits.
   - Fetch via the available web/download tooling. If direct download isn't possible in the
     session, insert the direct image URL as the Markdown `src` and clearly note in the credits
     block that the file still needs to be pulled in — never leave a blank placeholder.
4. Caption it directly beneath the image: `*Photo by <Photographer> on Unsplash*`.

Attribution format Medium/PB uses:
```markdown
![Hero image](assets/hero-agents.jpg)
*Photo by Jane Doe on Unsplash*
```

Rules: only images you have the right to use (Unsplash/Pexels/Pixabay license, or CC). Never hot-
link a random Google result or a copyrighted press image. When in doubt, choose an Unsplash photo.

### 2. Create original diagrams and plots yourself ("Image by Author")

This is the differentiator. PB draws his own workflow diagrams, architecture sketches, and plots.
The skill should generate these as real image files, not describe them.

Pick the tool by figure type:

- **Process / workflow / pipeline diagrams, architecture, fl: use Mermaid**, then render to
  SVG/PNG so it drops into Medium (Medium/Substack don't render Mermaid natively — always export
  to an image). Example Mermaid for a pipeline:
  ```mermaid
  flowchart LR
    A[Raw data] --> B[Clean & prep]
    B --> C[Feature build]
    C --> D{Model}
    D -->|good| E[Serve / API]
    D -->|weak| B
  ```
  Render with the Mermaid CLI (`mmdc -i diagram.mmd -o assets/pipeline.png -b transparent`) or an
  equivalent renderer, save to `assets/`.
- **Boxes-and-arrows architecture where you want fine control: Graphviz** (`dot`) → PNG/SVG.
- **Data plots (bar, distribution, coefficients, comparisons): matplotlib / seaborn**, matching
  PB's habits (e.g. overlaid density plots with dotted mean lines, coefficient plots, class bar
  plots). Save to `assets/` at ~150 dpi, readable fonts, minimal chartjunk.
- **Conceptual comparison figures** (e.g. "SLM vs LLM trade-off", a 2x2): a clean matplotlib or
  SVG figure is fine.

Every generated figure gets the caption `*Image by Author*` (PB also uses "Image source: By
Author"). Keep a consistent, restrained visual style: clear labels, no rainbow palettes, enough
white space.

Generation checklist:
1. As you draft, mark each spot that needs a figure and decide type (diagram vs plot).
2. Generate the file into `assets/` with a descriptive name (`assets/rag-architecture.png`).
3. Reference it inline at that exact spot with an `*Image by Author*` caption.
4. If a plot needs data you don't have, generate representative sample data and label the figure
   as illustrative — never fabricate a real benchmark result and present it as measured.

## Placement conventions (where images go)

- **Hero**: immediately after the title/subtitle. Unsplash photo, credited.
- **Architecture / workflow diagram**: right where the system or process is first explained
  ("Image by Author").
- **Screenshots**: in hands-on builds, after the relevant step, showing the actual output
  (landing page, plot, model coefficients). If a real screenshot can't be produced in-session,
  generate a representative figure or leave a clearly-labelled `[Image by Author: <what to
  capture>]` note for PB to drop in.
- **Result plots**: in the "testing"/results section.
- Roughly one visual every 2–4 screens of text — enough to break up density, never decorative spam.

## Assets folder + credits block

- Store every image in an `assets/` folder beside the article `.md`.
- Reference with relative links so the folder is portable.
- At the top of the article file, include a short credits/metadata block listing each image, its
  caption, and (for sourced photos) the source URL and photographer — so publishing to Medium/
  Substack is a mechanical copy-paste-and-upload.

Example front-matter/credits block:
```markdown
<!--
Title: Building a small on-prem RAG service for sensitive documents
Subtitle: A weekend build for keeping retrieval fully local
Tags: RAG, LLM, Privacy, MLOps, Data Science
Images:
  - assets/hero-rag.jpg  — "Photo by Jane Doe on Unsplash" — https://unsplash.com/photos/xxxx
  - assets/rag-architecture.png — "Image by Author" (generated, Mermaid)
  - assets/latency-plot.png — "Image by Author" (matplotlib)
-->
```

## Fallbacks

- No image-download capability in the session → embed the direct source URL as `src` and flag in
  the credits block that the file needs pulling in. Still choose a specific, real image.
- No diagram renderer available → output the Mermaid/Graphviz source in a fenced block AND a
  `[Image by Author: render this]` note, so nothing is silently dropped.
- Never ship an article whose images are vague ("insert relevant image here"). Be specific about
  subject, source, and placement every time.
