# CLAUDE.md

## Project

@docs/project.md

This repo lives under `~/projects`, so the workspace-level `~/projects/CLAUDE.md` applies.

## Conventions
- Stack: Python 3.11, uv, LangGraph, Pydantic v2, pytest, Streamlit.
- First action in a new worktree: `uv sync`.
- Contracts live in `src/app/schemas.py`. Never modify them unless explicitly told to.
- Only edit the module(s) named in your brief. If you need a change elsewhere, stop and report it.
- Every LLM output is parsed into a Pydantic model. On validation failure: retry once, then raise. Never silently default.
- Calculations and rules are plain Python, never an LLM call.
- Run `uv run pytest` before reporting done.
- Finish with: files changed, test status, assumptions made.
- `.env` is **not** loaded automatically. `config.Settings` reads `os.environ` once, when the module is imported, so export the variables first or add a loader such as `python-dotenv` before relying on `.env`.
- When you add a new setting, put it in both `config.Settings` and `.env.example`.
- Keep prompts in `prompts/` and tools in `tools/` rather than inline in agent modules, so agents stay thin wiring.
- The build backend is `uv_build`, which is pointed at the package by `[tool.uv.build-backend] module-name = "app"` in `pyproject.toml`. Don't rename or move `src/app/` without updating it.
- Tests that call a real LLM or network go in `tests/integration/`. Keep `tests/unit/` offline and fast.
- Always confirm the branch name when committing to git or pushing to a remote repo.
- Integrate branches by rebasing, never by merge commits: `git rebase main` on the feature branch, then `git switch main && git merge --ff-only <branch>`. Use `git pull --rebase` when updating from the remote. Don't rebase commits that are already pushed to a shared branch without asking.

## Commands

- `uv sync` installs dependencies (pytest is a dev dependency).
- `uv run agent-template` (or `uv run python -m app`) runs the entry point `app:main`.
- `uv run pytest` runs all tests; `uv run pytest tests/unit/test_smoke.py::test_package_imports` runs one.
- `uv add <pkg>` adds a runtime dependency; `uv add --dev <pkg>` adds a dev-only one. Don't edit `uv.lock` by hand.
- No linter, formatter, or type checker is configured.

## Layout

- `src/app/`: `schemas.py` (contracts), `agents/`, `tools/`, `prompts/`, `workflows/` (LangGraph orchestration), `memory/`, `llm/` (model clients), and `config.py` (settings read from env vars).
- `tests/unit/` and `tests/integration/`, with shared fixtures in `tests/conftest.py`.
- `docs/project.md` is the project description (imported above); swap it out per project. `evals/`, `scripts/`, and `notebooks/` are empty placeholders. `data/` is gitignored except for `.gitkeep`.
- Copy `.env.example` to `.env` for local settings. `.env` is gitignored.
