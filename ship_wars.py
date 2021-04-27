import random


class Board:
    rows = None
    rows_opponent = None
    ship_x = 0
    ship_y = 0
    ship_coord_x = []
    ship_coord_y = []
    game_counter = 0
    game_counter_opponent = 0
    rand_count = 0
    random_method = False

    count = True

    def __init__(self, row_count=10):
        self.rows = [[' ' for x in range(row_count)] for y in range(row_count)]
        self.rows_opponent = [[' ' for x in range(row_count)] for y in range(row_count)]

    def print_x_num(self):
        x_num = 1
        print("x,y", end='')
        for row in self.rows:
            print(x_num, "   ", end="")
            x_num += 1
        print('')

    def print_board(self):
        self.print_x_num()
        y_num = 1
        for row in self.rows:
            print(y_num, end='')
            print(row)
            y_num += 1

    def make_bum(self):
        bom_x = 0
        bom_y = 0
        while True:
            print('Please input boom coords x and y:')
            bom_x = input('x')
            bom_y = input('y')
            if not bom_x.isdigit() or not bom_y.isdigit():
                print('ERROR Your input false, please write number!')
                continue
            bom_x = int(bom_x) - 1
            bom_y = int(bom_y) - 1
            if not 0 <= bom_x < 10 and not 0 <= bom_y < 10:
                print('Please write coordinate between 1 and 10!')
                continue
            if self.rows[bom_x][bom_y] == '*':
                print('This cell was boomed in previously turn!')
                continue
            break
        if self.rows[bom_x][bom_y] == '0':
            print("You hit!")
            self.game_counter -= 1
            if 0 > bom_x - 1 or self.rows[bom_x-1][bom_y] != '0':
                if 0 > bom_y - 1 or self.rows[bom_x][bom_y-1] != '0':
                    if 9 < bom_x + 1 or self.rows[bom_x+1][bom_y] != '0':
                        if 9 < bom_y + 1 or self.rows[bom_x][bom_y+1] != '0':
                            print('You drown the ship!')
        else:
            print("You miss!")
        self.rows[bom_x][bom_y] = '*'
        self.print_board()

    def write_coord(self):
        while True:
            print('Please input front coordinate x and y of first deck:')
            self.ship_x = input('x')
            self.ship_y = input('y')
            if not self.ship_x.isdigit() or not self.ship_y.isdigit():
                print('ERROR Your input false, please write number!')
                continue
            self.ship_x = int(self.ship_x) - 1
            self.ship_y = int(self.ship_y) - 1
            if not 0 <= self.ship_x < 10 or not 0 <= self.ship_y < 10:
                print('Please write coordinate between 1 and 10!')
                continue
            if not self.rows[self.ship_x][self.ship_y] == ' ':
                print('Please choose empty cell!')
                continue
            break

    def method_of_random_draw(self, deck):
        self.ship_x = random.randrange(0, 10)
        self.ship_y = random.randrange(0, 10)
        if not self.rows[self.ship_x][self.ship_y] == ' ':
            print('Please choose empty cell!')
            return
        self.draw_ship(deck)

    def draw_all_ships_random(self):
        self.random_method = True
        while self.game_counter != 4:
            self.method_of_random_draw(4)
        while self.game_counter != 7:
            self.method_of_random_draw(3)
        while self.game_counter != 10:
            self.method_of_random_draw(3)
        while self.game_counter != 12:
            self.method_of_random_draw(2)
        while self.game_counter != 14:
            self.method_of_random_draw(2)
        while self.game_counter != 16:
            self.method_of_random_draw(2)
        while self.game_counter != 17:
            self.method_of_random_draw(1)
        while self.game_counter != 18:
            self.method_of_random_draw(1)
        while self.game_counter != 19:
            self.method_of_random_draw(1)
        while self.game_counter != 20:
            self.method_of_random_draw(1)

    def draw_ship(self, deck):
        input_choose_cord = '0'
        self.ship_coord_x = []
        self.ship_coord_y = []
        if self.random_method:
            self.rand_count = random.randrange(1, 5)
        print('Please draw', deck, 'deck ship:')
        if not self.random_method:
            self.write_coord()
        self.ship_coord_x.append(self.ship_x)
        self.ship_coord_y.append(self.ship_y)
        self.rows[self.ship_x][self.ship_y] = '0'
        self.print_board()
        print('Choose rear of your', deck, '-deck ship:')
        if 1 < deck < 5:
            while True:
                if self.ship_y - (deck-1) >= 0 and self.rows[self.ship_x][self.ship_y-(deck-1)] == ' ':
                    print('If you want', self.ship_x+1, ":", self.ship_y - (deck-2), 'coordinats for you ship, press 1, if no press 2')
                    if not self.random_method:
                        input_choose_cord = input()
                    if self.rand_count == 1 or int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_y.append(self.ship_y - numb)
                            self.ship_coord_x.append(self.ship_x)
                        break
                elif self.ship_y + (deck-1) < 10 and self.rows[self.ship_x][self.ship_y+(deck-1)] == ' ':
                    print('If you want', self.ship_x+1, ":", self.ship_y+deck, 'coordinats for you ship, press 1, if no press 2')
                    if not self.random_method:
                        input_choose_cord = input()
                    if self.rand_count == 2 or int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_y.append(self.ship_y + numb)
                            self.ship_coord_x.append(self.ship_x)
                        break
                elif self.ship_x - (deck-1) >= 0 and self.rows[self.ship_x-(deck-1)][self.ship_y] == ' ':
                    print('If you want', self.ship_x-(deck-2), ":", self.ship_y+1, 'coordinats for you ship, press 1, if no press 2')
                    if not self.random_method:
                        input_choose_cord = input()
                    if int(input_choose_cord) == 1 or self.rand_count == 3:
                        for numb in range(1, deck):
                            self.ship_coord_x.append(self.ship_x - numb)
                            self.ship_coord_y.append(self.ship_y)
                        break
                elif self.ship_x + (deck-1) < 10 and self.rows[self.ship_x+(deck-1)][self.ship_y] == ' ':
                    print('If you want', self.ship_x+deck, ":", self.ship_y+1, 'coordinats for you ship, press 1, if no press 2')
                    if not self.random_method:
                        input_choose_cord = input()
                    if int(input_choose_cord) == 1 or self.rand_count == 4:
                        for numb in range(1, deck):
                            self.ship_coord_x.append(self.ship_x + numb)
                            self.ship_coord_y.append(self.ship_y)
                        break
                print('Your input is wrong!')
                if self.random_method:
                    self.rand_count = random.randrange(1, 5)

            for numb_x in range(self.ship_coord_x[0]-1, self.ship_coord_x[0]+2):
                for numb_y in range(self.ship_coord_y[0] - 1, self.ship_coord_y[0] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        self.rows[numb_x][numb_y] = '.'
            for numb_x in range(self.ship_coord_x[deck-1] - 1, self.ship_coord_x[deck-1] + 2):
                for numb_y in range(self.ship_coord_y[deck-1] - 1, self.ship_coord_y[deck-1] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        self.rows[numb_x][numb_y] = '.'
            for numb in range(0, deck):
                self.rows[self.ship_coord_x[numb]][self.ship_coord_y[numb]] = '0'
            self.game_counter += deck
        elif deck == 1:
            for numb_x in range(self.ship_coord_x[0]-1, self.ship_coord_x[0]+2):
                for numb_y in range(self.ship_coord_y[0] - 1, self.ship_coord_y[0] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        self.rows[numb_x][numb_y] = '.'
            self.rows[self.ship_coord_x[0]][self.ship_coord_y[0]] = '0'
            self.game_counter += 1
        else:
            print('Count of your deck is wrong!')
        self.print_board()


def main():
    BoardUser = Board()
    BoardUser.draw_all_ships_random()
    BoardUser.print_board()
    while BoardUser.game_counter > 0:
        BoardUser.make_bum()
    #
    # raise SystemExit


if __name__ == '__main__':
     main()
