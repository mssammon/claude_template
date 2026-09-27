# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

This repository is a fresh git repo (branch `main`, no commits yet) that holds only a `.gitignore`, which ignores `.env`, logs, `*.pyc`, and editor backup files. It has no source code, dependency manifest, tests, or README yet, so there are no build, lint, or test commands to document.

It lives under `~/projects`, so the workspace-level `~/projects/CLAUDE.md` applies. In particular, a new Python project here should use **uv** (`uv init`, `uv sync`, `uv run pytest path/to/test_file.py::test_name`) rather than poetry, and should target Python 3.11.

Update this file with real commands and architecture notes once code is added.
