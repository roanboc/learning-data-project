# Guards: Claude Code hooks and GitHub checks

One script, [`guard.py`](guard.py), runs both as Claude Code's hooks ([`.claude/settings.json`](../../.claude/settings.json))
and as GitHub's *Guards* check ([`.github/workflows/guards.yml`](../workflows/guards.yml)), so the same rules hold whoever
pushes. This repository's own rules are in [`local.py`](local.py); they hold [30-data-project/AGENTS.md](../../30-data-project/AGENTS.md).
`guard.py` is the same file in [learning-data](https://github.com/roanboc/learning-data/tree/main/.github/hooks): change one,
copy it to the other.

| When | What it does | Why |
|---|---|---|
| Before a shell command | Refuses force-push, a push to main, a commit with Co-authored-by, Claude-Session or "Generated with Claude Code" lines, `gh pr merge` without a squash and an explicit message, `rm -rf` on `/`, `~`, `.git`, `..` or `*` | Main's history is roanboc's alone, one squash per pull request |
| | Refuses `dbt run`, `build`, `seed`, `snapshot`, `run-operation`, `retry` or `clone` on any target but `duckdb`; `dbt parse --target databricks` stays fine, as CI runs it | Agents never change production; on Databricks a build runs as the agent's service principal, in its own development schema |
| | Refuses `dbt show` with more than 20 rows | Samples of at most 20 rows, never bulk personal data |
| | Refuses Databricks CLI calls that change the platform (bundle deploy or run, jobs, pipelines, grants, deletes, `api post`...) | A change reaches the platform only through a reviewed pull request and the release |
| | Refuses `cat` of a file over 300 KB; pipes noisy runs (`dbt build`, `test`, `parse`, the check scripts, `unittest`) through `guard.py trim`, which keeps the failures and the last 25 lines and saves the whole log | Tokens |
| Before a merge or workflow run through the GitHub tools | Squash only, with an explicit title and message and no Claude lines; no release workflow | |
| Before Edit or Write | Refuses credentials files and text that looks like a token or key; files whose first lines say they're generated (CODEOWNERS, the product descriptors...); dbt's output (`target/`, `logs/`, `dbt_packages/`, `.duckdb`) | Secrets never enter the repository; generated files come from their generator |
| Before Read | Refuses a whole read of dbt's output or of a file over 300 KB; reading with offset and limit is fine | Tokens |
| After Edit or Write | `profiles.yml`, `databricks.yml` and agents' workflows: no literal token, password or secret (read it with `env_var`). Model, source and test YAML: a new `severity: warn`, `enabled: false`, `where`, `warn_if` or `error_if` with no new test beside it, or fewer entries than before. A new model: its YAML beside it | Don't weaken a test to make it pass (30-data-project/AGENTS.md) |
| Session start | The branch, how far it is from `origin/main`, and the rules above in five lines | |
| Before a turn ends | Once each: commits not pushed (the container is reclaimed); models changed, so run `dbt build` and the `--check` scripts and put `impact.py`'s output in the pull request | |

On GitHub, *Guards* runs the tests beside the script, then `guard.py ci`: on every changed file, the credentials and token checks
and the same after-edit checks (a literal credential fails; a weakened test warns, for the reviewers), and every commit's message.
A Claude author or trailer warns on a pull request (the squash message must leave it out) and fails on main. It takes seconds.

Run the tests: `python -m unittest discover -s .github/hooks -p 'test_*.py'`. Try a hook by hand:
`echo '{"tool_input":{"command":"dbt build --target databricks"}}' | python3 .github/hooks/guard.py pre-bash`.

**Where the hooks load.** Claude Code reads `.claude/settings.json` from the folder a session starts in. A session started in
this repository runs them. A session that starts in a parent folder with both repositories beside it doesn't load either
repository's hooks; GitHub's *Guards* check still holds every change.
