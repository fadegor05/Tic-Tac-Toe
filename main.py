import random
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich.markdown import Markdown
from rich import print
from rich.panel import Panel
from config import *

class Game():
    def __init__(self):
        custom_theme = Theme({'title': 'bold green blink','info': 'dim cyan', 'warning': 'bold yellow'})
        self.console = Console(theme=custom_theme)

        self.start = self.get_start()
        self.field = self.create_field()
        self.print_credits()
        self.game_cycle()

    def print_credits(self):
        cd = Markdown(CREDITS)
        self.console.print(cd)

    def create_field(self):
        field = []
        for row in range(0,3):
            row_items = []
            for item in range(0,3):
                row_items.append(SPACE)
            field.append(row_items)
        return field

    def draw_field(self):
        drawing = Table(' ', 'A', 'B', 'C')
        for x,row in enumerate(self.field):
            items_row = []
            for item in row: items_row.append(SYMBOLS[item])
            drawing.add_row(str(x+1), items_row[0], items_row[1], items_row[2])
        self.console.print(drawing)


    def get_start(self):
        return CROSS if random.randint(0,1) == 0 else NOUGHT

    def wait(self, wait_for):
        if wait_for == 0:
            self.console.print(f"Ожидание [bold green]{PLAYER_NAME[1]}[/bold green] хода ...")
            return input("> ")
        if wait_for == 1:
            self.console.print(f"[bold green]{ENEMY_NAME[0]}[/bold green] совершил ход, приступим к следующему ходу? ")
            input("> ")

    def start_game(self):
        a = PLAYER_NAME[0] if self.start == PLAYER else ENEMY_NAME[0]
        print(Panel(f"Первыми ходят: [bold]{ NAMES[self.start] } ( {a} )"))
        self.draw_field()
    def game_cycle(self):
        self.start_game()
        if self.start == PLAYER: p1, p2 = PLAYER, ENEMY
        else: p1, p2 = ENEMY, PLAYER
        while(True):
            self.make_turn(p1)
            if self.check_win() != None:
                self.draw_win(self.check_win())
                self.draw_field()
                break
            print(Panel(f"Теперь ходят: [bold]{NAMES[p2]}"))
            self.draw_field()
            self.make_turn(p2)
            if self.check_win() != None:
                self.draw_win(self.check_win())
                self.draw_field()
                break
            print(Panel(f"Теперь ходят: [bold]{NAMES[p1]}"))
            self.draw_field()

    def make_turn(self, activator):
        if activator == PLAYER:
            while(True):
                place = self.wait(0)
                try:
                    pos = list(place.upper())
                    pos[0] = D[pos[0]]
                    ints = []
                    for element in pos:
                        ints.append(int(element)-1)
                    if self.field[ints[1]][ints[0]] == SPACE:
                        self.field[ints[1]][ints[0]] = activator
                        break
                    else:
                        self.console.print(f'{PLAYER_NAME[0]}, выбрали уже занятое поле, попробуйте выбрать другое...',style='warning')

                except:
                    self.console.print(f'{PLAYER_NAME[0]}, ввели неверное значение, попробуйте еще раз...', style = 'warning')
        else:
            while(True):
                ints = [random.randint(0,2),random.randint(0,2)]
                try:
                    if self.field[ints[1]][ints[0]] == SPACE:
                        self.field[ints[1]][ints[0]] = activator
                        break
                except:
                    pass
            self.wait(1)

    def check_win(self):
        win = None
        #rows
        for z in self.field:
            noughts = 0
            crosses = 0
            for x in z:
                if x != SPACE:
                    noughts += 1 if x == NOUGHT else 0
                    crosses += 1 if x == CROSS else 0
            if win == None:
                if crosses == 3:
                    win = CROSS
                elif noughts == 3:
                    win = NOUGHT

        #cols
        cols = []
        for z,x in enumerate(range(0,3)):
            b = []
            for c, v in enumerate(range(0,3)): b.append(self.field[c][z])
            cols.append(b)

        for z in cols:
            noughts = 0
            crosses = 0
            for x in z:
                if x != SPACE:
                    noughts += 1 if x == NOUGHT else 0
                    crosses += 1 if x == CROSS else 0
            if win == None:
                if crosses == 3:
                    win = CROSS
                elif noughts == 3:
                    win = NOUGHT

        #diagonals
        temp = []
        for x in self.field:
            for z in x:
                temp.append(z)

        if temp[0] == NOUGHT and temp[4] == NOUGHT and temp[8] == NOUGHT:
            win = NOUGHT
        elif temp[0] == CROSS and temp[4] == CROSS and temp[8] == CROSS:
            win = CROSS

        if temp[2] == NOUGHT and temp[4] == NOUGHT and temp[6] == NOUGHT:
            win = NOUGHT
        elif temp[2] == CROSS and temp[4] == CROSS and temp[6] == CROSS:
            win = CROSS

        return win

    def draw_win(self, winner):
        winner_name = PLAYER_NAME[0] if winner == PLAYER else ENEMY_NAME[0]
        if winner == NOUGHT:
            print(Panel(f"Выйграли: [bold]{NAMES[NOUGHT]} ( {winner_name} )"))
        if winner == CROSS:
            print(Panel(f"Выйграли: [bold]{NAMES[CROSS]} ( {winner_name} )"))





if __name__ == '__main__':
    game = Game()








