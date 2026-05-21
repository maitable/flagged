# Flagged
> A CLI tracker for Capture The Flag problem write-ups 

## Pre-Build specs
### Flagged commands 
-  **flagged init** - create a vault in the current directory
-  **flagged new** - interactive wizard that creates **writeup.md**, opens in $EDITOR
-  **flagged list** - rich table of all writeups, filterable by ctf/category/solved
-  **flagged show [slug]** - render writeup in terminal with rich markdown
- **flagged edit [slug]** - open in $EDITOR
- **flagged search [query]** - grep that searches in titles, tags and content
- **flagged flag [slug] [flag]** - set solved = True, save flag
- **flagged stats** - dashboard(solve rate, categories, points, top CTFs)


| Thing | Package | Why |
|---|---|---|
| CLI framework | `typer` | auto-generates `--help`, supports subcommands cleanly |
| Terminal output | `rich` | tables, markdown rendering, panels, progress |
| Frontmatter parsing | `python-frontmatter` | reads/writes YAML frontmatter without touching content |
| Config file | `tomllib` (stdlib 3.11+) / `tomli` fallback | no extra dep for reading `.ctf.toml` |
| Fuzzy slug match | `difflib.get_close_matches` | stdlib, no dep, good enough |
| Date handling | `datetime` (stdlib) | no need for arrow/pendulum |
