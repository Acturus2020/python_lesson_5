# lesson 5 Mateush Vilen
import math


def perumetr_kola(radius):
    PI = 3.1415926535
    return 2 * radius * PI


def ploscha_kola(radius):
    PI = 3.1415926535
    return (radius ** 2) * PI


def radius_in_per(perumetr):
    PI = 3.1415926535
    return perumetr / 2 / PI


def radius_in_ploscha(perumetr):
    PI = 3.1415926535
    return math.sqrt(perumetr / PI)


def print_n_close():
    print('message')
    raise SystemExit


def zodiack_search(month_birth, day_birth):
    zodiack = {
        'Aries': [[3, 21, 31], [4, 1, 19]],
        'Taurus': [[4, 20, 30], [5, 1, 20]],
        'Gemini': [[5, 21, 31], [6, 1, 20]],
        'Cancer': [[6, 21, 30], [7, 1, 22]],
        'Leo': [[7, 23, 31], [8, 1, 22]],
        'Virgo': [[8, 23, 31], [9, 1, 22]],
        'Libra': [[9, 23, 30], [10, 1, 22]],
        'Scorpio': [[10, 23, 31], [11, 1, 22]],
        'Sagittarius': [[11, 23, 30], [12, 1, 22]],
        'Capricorn': [[12, 22, 31], [1, 1, 19]],
        'Aquarius': [[1, 20, 31], [2, 1, 18]],
        'Pisces': [[2, 19, 29], [3, 1, 20]]
    }
    for key in zodiack:
        if zodiack[key][0][0] == month_birth and zodiack[key][0][1] <= day_birth <= zodiack[key][0][2]:
            return key
        elif zodiack[key][1][0] == month_birth and zodiack[key][1][1] <= day_birth <= zodiack[key][1][2]:
            return key
    return 'Your birth data is wrong'


def reverse_mas(user_mas=None):
    if user_mas is None:
        user_mas = {}
    mas_copy = user_mas.copy()
    len_mas = len(user_mas) - 1
    for x in range(0, 9):
        user_mas[x] = mas_copy[len_mas-x]
    return user_mas


# ------------My database from 4 lesson------------:
def my_database():
    work = True
    user_dict = {}
    user_numb = 0
    while work == True:
        print('Your personal database is work, you have this base:')
        print(user_dict)
        print('if you want add record press 1')
        print('if you wand delete record press 2')
        print('if you wand change record press 3')
        print('if you want exit press 4')
        user_numb = input()

        if user_numb.isdigit() == False:
            continue

        if int(user_numb) == 1:
            print('write key of record:')
            key1 = input()
            print('write value for your key:')
            value1 = input()
            if key1.isdigit() == True:
                key1 = int(key1)
            if value1.isdigit() == True:
                value1 = int(value1)
            user_dict.update({key1: value1})

        elif int(user_numb) == 2:
            print(user_dict)
            print('what number of record you want to delete?')
            del_key = input()
            if not del_key.isdigit():
                print('This is not correct number!')
                continue

            elif int(del_key) > len(user_dict) or int(del_key) <= 0:
                print('Your base doesnot have this number!')
                continue
            print(del_key)
            user_dict.pop(int(del_key) - 1)

        elif int(user_numb) == 3:
            print('What number of record you want to change?')
            reg_key = input()
            if not reg_key.isdigit():
                print('This is not number!')
                continue
            elif int(reg_key) > len(user_dict) or int(reg_key) <= 0:
                print('Your base doesnt have this number!')
                continue
            print('write value for your key:')
            value = input()
            if not value.isdigit():
                value = int(value)
            user_dict[int(reg_key) - 1] = value

        elif int(user_numb) == 4:
            work = False

        else:
            print('your input false, please write true number!')


def main():
    # print(ploscha_kola(123))
    # print(radius_in_ploscha(234))
    # print(perumetr_kola(345))
    # print(radius_in_per(456))
    # print(zodiack_search(2, 13))
    # print(reverse_mas([454, 656, 676, 878, 898, 1090, 1122, 1234, 1789]))
    # print_n_close()
    my_database()


if __name__ == "__main__":
    main()
