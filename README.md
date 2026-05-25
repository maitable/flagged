# Flagged
> a CLI tracker for CTF challenge write-ups

#### Prereqs:
- python 3.11+
- pip/pipx
- a terminal editor set as ```$EDITOR``` (default micro)

#### Setup with pip into a venv:
```bash
git clone https://github.com/maitable/flagged.git
cd flagged
python -m venv .venv
source .venv/bin/activate
pip install .
```

#### Init Flagged:
```bash
mkdir writeup-vault
cd writeup-vault
export EDITOR=nvim
flagged init
```

#### Basic usage:
```bash
flagged new #wizard that creates writeup.md and opens in $EDITOR
flagged list #renders all writeups in a table
flagged show [slug] #renders a writeup's content
flagged edit [slug] #open a writeup in $EDITOR
flagged search [query] #greps query, not functional yet
flagged flag [slug] [flag] #sets a writeup to solved, adds flag
```

> Thing still buggy because thing not done yet (ooga booga)
