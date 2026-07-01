# LinkedIn Posts

PB uses LinkedIn to share learnings and increase visibility — not to broadcast hype. A post
should read like him thinking out loud after shipping or reading something, and should invite a
peer conversation. Same voice as the articles, just compressed.

## Principles

- **One idea per post.** A single learning, comparison, or observation. Don't cram.
- **First person, practitioner framing.** "Spent the weekend building…", "A thing that bit me
  this week…", "I keep seeing teams…". Share, don't lecture.
- **Concrete detail earns the post.** One real number, tool, trade-off, or failure mode makes it
  credible. Vague inspiration posts are exactly what to avoid.
- **Honest, non-promotional.** If it's an opinion, flag it. If a tool has a downside, name it.
- **End with a takeaway or a genuine question.** Invite discussion; don't beg for engagement.
- **Restraint on formatting.** Short lines and white space are fine (LinkedIn rewards them), but
  no emoji spam, no "🚀🔥", no "Agree? 👇", no 15-hashtag wall. 2–4 precise hashtags max.
- **Link when relevant.** To the companion Medium article, GitHub repo, or notebook.

## Anti-patterns (do NOT do these)

- "🚀 Excited to share…", "Thrilled to announce…", "Game-changer.", "This will blow your mind."
- Fake-vulnerable hook-bait ("I failed 100 times so you don't have to 🧵").
- Listicle hustle-culture tone, fabricated stats, or manufactured urgency.
- Bolding every line or turning it into a carousel-script of one-word lines.

## Templates

### 1. Shipped-a-project post
```
Spent the weekend building <thing> — <one-line what it does>.

The interesting part wasn't <the obvious bit>. It was <the real challenge / trade-off>.
<One concrete detail or number.>

<One honest learning — what you'd do differently or what's still open.>

Wrote up the full build + code here: <link>

#DataScience #<Topic> #<Tool>
```

### 2. Comparison / opinion post
```
<Two or three options> for <task>. Quick take from actually using them:

- <Option A>: <where it fits, one caveat>
- <Option B>: <where it fits, one caveat>

My rule of thumb: <the situational recommendation>. This is basis my usage — your mileage
will vary with <the factor that changes the answer>.

What are you reaching for these days?

#<Topic> #<Field>
```

### 3. Learning / observation post
```
<A crisp observation about the field or a term worth clarifying.>

<2–3 lines unpacking it, with one concrete example.>

<The open question or the "so what".>

#<Topic>
```

## Worked examples

**Shipped-a-project:**
> Spent the weekend wiring a pandas dataframe agent to an LLM so it answers data questions in
> plain English and writes the code itself.
>
> The fun part wasn't getting it to work once — it was getting it to fail gracefully. Left to
> itself, the model drifts, returns half-formatted output, or quietly hands back the wrong type.
> Most of my time went into an output parser and a "Thought → Action → Observation → Final
> Answer" contract, not the happy path.
>
> Lesson: for quick prototypes, start with a purpose-built agent; for control and security, build
> your own in a sandboxed REPL. Pick deliberately.
>
> Full write-up with code: <link>
>
> #DataScience #LLM #LangChain

**Comparison / opinion:**
> Running LLMs locally has gotten genuinely easy. Three I've actually used:
>
> - llama.cpp: fastest, most control, least hand-holding.
> - Ollama: nicest developer experience to just get a model running.
> - GPT4All: friendliest GUI + built-in RAG, plug in your own API keys too.
>
> Rule of thumb: match the tool to how much you want to tinker vs. just ship. This is basis my
> own testing — no promotion here.
>
> What's your local stack right now?
>
> #SmallLanguageModels #LocalLLM #GenAI

Note how both stay honest, concrete, and free of hype — that's the whole game.
