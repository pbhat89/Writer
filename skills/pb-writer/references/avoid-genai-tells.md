# Avoiding Generic-GenAI Tells

The single biggest failure mode for this skill is producing text that is competent but
*obviously AI-written*. PB's whole value is that his writing sounds like a real practitioner.
This file lists the anti-patterns to actively strip out, and what to do instead.

## Banned / heavily-avoided phrases and constructions

- Throat-clearing openers: "In today's fast-paced world", "In the ever-evolving landscape of",
  "In the realm of", "As we navigate the world of". → Instead open on the concrete real-world
  tension or the itch that started the project.
- Hype adjectives: "revolutionary", "game-changer", "cutting-edge", "powerful", "seamless",
  "robust" (as filler), "unlock", "harness the power of", "supercharge", "next-level". → State
  what it does plainly; let the reader judge.
- Empty transitions stacked mechanically: "Moreover", "Furthermore", "Additionally", "In
  conclusion", at the head of every paragraph. → Use natural connectives, or none.
- Hedging filler: "It's important to note that", "It's worth mentioning", "Needless to say",
  "At the end of the day". → Just say the thing.
- Fake balance clichés: "However, it's not without its challenges", "But like any tool, it has
  its pros and cons". → Name the *specific* trade-off instead.
- The rule-of-three tic: relentless triplets ("fast, efficient, and scalable"). → Vary rhythm;
  use a triplet only when the three things are genuinely the point.
- Summary-of-a-summary closings: "In conclusion, we have explored…". → PB closes with concrete
  "Learnings and future enhancements" and honest open questions, not a restatement.
- Marketing-y calls to action: "Dive in and start today!", "The possibilities are endless!". →
  A genuine "what next" or an open question is fine; hype is not.

## Structural tells to avoid

- Every section the same length and shape. → Vary; some sections are a paragraph, some are a
  build with code, some are a single sharp callout.
- Bolding every other phrase and bulleting everything. → Headers and prose carry most of the
  load; lists are for genuinely enumerable things.
- Perfectly symmetric "Pros / Cons" tables for everything. → Weave trade-offs into the prose
  where they're relevant.
- No first-person, no opinion, no "I". → PB is explicitly present: his experience, his caveats,
  his personal take.
- Emoji as connective tissue, especially in LinkedIn posts.

## Content tells to avoid

- **Fabricated specifics.** Invented statistics, made-up benchmark numbers, non-existent
  citations, or APIs/parameters that don't exist. If PB doesn't have the number, the draft says
  so or leaves a marked placeholder. Never invent.
- **Generic certainty.** Presenting a contested or immature area as settled. PB flags open
  debates and immaturity.
- **Vagueness where a concrete example belongs.** Every abstract claim gets anchored to a real
  dataset, tool, provider, or repo.
- **Uniform politeness with no personality.** The dry wit, the "basis usage and experience", the
  "unless you're living under a rock" — these are what make it his.

## Positive checklist (what presence looks like)

- Opens on a real problem, not a definition.
- First-person opinions, clearly flagged as personal.
- At least one honest trade-off or "when NOT to use this".
- Real code / real dataset / real link.
- A closing that lists genuine learnings and open questions.
- Reads like it could only have been written by someone who actually built the thing.

When a draft is done, re-read it hunting specifically for the phrases above. If you find them,
cut or rewrite. This pass matters more than any other for authenticity.
