import typer

app = typer.Typer(help="Flagged")

@app.command()
def init():
    """Create a vault in the current directory."""
    typer.echo("TODO")
