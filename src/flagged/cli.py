import typer
from pathlib import Path

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

    typer.echo("TODO")

@app.command()
def new():
    """Meow"""
    typer.echo("TODO")
