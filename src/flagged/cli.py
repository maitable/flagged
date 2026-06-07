import typer
from pathlib import Path
from flagged.vault import find_vault_root
import subprocess

app = typer.Typer(help="Flagged", no_args_is_help=True)

@app.command()
def init():
    """Create a vault in the current directory."""
    cwd = Path.cwd()
    vault_file = cwd/".ctf.toml"

    if vault_file.exists():
        typer.echo("Vault already exists here.")
        raise typer.Exit(1)
    vault_file.touch()
    typer.echo(f"Complete vault init at {cwd}")
@app.command()
def new():
    """Create a new write-up"""
    ctf = typer.prompt("CTF Name")
    name = typer.prompt("Challenge")
    category = typer.prompt("Category ((crypto/web/pwn/rev/misc/forensics/osint)")
    points = typer.prompt("Points", default="0")
    difficulty = typer.prompt("Diff (easy/medium/hard)")
    tags = typer.prompt('Tags (comma-separated)', default="")

    year = str(__import__("datetime").date.today().year)
    ctf_slug = ctf.lower().replace(" ", "-")
    name_slug = name.lower().replace(" ", "-")

    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)
    writeup_path = vault / year / ctf_slug / f"{name_slug}.md"
    writeup_path.parent.mkdir(parents = True, exist_ok = True)

    tags_list = [t.strip() for t in tags.split(",") if t.strip()]
    template = f"""---
title: {name}
ctf: {ctf}
category: {category}
date: {__import__("datetime").date.today()}
solved: false
flag: ""
points: {points}
difficulty: {difficulty}
tags: {tags_list}
---

## Challenge

## Solution

## Flag
"""

    writeup_path.write_text(template)

    editor = __import__("os").environ.get("EDITOR", "nano")
    __import__("os").system(f"{editor} {writeup_path}")
    typer.echo(f"Created: {writeup_path}")

@app.command()
def list():
    """List all writeups!"""
    from flagged.writeup import list_all
    from flagged.display import render_table

    vault = find_vault_root()

    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)

    writeups = list_all(vault)
    render_table(writeups)

@app.command()
def show(slug: str):
    """Show a writeup in the terminal"""
    from flagged.writeup import resolve_slug
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    
    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)
    w = resolve_slug(vault, slug)
    if w is None:
        typer.echo(f"Err: No writeup matches {slug}")
        raise typer.Exit(1)

    console = Console()
    console.print(Panel(
        Markdown(w.content),
        title=w.title,
        subtitle = f"{w.ctf} - {w.category} - {w.points}pts"
    ))


@app.command()
def edit(slug: str):
    """Edit a writeup using environment variable EDITOR"""
    from flagged.writeup import resolve_slug
    import os
    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)

    w = resolve_slug(vault, slug)
    if w is None:
        typer.echo(f"Err: No writeup matches {slug}")
        raise typer.Exit(1)
    fp = w.path

    editor = os.environ.get("EDITOR", "micro")
    os.system(f"{editor} {fp}")

@app.command() 
def search(query:str):
    """Search a query across all writeups"""
    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)
    subprocess.run(["grep", "-r", query, str(vault)])

@app.command()
def flag(slug:str, flag:str):
    """Mark writeup as solved and set a flag"""
    from flagged.writeup import resolve_slug, save
    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)
    w = resolve_slug(vault, slug)
    if w is None:
        typer.echo(f"Err: No writeup matches {slug}")
        raise typer.Exit(1)

    fp = w.path
    w.solved = True
    w.flag = flag
    save(w)
    typer.echo(f"Flagged: {w.title} with flag {w.flag}")

@app.command()
def stats():
    """Show vault stats"""
    from flagged.writeup import list_all
    from flagged.display import render_stats
    vault = find_vault_root()
    if vault is None:
        typer.echo("Err: No vault found, Run flagged init first")
        raise typer.Exit(1)

    writeups = list_all(vault)
    render_stats(writeups)
