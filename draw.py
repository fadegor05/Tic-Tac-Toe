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

    # Draw functions
    def draw(self, field):
        print("  A B C")
        for x,row in enumerate(field):
            a = f"{x+1} "
            for item in row:
                a += self.icons[item]
            print(a)