---
name: conventional-commits
description: Use when writing a commit message for this repo, or right before running `git commit`. Generates messages following the Conventional Commits specification (type(scope): summary) so the history stays readable and works with changelog/semantic-release tooling. Trigger on "write a commit message", "commit this", "помоги с commit-сообщением".
---

# Conventional Commits

Format every commit message as:

```
<type>(<scope>): <short summary>

<optional body>

<optional footer>
```

## Types

- `feat`: a new feature
- `fix`: a bug fix
- `docs`: documentation only changes
- `style`: formatting only, no code behavior change
- `refactor`: code change that neither fixes a bug nor adds a feature
- `perf`: performance improvement
- `test`: adding or correcting tests
- `build`: changes to the build system or dependencies
- `ci`: changes to CI configuration
- `chore`: other changes that don't modify src or test files
- `revert`: reverts a previous commit

## Rules

- Subject line: imperative mood, no trailing period, ideally <= 72 chars
  (e.g. "fix: handle empty name in greet()")
- Scope is optional, lowercase, names the affected module/file (e.g. "greet")
- Body explains *why*, separated from the subject by a blank line
- Breaking changes: append `!` after the type/scope (e.g. `feat!:`) and add
  a `BREAKING CHANGE:` footer describing the change and migration path

## Examples

```
feat(greet): add farewell function

fix(greet): handle empty name argument

docs: explain usage in README

test(greet): add tests for farewell function
```
