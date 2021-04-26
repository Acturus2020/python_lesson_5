

class Board:
    rows = None
    ship_x = 0
    ship_y = 0
    ship_coord_x = []
    ship_coord_y = []

    count = True

    def __init__(self, row_count=10):
        self.rows = [[' ' for x in range(row_count)] for y in range(row_count)]

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

    def make_bum(self, x, y):
        self.rows[y-1][x-1] = '*'

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
            if not 0 <= self.ship_x < 10 and not 0 <= self.ship_y < 10:
                print('Please write coordinate between 1 and 10!')
                continue
            if not self.rows[self.ship_x][self.ship_y] == ' ':
                print('Please choose empty cell!')
                continue
            self.rows[self.ship_x][self.ship_y] = '0'
            break

    def draw_ship(self, deck):
        self.ship_coord_x = []
        self.ship_coord_y = []
        print('Please draw', deck, 'deck ship:')
        self.write_coord()
        self.ship_coord_x.append(self.ship_x)
        self.ship_coord_y.append(self.ship_y)
        self.print_board()
        print('Choose rear of your', deck, '-deck ship:')
        if 1 < deck < 5:
            while True:
                if self.ship_y - (deck-1) >= 0 and self.rows[self.ship_x][self.ship_y-(deck-1)] == ' ':
                    print('If you want', self.ship_x+1, ":", self.ship_y - (deck-2), 'coordinats for you ship, press 1, if no press 2')
                    input_choose_cord = input()
                    if int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_y.append(self.ship_y - numb)
                            self.ship_coord_x.append(self.ship_x)
                        break
                if self.ship_y + (deck-1) < 10 and self.rows[self.ship_x][self.ship_y+(deck-1)] == ' ':
                    print('If you want', self.ship_x+1, ":", self.ship_y+deck, 'coordinats for you ship, press 1, if no press 2')
                    input_choose_cord = input()
                    if int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_y.append(self.ship_y + numb)
                            self.ship_coord_x.append(self.ship_x)
                        break
                if self.ship_x - (deck-1) >= 0 and self.rows[self.ship_x-(deck-1)][self.ship_y] == ' ':
                    print('If you want', self.ship_x-(deck-2), ":", self.ship_y+1, 'coordinats for you ship, press 1, if no press 2')
                    input_choose_cord = input()
                    if int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_x.append(self.ship_x - numb)
                            self.ship_coord_y.append(self.ship_y)
                        break
                if self.ship_x + (deck-1) < 10 and self.rows[self.ship_x+(deck-1)][self.ship_y] == ' ':
                    print('If you want', self.ship_x+deck, ":", self.ship_y+1, 'coordinats for you ship, press 1, if no press 2')
                    input_choose_cord = input()
                    if int(input_choose_cord) == 1:
                        for numb in range(1, deck):
                            self.ship_coord_x.append(self.ship_x + numb)
                            self.ship_coord_y.append(self.ship_y)
                        break

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
        elif deck == 1:
            for numb_x in range(self.ship_coord_x[0]-1, self.ship_coord_x[0]+2):
                for numb_y in range(self.ship_coord_y[0] - 1, self.ship_coord_y[0] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        self.rows[numb_x][numb_y] = '.'
            self.rows[self.ship_coord_x[0]][self.ship_coord_y[0]] = '0'
        else:
            print('Count of your deck is wrong!')
        self.print_board()


def main():
    # user = Gamer(user=True)
    # pc = Gamer(user=False)
    # user.generate_board()
    # pc.generate_board()
    # game = Game(user, pc)
    # game.run()
    # while True:
    #     game.step_user()
    #     game.step_pc()
    #     game.check_winner()
    BoardUser = Board()
    # BoardUser.make_bum(1, 10)
    BoardUser.print_board()
    BoardUser.draw_ship(4)
    BoardUser.draw_ship(3)
    BoardUser.draw_ship(3)
    BoardUser.draw_ship(2)
    BoardUser.draw_ship(2)
    BoardUser.draw_ship(2)
    BoardUser.draw_ship(1)
    BoardUser.draw_ship(1)
    BoardUser.draw_ship(1)
    BoardUser.draw_ship(1)


if __name__ == '__main__':
     main()
