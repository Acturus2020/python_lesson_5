import random


class Board:
    rows = None
    rows_opponent = None
    rows_for_player_boom = None
    ship_x_temp_coord = 0
    ship_y_temp_coord = 0
    ship_x_temp_coord_list = []
    ship_y_temp_coord_list = []
    game_counter = 0
    game_counter_opponent = 0
    rand_method_of_ships_create = False
    ships_draw_for_bot = False

    def __init__(self, row_count=10):
        self.rows = [[' ' for x in range(row_count)] for y in range(row_count)]
        self.rows_opponent = [[' ' for x in range(row_count)] for y in range(row_count)]
        self.rows_for_player_boom = [[' ' for x in range(row_count)] for y in range(row_count)]

    def print_board(self):
        numb_for_x_board = 1
        print("x,y", end='')
        for row in self.rows:
            print(numb_for_x_board, "   ", end="")
            numb_for_x_board += 1
        print('')
        numb_for_y_board = 1
        for row in self.rows:
            print(numb_for_y_board, end='')
            print(row)
            numb_for_y_board += 1

    def print_board_for_boom(self):
        numb_for_x_board = 1
        print("x,y", end='')
        for row in self.rows_for_player_boom:
            print(numb_for_x_board, "   ", end="")
            numb_for_x_board += 1
        print('')
        numb_for_y_board = 1
        for row in self.rows_for_player_boom:
            print(numb_for_y_board, end='')
            print(row)
            numb_for_y_board += 1

    def print_board_bot(self):
        numb_for_x_board = 1
        print("x,y", end='')
        for row in self.rows_opponent:
            print(numb_for_x_board, "   ", end="")
            numb_for_x_board += 1
        print('')
        numb_for_y_board = 1
        for row in self.rows_opponent:
            print(numb_for_y_board, end='')
            print(row)
            numb_for_y_board += 1

    def make_bum_bot(self):
        while True:
            boom_x_temp_coord = random.randrange(0, 10)
            boom_y_temp_coord = random.randrange(0, 10)
            if self.rows[boom_x_temp_coord][boom_y_temp_coord] == '*':
                continue
            break
        if self.rows[boom_x_temp_coord][boom_y_temp_coord] == '0':
            self.rows[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            print("Bot hit!")
            self.print_board()
            self.print_board_for_boom()
            self.game_counter -= 1
            if 0 > boom_x_temp_coord - 1 or self.rows[boom_x_temp_coord-1][boom_y_temp_coord] != '0':
                if 0 > boom_y_temp_coord - 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord-1] != '0':
                    if 9 < boom_x_temp_coord + 1 or self.rows[boom_x_temp_coord+1][boom_y_temp_coord] != '0':
                        if 9 < boom_y_temp_coord + 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord+1] != '0':
                            print('Bot drown Your ship!')
        else:
            print("Bot miss!")
            self.rows[boom_x_temp_coord][boom_y_temp_coord] = '*'
            self.print_board()
            self.print_board_for_boom()

    def make_bum(self):
        boom_x_temp_coord = 0
        boom_y_temp_coord = 0
        while True:
            print('Please input boom coords x and y:')
            boom_x_temp_coord = input('x')
            boom_y_temp_coord = input('y')
            if not boom_x_temp_coord.isdigit() or not boom_y_temp_coord.isdigit():
                print('ERROR Your input false, please write number!')
                continue
            boom_x_temp_coord = int(boom_x_temp_coord) - 1
            boom_y_temp_coord = int(boom_y_temp_coord) - 1
            if not 0 <= boom_x_temp_coord < 10 or not 0 <= boom_y_temp_coord < 10:
                print('Please write coordinate between 1 and 10!')
                continue
            if self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] == '*':
                print('This cell was boomed in previously turn!')
                continue
            break
        if self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] == '0':
            self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            self.rows_for_player_boom[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            print("You hit!")
            self.game_counter_opponent -= 1
            if 0 > boom_x_temp_coord - 1 or self.rows[boom_x_temp_coord-1][boom_y_temp_coord] != '0':
                if 0 > boom_y_temp_coord - 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord-1] != '0':
                    if 9 < boom_x_temp_coord + 1 or self.rows[boom_x_temp_coord+1][boom_y_temp_coord] != '0':
                        if 9 < boom_y_temp_coord + 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord+1] != '0':
                            print('You drown the ship!')
        else:
            print("You miss!")
            self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] = '*'
            self.rows_for_player_boom[boom_x_temp_coord][boom_y_temp_coord] = '*'

    def write_coord(self):
        while True:
            print('Please input front coordinate x and y of first number_of_ship_deck:')
            self.ship_x_temp_coord = input('x')
            self.ship_y_temp_coord = input('y')
            if not self.ship_x_temp_coord.isdigit() or not self.ship_y_temp_coord.isdigit():
                print('ERROR Your input false, please write number!')
                continue
            self.ship_x_temp_coord = int(self.ship_x_temp_coord) - 1
            self.ship_y_temp_coord = int(self.ship_y_temp_coord) - 1
            if not 0 <= self.ship_x_temp_coord < 10 or not 0 <= self.ship_y_temp_coord < 10:
                print('Please write coordinate between 1 and 10!')
                continue
            if not self.rows[self.ship_x_temp_coord][self.ship_y_temp_coord] == ' ':
                print('Please choose empty cell!')
                continue
            break

    def method_of_random_draw(self, number_of_ship_deck):
        self.ship_x_temp_coord = random.randrange(0, 10)
        self.ship_y_temp_coord = random.randrange(0, 10)
        if not self.ships_draw_for_bot:
            if not self.rows[self.ship_x_temp_coord][self.ship_y_temp_coord] == ' ':
                return
            self.game_counter = self.draw_ship(number_of_ship_deck, self.rows, self.game_counter)
        else:
            if not self.rows_opponent[self.ship_x_temp_coord][self.ship_y_temp_coord] == ' ':
                return
            self.game_counter_opponent = self.draw_ship(number_of_ship_deck, self.rows_opponent, self.game_counter_opponent)

    def draw_all_ships_random_bot(self):
        self.ships_draw_for_bot = True
        self.rand_method_of_ships_create = True
        while self.game_counter_opponent != 4:
            self.method_of_random_draw(4)
        while self.game_counter_opponent != 7:
            self.method_of_random_draw(3)
        while self.game_counter_opponent != 10:
            self.method_of_random_draw(3)
        while self.game_counter_opponent != 12:
            self.method_of_random_draw(2)
        while self.game_counter_opponent != 14:
            self.method_of_random_draw(2)
        while self.game_counter_opponent != 16:
            self.method_of_random_draw(2)
        while self.game_counter_opponent != 17:
            self.method_of_random_draw(1)
        while self.game_counter_opponent != 18:
            self.method_of_random_draw(1)
        while self.game_counter_opponent != 19:
            self.method_of_random_draw(1)
        while self.game_counter_opponent != 20:
            self.method_of_random_draw(1)

    def draw_all_ships_random(self):
        self.rand_method_of_ships_create = True
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

    def draw_ship(self, number_of_ship_deck, rows, counter):
        read_cord_of_ship = '0'
        self.ship_x_temp_coord_list = []
        self.ship_y_temp_coord_list = []
        if self.rand_method_of_ships_create:
            self.rand_count = random.randrange(1, 5)
        else:
            print('Please draw', number_of_ship_deck, 'number_of_ship_deck ship:')
            self.write_coord()
            print('Choose rear of your', number_of_ship_deck, '-number_of_ship_deck ship:')
        self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
        self.ship_y_temp_coord_list.append(self.ship_y_temp_coord)
        rows[self.ship_x_temp_coord][self.ship_y_temp_coord] = '0'
        if 1 < number_of_ship_deck < 5:
            while True:
                if self.ship_y_temp_coord - (number_of_ship_deck-1) >= 0 and rows[self.ship_x_temp_coord][self.ship_y_temp_coord-(number_of_ship_deck-1)] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + 1, ":", self.ship_y_temp_coord - (number_of_ship_deck - 2),
                              'coordinats for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 2 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord - numb)
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
                        break
                elif self.ship_y_temp_coord + (number_of_ship_deck-1) < 10 and rows[self.ship_x_temp_coord][self.ship_y_temp_coord+(number_of_ship_deck-1)] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + 1, ":", self.ship_y_temp_coord + number_of_ship_deck,
                              'coordinats for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 1 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord + numb)
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
                        break
                elif self.ship_x_temp_coord - (number_of_ship_deck-1) >= 0 and rows[self.ship_x_temp_coord-(number_of_ship_deck-1)][self.ship_y_temp_coord] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord - (number_of_ship_deck - 2), ":", self.ship_y_temp_coord + 1,
                              'coordinats for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 4 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord - numb)
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord)
                        break
                elif self.ship_x_temp_coord + (number_of_ship_deck-1) < 10 and rows[self.ship_x_temp_coord+(number_of_ship_deck-1)][self.ship_y_temp_coord] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + number_of_ship_deck, ":", self.ship_y_temp_coord + 1,
                              'coordinats for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 3 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord + numb)
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord)
                        break
                if self.rand_method_of_ships_create:
                    self.rand_count = random.randrange(1, 5)
                else:
                    print('Your input is wrong!')

            for numb_x in range(self.ship_x_temp_coord_list[0]-1, self.ship_x_temp_coord_list[0]+2):
                for numb_y in range(self.ship_y_temp_coord_list[0] - 1, self.ship_y_temp_coord_list[0] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        rows[numb_x][numb_y] = '.'
            for numb_x in range(self.ship_x_temp_coord_list[number_of_ship_deck-1] - 1, self.ship_x_temp_coord_list[number_of_ship_deck-1] + 2):
                for numb_y in range(self.ship_y_temp_coord_list[number_of_ship_deck-1] - 1, self.ship_y_temp_coord_list[number_of_ship_deck-1] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        rows[numb_x][numb_y] = '.'
            for numb in range(0, number_of_ship_deck):
                rows[self.ship_x_temp_coord_list[numb]][self.ship_y_temp_coord_list[numb]] = '0'
            counter += number_of_ship_deck
        elif number_of_ship_deck == 1:
            for numb_x in range(self.ship_x_temp_coord_list[0]-1, self.ship_x_temp_coord_list[0]+2):
                for numb_y in range(self.ship_y_temp_coord_list[0] - 1, self.ship_y_temp_coord_list[0] + 2):
                    if 0 <= numb_x < 10 and 0 <= numb_y < 10:
                        rows[numb_x][numb_y] = '.'
            rows[self.ship_x_temp_coord_list[0]][self.ship_y_temp_coord_list[0]] = '0'
            counter += 1
        else:
            print('Count of your number_of_ship_deck is wrong!')
        return counter


def main():
    BoardUser = Board()
    BoardUser.draw_all_ships_random()
    BoardUser.print_board()
    BoardUser.draw_all_ships_random_bot()
    BoardUser.print_board_for_boom()
    while BoardUser.game_counter_opponent > 0 and BoardUser.game_counter > 0:
        BoardUser.make_bum()
        BoardUser.make_bum_bot()
    raise SystemExit


if __name__ == '__main__':
     main()