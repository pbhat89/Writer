# Code Conventions

How PB writes and presents code in articles. Code is a first-class part of his tutorials — it's
real, runnable, and commented like production-adjacent work, not a toy snippet.

## Presentation

- **Imports block first, as its own numbered step.** "1. Loading the libraries" — one code block
  with every import, grouped and lightly commented (`# load base packages`).
- **Numbered build steps.** Each subsequent step gets a short prose lead-in explaining *why*,
  then the code, then a one-line note on the output (often an `[Image by Author: …]` screenshot
  of the result).
- **Show outputs.** After code, describe or screenshot what it produced ("bar plot of class",
  "Logistic regression model build and show coefficients"). Readers see the payoff.
- **Link the full repo.** Long apps aren't pasted end-to-end; the key functions are shown and the
  full code is linked ("The app UI code can be found here.").

## Style within the code

- **Language**: Python primarily (also R for the `targets`/workflow material). Idiomatic, current.
- **Comments**: liberal inline `#` comments explaining intent and gotchas, not restating syntax.
  Examples from his work: `# from your .env`, `# Set to 0 for deterministic output`,
  `# required for OpenRouter`, `# final coding model for analysis`.
- **Docstrings**: functions get a docstring with `Args:` and `Returns:`. Example:
  ```python
  def create_chat_openai(model):
      """
      Create a ChatOpenAI instance with a specified model.

      Args:
          model (str): The model to use (e.g., "qwen/qwen3-coder").

      Returns:
          ChatOpenAI: A ChatOpenAI instance with the specified model.
      """
  ```
- **Type hints**: used on function signatures (`from typing import Any, Optional`, e.g.
  `def agent_at_work(model: Any, user_query: str, path: Any) -> dict:`).
- **Section banners** inside longer scripts to organize:
  ```python
  # ============================================================================
  # Main Function
  # ============================================================================
  ```
  and step markers like `# Step 5: Final validation and formatting & last attempts`.
- **Error handling with graceful defaults**: `try/except` around fragile calls,
  `logging.error(f"...: {e}")`, and always return a sensible default rather than crashing.
- **Structured return values**: dict responses with consistent keys — `status`
  ("success"/"error"), `message`, `data`, and a type/`result_type` field — so a frontend can
  consume them predictably.
- **Security & environment hygiene**: secrets via `.env` and `os.getenv(...)`, never hardcoded;
  explicit notes when something runs with full local access ("use with caution due to security
  risks"); prefer sandboxed execution for untrusted code.
- **Deterministic settings called out**: e.g. `temperature=0.0  # Set to 0 for deterministic
  output`, `max_retries=3`.

## Tooling PB reaches for (use when relevant, don't force)

- LLM access via OpenRouter (`ChatOpenAI` pointed at OpenRouter base URL), Hugging Face models,
  local runtimes (llama.cpp, Ollama, GPT4All), Qwen/Llama models.
- LangChain / `langchain-experimental` agents, output parsers (`OutputFixingParser`), and a note
  that you can build from scratch on a Python REPL for more control.
- Streamlit for quick UIs (often a dark theme), matplotlib/seaborn/Plotly for plots, pandas/numpy.
- SDV/Faker for synthetic data; SHAP/LIME/DALEX/ELI5/explainerdashboard for XAI; R `targets`/
  `drake` for reproducible pipelines.

## Rules

- Code must actually run and match the prose. Don't show an API that doesn't exist.
- Comment the *why*, not the obvious.
- Prefer a real dataset and real provider over abstract placeholders.
- If pasting a full app is too long, show the important functions and link the rest.
