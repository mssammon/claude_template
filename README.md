# agent-template

Skeleton for a Python agent project (uv, Python 3.11, LangGraph, Pydantic v2, Streamlit, src layout).

```
src/app/
  schemas.py  contracts (Pydantic v2 models)
  agents/     agent definitions (LLM + prompt + tools)
  tools/      callable tools
  prompts/    prompt templates / system messages
  workflows/  LangGraph orchestration
  memory/     conversation state and memory stores
  llm/        model client setup
  config.py   settings from environment
tests/        unit/ and integration/
evals/        agent evaluation datasets and harness
scripts/      one-off utilities
data/         local data (gitignored)
notebooks/    exploration
docs/         design notes
```

## Usage

```
cp .env.example .env
uv sync
uv run agent-template
uv run pytest
```
