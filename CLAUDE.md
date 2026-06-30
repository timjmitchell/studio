# studio

## Toolchain preferences

- **Node.js**: managed via `nvm`. Don't install Node from Homebrew, the macOS installer, or `n`. If `node`/`npx` isn't on PATH, ensure nvm is sourced (`source ~/.nvm/nvm.sh`) before running.
- **Python**: managed via `uv`. Use `uv run`, `uv add`, `uv sync` — not `pip`, `pyenv`, or `poetry`.
- **Config files**: prefer TOML over JSON/YAML when authoring new config (e.g. `pyproject.toml` for Python projects).
