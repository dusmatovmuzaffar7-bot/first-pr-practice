# CLAUDE.md

Guidance for AI assistants (Claude Code) working in this repository.

## Repository purpose

This is a small practice repository for learning the GitHub pull request
workflow. It is intentionally simple — a few standalone scripts, not a
unified application. Don't assume the projects in this repo share
dependencies, tooling, or a build system.

## Structure

```
.
├── greet.py            # Standalone script: greet/farewell/good_morning helpers
├── test_greet.py       # pytest tests for greet.py
├── README.md           # Top-level repo description
├── telegram-ai-bot/    # Separate, self-contained Python project
│   ├── bot.py          # Telegram bot: chat, /music, /image commands
│   ├── requirements.txt
│   ├── .env.example    # Template for required env vars (never commit .env)
│   └── README.md       # Setup instructions (in Russian)
├── .githooks/
│   └── commit-msg      # Enforces Conventional Commits on every commit
└── .claude/
    ├── settings.json    # Hooks config (SessionStart -> session-start.sh)
    ├── hooks/session-start.sh  # Wires git core.hooksPath to .githooks
    └── skills/conventional-commits/SKILL.md
```

### `greet.py` / `test_greet.py`

Trivial pure functions (`greet`, `farewell`, `good_morning`), each taking an
optional `name` (default `"World"`) and returning a formatted string. Run
directly with `python3 greet.py`. Tests use pytest:

```bash
python3 -m pytest test_greet.py -v
```

When adding a new greeting-style function, follow the existing pattern:
a one-line function with a `name="World"` default, plus matching default/
custom-name test cases in `test_greet.py`.

### `telegram-ai-bot/`

A standalone Telegram bot using `python-telegram-bot`, OpenAI API, and
`ytmusicapi`. It is not wired into the rest of the repo — it has its own
`requirements.txt` and `.env`.

- Requires `TELEGRAM_BOT_TOKEN` and `OPENAI_API_KEY` env vars (see
  `.env.example`); loaded via `python-dotenv`.
- Optional env vars: `CHAT_MODEL` (default `gpt-4o-mini`), `IMAGE_MODEL`
  (default `gpt-image-1`).
- Commands: `/start`, `/music <query>` (returns YouTube Music search links
  only — never downloads or forwards audio), `/image <prompt>` (OpenAI image
  generation), plus a plain-text handler that proxies to OpenAI chat
  completions.
- Setup/run:
  ```bash
  cd telegram-ai-bot
  python3 -m venv venv && source venv/bin/activate
  pip install -r requirements.txt
  cp .env.example .env   # then fill in the two keys
  python3 bot.py
  ```
- **Never commit `.env`** — it's gitignored for a reason; it holds live API
  keys/tokens.

## Commit conventions (enforced by git hook)

This repo enforces [Conventional Commits](.claude/skills/conventional-commits/SKILL.md)
via a `commit-msg` git hook at `.githooks/commit-msg`, activated automatically
each session by `.claude/hooks/session-start.sh` (sets
`core.hooksPath = .githooks`).

Every commit subject line must match:

```
<type>(<scope>): <summary>
```

Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
`build`, `ci`, `chore`, `revert`. Scope is optional and lowercase (usually
the module/file touched, e.g. `greet`, `telegram-ai-bot`). Use imperative
mood, no trailing period, ≤72 chars. Breaking changes append `!` after the
type/scope and add a `BREAKING CHANGE:` footer. Commits that don't match
this pattern are rejected by the hook (merge/revert commits are exempt).

Always use the `conventional-commits` skill (or follow this format
manually) before running `git commit` in this repo.

## Working conventions

- Keep changes scoped to one project at a time (`greet.py`/tests vs.
  `telegram-ai-bot/`) — they're unrelated codebases sharing a repo.
- No CI/build pipeline exists beyond the commit-msg hook; verify Python
  changes locally with `python3 -m pytest` (root) or by running
  `bot.py` manually (requires real API keys, so prefer static review for
  bot.py changes unless the user provides credentials).
- Do not commit secrets, `.env` files, or API keys.
- This repo has no linter/formatter configured — match existing style
  (plain functions, no type hints, minimal docstrings) rather than
  introducing new tooling.
