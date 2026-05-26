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

def render_stats(writeups):
    if not writeups:
        console.print("No writeups here")
        return
    total = len(writeups)
    solved = sum(1 for w in writeups if w.solved)
    rate = solved/total*100 if total >0 else 0
   
    from rich.table import Table

    overview = Table(show_header=False, box=None, padding=(0, 3))
    overview.add_column()
    overview.add_column()
    overview.add_column()
    overview.add_column()

    overview.add_row(
        f"[bold]{total}[/bold]\n[dim]total[/dim]",
        f"[bold]{solved}[/bold]\n[dim]solved[/dim]",
        f"[bold]{sum(w.points for w in writeups if w.solved)}[/bold]\n[dim]points[/dim]",
        f"[bold]{rate:.1f}%[/bold]\n[dim]solve rate[/dim]",
    )

    console.print(overview)
    console.print()
