import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter


class Board:
    message = ''
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
        self.rand_count = random.randrange(1, 5)

    def make_bum_bot(self):
        while True:
            boom_x_temp_coord = random.randrange(0, 10)
            boom_y_temp_coord = random.randrange(0, 10)
            if self.rows[boom_x_temp_coord][boom_y_temp_coord] == '*':
                continue
            break
        if self.rows[boom_x_temp_coord][boom_y_temp_coord] == '0':
            self.rows[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            self.message += ", bot hit!"
            self.game_counter -= 1
            if 0 > boom_x_temp_coord - 1 or self.rows[boom_x_temp_coord-1][boom_y_temp_coord] != '0':
                if 0 > boom_y_temp_coord - 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord-1] != '0':
                    if 9 < boom_x_temp_coord + 1 or self.rows[boom_x_temp_coord+1][boom_y_temp_coord] != '0':
                        if 9 < boom_y_temp_coord + 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord+1] != '0':
                            self.message += 'Bot drown Your ship!'
        else:
            self.message += ", bot miss!"
            self.rows[boom_x_temp_coord][boom_y_temp_coord] = '*'

    def make_bum(self, x, y):
        boom_x_temp_coord = x
        boom_y_temp_coord = y
        if self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] == '0':
            self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            self.rows_for_player_boom[boom_x_temp_coord][boom_y_temp_coord] = 'X'
            self.message = "You hit!"
            self.game_counter_opponent -= 1
            if 0 > boom_x_temp_coord - 1 or self.rows[boom_x_temp_coord-1][boom_y_temp_coord] != '0':
                if 0 > boom_y_temp_coord - 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord-1] != '0':
                    if 9 < boom_x_temp_coord + 1 or self.rows[boom_x_temp_coord+1][boom_y_temp_coord] != '0':
                        if 9 < boom_y_temp_coord + 1 or self.rows[boom_x_temp_coord][boom_y_temp_coord+1] != '0':
                            self.message = 'You drown the ship!'
                            return
        elif self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] == 'X':
            self.message = "You was shooting for this cell!"
        else:
            self.message = "You miss!"
            self.rows_opponent[boom_x_temp_coord][boom_y_temp_coord] = '*'
            self.rows_for_player_boom[boom_x_temp_coord][boom_y_temp_coord] = '*'

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

    def draw_all_ships_random(self, draw_bot=False):
        self.ships_draw_for_bot = draw_bot
        self.rand_method_of_ships_create = True
        if draw_bot:
            while self.game_counter_opponent != 4:
                self.method_of_random_draw(4)
        else:
            while self.game_counter != 4:
                self.method_of_random_draw(4)
        if draw_bot:
            while self.game_counter_opponent != 7:
                self.method_of_random_draw(3)
        else:
            while self.game_counter != 7:
                self.method_of_random_draw(3)
        if draw_bot:
            while self.game_counter_opponent != 10:
                self.method_of_random_draw(3)
        else:
            while self.game_counter != 10:
                self.method_of_random_draw(3)
        if draw_bot:
            while self.game_counter_opponent != 12:
                self.method_of_random_draw(2)
        else:
            while self.game_counter != 12:
                self.method_of_random_draw(2)
        if draw_bot:
            while self.game_counter_opponent != 14:
                self.method_of_random_draw(2)
        else:
            while self.game_counter != 14:
                self.method_of_random_draw(2)
        if draw_bot:
            while self.game_counter_opponent != 16:
                self.method_of_random_draw(2)
        else:
            while self.game_counter != 16:
                self.method_of_random_draw(2)
        if draw_bot:
            while self.game_counter_opponent != 17:
                self.method_of_random_draw(1)
        else:
            while self.game_counter != 17:
                self.method_of_random_draw(1)
        if draw_bot:
            while self.game_counter_opponent != 18:
                self.method_of_random_draw(1)
        else:
            while self.game_counter != 18:
                self.method_of_random_draw(1)
        if draw_bot:
            while self.game_counter_opponent != 19:
                self.method_of_random_draw(1)
        else:
            while self.game_counter != 19:
                self.method_of_random_draw(1)
        if draw_bot:
            while self.game_counter_opponent != 20:
                self.method_of_random_draw(1)
        else:
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
            print('Choose rear of your', number_of_ship_deck, '-number_of_ship_deck ship:')
        self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
        self.ship_y_temp_coord_list.append(self.ship_y_temp_coord)
        rows[self.ship_x_temp_coord][self.ship_y_temp_coord] = '0'
        if 1 < number_of_ship_deck < 5:
            while True:
                if self.ship_y_temp_coord - (number_of_ship_deck-1) >= 0 and rows[self.ship_x_temp_coord][self.ship_y_temp_coord-(number_of_ship_deck-1)] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + 1, ":", self.ship_y_temp_coord - (number_of_ship_deck - 2),
                              'coords for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 2 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord - numb)
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
                        break
                elif self.ship_y_temp_coord + (number_of_ship_deck-1) < 10 and rows[self.ship_x_temp_coord][self.ship_y_temp_coord+(number_of_ship_deck-1)] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + 1, ":", self.ship_y_temp_coord + number_of_ship_deck,
                              'coords for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 1 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord + numb)
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord)
                        break
                elif self.ship_x_temp_coord - (number_of_ship_deck-1) >= 0 and rows[self.ship_x_temp_coord-(number_of_ship_deck-1)][self.ship_y_temp_coord] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord - (number_of_ship_deck - 2), ":", self.ship_y_temp_coord + 1,
                              'coords for you ship, press 1, if no press 2')
                        read_cord_of_ship = input()
                    if self.rand_count == 4 or int(read_cord_of_ship) == 1:
                        for numb in range(1, number_of_ship_deck):
                            self.ship_x_temp_coord_list.append(self.ship_x_temp_coord - numb)
                            self.ship_y_temp_coord_list.append(self.ship_y_temp_coord)
                        break
                elif self.ship_x_temp_coord + (number_of_ship_deck-1) < 10 and rows[self.ship_x_temp_coord+(number_of_ship_deck-1)][self.ship_y_temp_coord] == ' ':
                    if not self.rand_method_of_ships_create:
                        print('If you want', self.ship_x_temp_coord + number_of_ship_deck, ":", self.ship_y_temp_coord + 1,
                              'coord for you ship, press 1, if no press 2')
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


