

class Board:
    rows = None
    four_deck_coord_x = []
    four_deck_coord_y = []
    three_deck_first_coord = []
    three_deck_second_coord = []
    two_deck_first_coord = []
    two_deck_second_coord = []
    two_deck_third_coord = []
    one_deck_coords = []

    count = True

    def __init__(self, row_count=10):
        self.rows = [[' ' for x in range(row_count)] for y in range(row_count)]

    def print_x_num(self):
        x_num = 1
        print("y,x", end='')
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

    def draw_ship_4_deck(self):
        ship_x = 0
        ship_y = 0
        print('Please input front coordinate x and y of 4-deck ship:')
        ship_x = input('x')
        ship_y = input('y')
        if not ship_x.isdigit() or not ship_y.isdigit():
            print('ERROR Your input false, please write number!')
        ship_y = int(ship_y)
        ship_x = int(ship_x)
        self.rows[ship_y - 1][ship_x - 1] = '0'
        self.four_deck_coord_x.append(ship_y-1)
        self.four_deck_coord_y.append(ship_x-1)
        self.print_board()
        print('Choose rear of your 4-deck ship:')
        while True:
            if (ship_x-1) - 3 >= 0:
                print('If you want', ship_x-3, ":", ship_y, 'coordinats for you ship, press 1, if no press 2')
                input_choose_cord = input()
                if int(input_choose_cord) == 1:
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x - 2)
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x - 3)
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x - 4)
                    break
            if (ship_x - 1) + 3 < 10:
                print('If you want', ship_x + 3, ":", ship_y, 'coordinats for you ship, press 1, if no press 2')
                input_choose_cord = input()
                if int(input_choose_cord) == 1:
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x)
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x + 1)
                    self.four_deck_coord_x.append(ship_y - 1)
                    self.four_deck_coord_y.append(ship_x + 2)
                    break
            if (ship_y - 1) - 3 >= 0:
                print('If you want', ship_x, ":", ship_y - 3, 'coordinats for you ship, press 1, if no press 2')
                input_choose_cord = input()
                if int(input_choose_cord) == 1:
                    self.four_deck_coord_x.append(ship_y - 2)
                    self.four_deck_coord_y.append(ship_x - 1)
                    self.four_deck_coord_x.append(ship_y - 3)
                    self.four_deck_coord_y.append(ship_x - 1)
                    self.four_deck_coord_x.append(ship_y - 4)
                    self.four_deck_coord_y.append(ship_x - 1)
                    break
            if (ship_y - 1) + 3 < 10:
                print('If you want', ship_x, ":", ship_y + 3, 'coordinats for you ship, press 1, if no press 2')
                input_choose_cord = input()
                if int(input_choose_cord) == 1:
                    self.four_deck_coord_x.append(ship_y)
                    self.four_deck_coord_y.append(ship_x - 1)
                    self.four_deck_coord_x.append(ship_y + 1)
                    self.four_deck_coord_y.append(ship_x - 1)
                    self.four_deck_coord_x.append(ship_y + 2)
                    self.four_deck_coord_y.append(ship_x - 1)
                    break
        # print(self.four_deck_coord_x)
        # print(self.four_deck_coord_y)
        for numb in range(0, 4):
            self.rows[self.four_deck_coord_x[numb]][self.four_deck_coord_y[numb]] = '0'
        self.print_board()

        # def draw_ship_3_deck(self):


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
    BoardUser.draw_ship_4_deck()


if __name__ == '__main__':
     main()
