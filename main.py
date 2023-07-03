from config import *
from draw import Draw
from random import randint

# Main game class
class Game():
    def __init__(self):
        # Initialization
        self.draw = Draw(ICONS)
        # Generating a game field
        self.field = self.create_field()
        # Getting a winning position on field
        self.win_positions = self.generate_win_positions()
        # Starting main game loop
        self.main_loop()

    #init functions
    def create_field(self):
        return [ [ EMPTY for f in range(0,3) if i < 3] for i in range(0,3) if i < 3 ]
    
    def generate_win_positions(self):
        positions = []
        # horizontal lines
        for i in range(0,3):
            positions.append( [[i,j] for j in range(0,3) ])
        # vertical lines
        for i in range(0,3):
            positions.append( [[j,i] for j in range(0,3) ])
        # positive diagonal
        positions.append( [[i,i] for i in range(0,3) ])
        # negative diagonal
        positions.append( [[i,-i+2] for i in range(0,3) ])

        return positions
        

    # Game functions
    def is_free(self, x, y):
        return True if self.field[y][x] == EMPTY else False
    
    def make_move(self, tagger, x, y):
        place = self.is_free(x,y)
        self.field[y][x] = tagger if place else self.field[y][x]
        return place

    def check_win(self, tagger):
        t = 0
        for item in self.win_positions:
            j = 0
            for positions in item:
                j += 1 if tagger == self.field[positions[0]][positions[1]] else 0
            t += 1 if j == 3 else 0
        return True if t >= 1 else False

    # Input functions
    def can_decipher(self, string : str):
        if len(string) != 2:
            return False
        else:
            return False if list(string)[0] not in COLS or list(string)[1] not in ROWS else True

    def decipher_position(self, string : str):
        return (int(list(string)[1])-1, POS[list(string)[0]])
        

    # Main functions
    def end(self):
        if self.check_win(PLAYER):
            self.draw.draw(self.field)
            self.draw.win(PLAYER)
        if self.check_win(ENEMY):
            self.draw.draw(self.field)
            self.draw.win(ENEMY)

    def main_loop(self):
        while True:
            #player
            while True:
                self.draw.draw(self.field)
                self.draw.draw_move(PLAYER)
                out = input(">> ")
                if self.can_decipher(out) == True and self.make_move(PLAYER, self.decipher_position(out)[1], self.decipher_position(out)[0]):
                        self.draw.draw_moved(PLAYER)
                        self.draw.draw(self.field)
                        break
                else:
                    self.draw.draw_error()

            if self.check_win(PLAYER) or self.check_win(ENEMY):
                self.end()
                break
            #enemy
            while True:
                self.draw.draw(self.field)
                self.draw.draw_move(ENEMY)
                if self.make_move(ENEMY, randint(0, 2), randint(0, 2)):
                        self.draw.draw(self.field)
                        self.draw.draw_moved(ENEMY)
                        break
            if self.check_win(PLAYER) or self.check_win(ENEMY):
                self.end()
                break

if __name__ == '__main__':
    game = Game()








