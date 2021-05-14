# --lesson 6 class Mateush Vilen--

import json


def my_decorator(func):
    def wrapper():
        print("-----------------------------")
        func()
        print('-----------------------------')
    return wrapper()


class PersonalUserDatabase:
    user_dict = {}

    def __init__(self):
        with open('data_file.json') as read_file:
            self.user_dict = json.load(read_file)
            read_file.close()

    def start_work(self):
        print('Your personal database is work, you have this base:')
        print(self.user_dict)
        self.input_command_value()

    @my_decorator
    def input_command_value(self):
        print('if you want add record press 1')
        print('if you wand delete record press 2')
        print('if you wand edit value press 3')
        print('if you want edit key press 4')
        print('if you want exit press 5')
        user_value = input()
        if not user_value.isdigit():
            print('ERROR Your input false, please write number!')
        if int(user_value) == 1:
            self.add_record()
        if int(user_value) == 2:
            self.del_record()
        if int(user_value) == 3:
            self.edit_value()
        if int(user_value) == 4:
            self.edit_key()
        if int(user_value) == 5:
            raise SystemExit
        else:
            print('ERROR Your input false, please white true number!')

    def add_record(self):
        print('Write key of record:')
        key1 = input()
        print('Write value for your key:')
        value1 = input()
        if key1.isdigit():
            key1 = int(key1)
        if value1.isdigit():
            value1 = int(value1)
        self.user_dict.update({key1: value1})
        self.write_to_file()
        self.start_work()

    def del_record(self):
        print(self.user_dict)
        print('What number of record you want to delete?')
        del_key = input()
        if not del_key.isdigit():
            print('ERROR This is not correct number!')
            self.start_work()
        del_key = int(del_key)
        if del_key > len(self.user_dict) or del_key <= 0:
            print('ERROR Your base doesnt have this number!')
            self.start_work()
        user_list = list(self.user_dict)
        self.user_dict.pop(user_list[del_key - 1])
        self.write_to_file()
        self.start_work()

    def edit_value(self):
        print('What number of value you want to change?')
        reg_key = input()
        if not reg_key.isdigit():
            print('ERROR This is not number!')
            self.start_work()
        reg_key = int(reg_key)
        if reg_key > len(self.user_dict) or reg_key <= 0:
            print('ERROR Your base doesnt have this number!')
            self.start_work()
        print('Write new value:')
        value = input()
        if value.isdigit():
            value = int(value)
        user_list = list(self.user_dict)
        self.user_dict[user_list[reg_key - 1]] = value
        self.write_to_file()
        self.start_work()

    def edit_key(self):
        print('What number of key you want to change?')
        reg_key = input()
        if not reg_key.isdigit():
            print('ERROR This is not number!')
            self.start_work()
        reg_key = int(reg_key)
        if reg_key > len(self.user_dict) or reg_key <= 0:
            print('ERROR Your base doesnt have this number!')
            self.start_work()
        print('Write new text for your key:')
        value = input()
        if value.isdigit():
            value = int(value)
        user_list = list(self.user_dict)
        self.user_dict[value] = self.user_dict.pop(user_list[reg_key - 1])
        self.write_to_file()
        self.start_work()

    def write_to_file(self):
        with open("data_file.json", "w") as write_file:
            write_file.write(json.dumps(self.user_dict, sort_keys=True, indent=4))
            write_file.close()


def main():
    new_user_dict = PersonalUserDatabase()
    new_user_dict.start_work()
    # print(new_user_dict.user_dict)


if __name__ == "__main__":
    main()