class MainWindow(QMainWindow, QWidget):

    def __init__(self, Board_object, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Board_object = Board_object
        self.setWindowTitle("Ship wars")
        self.setFixedSize(851, 550)

        self.setStatusBar(QStatusBar(self))
        self.setStatusTip("Shot bomb!")

        self._size_cell = 40

    def mouseReleaseEvent(self, e):
        # Определяем позицию клика
        i = e.pos().y() // self._size_cell
        j = e.pos().x() // self._size_cell

        # Выход за пределы массива
        if i >= 10 or j >= 10:
            return
        self.Board_object.make_bum(i, j)
        if self.Board_object.rows_opponent[i][j] == '' or self.Board_object.rows_opponent[i][j] == '.' or self.Board_object.rows_opponent[i][j] == 'O':
            self.Board_object.rows_opponent[i][j] = '*'
        self.Board_object.make_bum_bot()

        self.setStatusTip(self.Board_object.message)
        # label.setText(str(self.Board_object.game_counter) + 'vs' + str(self.Board_object.game_counter_opponent))

        self.update()

    def paintEvent(self, e):
        if self.Board_object.game_counter == 0:
            label = QLabel("YOU LOOSE!")
            label.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(label)
            return
        if self.Board_object.game_counter_opponent == 0:
            label = QLabel("YOU WIN!")
            label.setAlignment(Qt.AlignCenter)
            self.setCentralWidget(label)
            return

        painter = QPainter(self)

        painter.setPen(Qt.black)
        painter.setBrush(Qt.white)

        for i in range(len(self.Board_object.rows_for_player_boom)):
            row = self.Board_object.rows_for_player_boom[i]

            for j in range(len(row)):
                x = j * self._size_cell
                y = i * self._size_cell
                w = self._size_cell
                h = self._size_cell

                painter.drawRect(x, y, w, h)

                painter.save()
                painter.setFont(QFont('Arial', 16))

                value = self.Board_object.rows_for_player_boom[i][j]
                painter.setPen(Qt.blue if value == 'O' else Qt.red)

                painter.drawText(x, y, w, h, Qt.AlignCenter, value)

                painter.restore()

        for i in range(len(self.Board_object.rows)):
            row = self.Board_object.rows[i]

            for j in range(len(row)):
                x = j * self._size_cell
                y = i * self._size_cell
                w = self._size_cell
                h = self._size_cell

                painter.drawRect(x+450, y, w, h)

                painter.save()
                painter.setFont(QFont('Arial', 16))

                value = self.Board_object.rows[i][j]
                painter.setPen(Qt.blue if value == 'O' else Qt.red)

                painter.drawText(x+450, y, w, h, Qt.AlignCenter, value)

                painter.restore()


def main():
    # Создаем экземпляр QApplication и передаем параметры командной строки
    app = QApplication(sys.argv)

    BoardUser = Board()
    BoardUser.draw_all_ships_random()
    BoardUser.draw_all_ships_random(True)

    # Создание окна приложения
    window = MainWindow(BoardUser)

    window.show()  # Окна скрыты по умолчанию!
    # Запуск цикла событий
    app.exec_()


if __name__ == '__main__':
     main()
