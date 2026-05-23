from rich.console import Console 
from rich.table import Table
from rich.text import Text

console = Console()

def render_table(writeups):
    table = Table()
    table.add_column("nr.")
    table.add_column("title")
    table.add_column("ctf")
    table.add_column("category")
    table.add_column("points")
    table.add_column("solved")
    table.add_column("date")

    for i,w in enumerate(writeups):
        solved = Text("-", style="dim")
        if w.solved:
            solved = Text("v", style = "green")
        table.add_row(
            str(i+1), #nr
            w.title,
            w.ctf,
            w.category,
            str(w.points),
            solved,
            str(w.date)
        )

    console.print(table)
