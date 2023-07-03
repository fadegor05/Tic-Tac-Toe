from config import *
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich.markdown import Markdown
from rich import print
from rich.panel import Panel


# Main draw class
class Draw:
    def __init__(self, icons):
        self.icons = icons
        self.console = Console(theme=Theme({'title': 'bold green blink','info': 'dim cyan', 'warning': 'bold yellow'}))

    # Draw functions
    def draw(self, field):
        table = Table(' ', 'A', 'B', 'C')
        for x,row in enumerate(field):
            items_row = []
            for item in row: 
                items_row.append(ICONS[item])
            table.add_row(str(x+1), items_row[0], items_row[1], items_row[2])
        self.console.print(table)

    def win(self, tagger):
        if tagger == PLAYER:
            print(Panel(f" Congratulations! [bold green]You[/bold green] won!"))
        if tagger == ENEMY:
            print(Panel(f"[bold red] You[/bold red] lose!"))

    def draw_move(self, tagger):
        if tagger == PLAYER:
            print(Panel(f"[bold green]You[/bold green] need to make a move!"))
        if tagger == ENEMY:
            print(Panel(f"Your [bold red]enemy[/bold red] are making move!"))

    def draw_moved(self, tagger):
        if tagger == PLAYER:
            print(Panel(f"[bold green]You[/bold green] made a move!"))
        if tagger == ENEMY:
            print(Panel(f"Your [bold red]enemy[/bold red] made a move!"))

    def draw_error(self):
        print(Panel(f"[bold yellow]Try again...[/bold yellow]"))