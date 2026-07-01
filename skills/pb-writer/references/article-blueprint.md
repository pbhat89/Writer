# Article / Tutorial Blueprint

The default skeleton for a PB long-form technical piece, followed by an annotated worked
example. Adapt sections to the topic — not every article is hands-on, and primers/comparisons
skip the code steps.

## Skeleton

1. **Title + subtitle line.** Clear and specific, says exactly what the reader gets. PB pairs a
   title with a one-line descriptor.
   - *"Running Language models locally: A Framework and UI Comparison"*
   - *"Data Science Workflows with the Targets Package in R: End-to-End Example with Code"* —
     subtitle: *"Structured and reproducible approach for analysis"*
   - *"Explainable AI (XAI) — A guide to 7 Packages in Python to Explain Your Models"* —
     subtitle: *"An introduction to various frameworks and web apps to interpret and explain ML
     models in Python"*

2. **Hero image note.** `[Image: Unsplash hero — Photo by <name> on Unsplash]`. PB opens with an
   Unsplash photo, credited.

3. **Motivating intro (the why).** 1–3 short paragraphs on why this matters right now — the
   real-world tension, business stakes, or the itch that started the project. If it's a series,
   say so up front ("This is a two part article series. Part one covers…"). If it's a weekend/
   self-learning build, say that too — it sets honest expectations.

4. **Brief primer (optional but common).** "Brief technical primer" / "A while back" — define the
   2–4 terms the reader needs (with plain-language definitions and the key trade-off), so the deep
   dive doesn't lose anyone.

5. **Question-headed body sections.** Build up logically. Typical shapes:
   - *Landscape / comparison piece*: "How does the current landscape look?" → survey options →
     per-option subsection with features, a code snippet or screenshot, and honest remarks →
     "Remarks" summary.
   - *Hands-on build*: "Which framework?" (justify the choice, compare alternatives, note when
     NOT to use) → "Getting started" → numbered steps (1. Loading the libraries → 2. Setting up
     the API → 3. …) each with prose lead-in, real code, and an `[Image by Author: output]` note →
     "Testing some examples" → optional UI/front-end section.
   - *Primer / conceptual piece*: "What and why?" → "How does the current landscape look?" →
     "Food for thought" open questions → "What next?".

6. **Trade-offs & caveats — woven throughout, not quarantined.** Every tool/approach gets its
   honest downside, security note, or "I would not recommend this for X."

7. **"Food for thought" callout (for conceptual pieces).** `>`-labeled open debates that pose
   real unresolved questions rather than resolving them neatly.

8. **Learnings and future enhancement areas (or "Remarks").** Bullet the honest takeaways: what
   you'd do differently, what to add next (cache/memory, LangGraph, orchestration…), what's still
   immature in the field.

9. **References.** Numbered `1.` or bracketed `[1]` list of docs, GitHub issues, papers,
   Stack Overflow threads actually used. Real links only — never fabricate a citation.

10. **Optional companion note.** "The app UI code can be found here." — link the repo/notebook.

## Image conventions

- Hero: Unsplash, credited "Photo by <name> on Unsplash".
- Diagrams and screenshots he made: caption "Image by Author" / "Image source: By Author".
- Borrowed charts/figures: caption "Source: <url or org>".
- In drafts, insert placeholders: `[Image by Author: streamlit dark-theme landing page with
  example query and output]` so PB knows exactly what to drop in.

## Annotated worked example (opening of a hands-on build)

> **Building a small on-prem RAG service for sensitive documents: a hands-on guide**
> *A weekend build for keeping retrieval fully local — with the lessons that bit me*
>
> `[Image: Unsplash hero — Photo by <name> on Unsplash]`
>
> Most RAG tutorials assume you can ship your documents to a hosted embedding API and move on.
> In a lot of enterprise settings — anything touching PII, contracts, or data-residency rules —
> that assumption quietly kills the project before it starts. So the interesting question isn't
> "can I build RAG?", it's "can I build RAG that never lets a document leave the box?" This is a
> self-learning build to see how far a fully local stack gets you, and where it hurts.
>
> The remarks below are my personal take basis usage and ease of setup — no branding or
> promotion here, just what worked for me.
>
> **Brief technical primer**
> - *Embedding*: turning text into a vector so we can measure similarity. Local models (e.g.,
>   `bge-small`, `e5`) run this on CPU/modest GPU — smaller and faster, at some quality cost. The
>   classic trade-off again.
> - *Vector store*: where those vectors live and get searched. We'll use a local one so nothing
>   goes to the cloud.
>
> **Which stack?**
> A few reasonable options, and when each fits …

Notice: the *why* (data residency) comes first, the personal-opinion disclaimer is explicit, the
primer defines terms with the trade-off stated, and the section header is a question. That's the
pattern to reproduce.
