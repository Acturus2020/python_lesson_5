# lesson 4 Mateush Vilen

my_information = {
    'name': 'Vilen',
    'last_name': 'Mateush',
    'how_old': 31,
    'born_town': 'Khmelniysky'
}

dict_test = {key:  key**2 for key in range(7)}
print('dict_test: ', dict_test)

elem_dict = 0
elem_dict = input('input number of elements:')
user_input_dict = {}
for key in range(0, int(elem_dict)):
    key = input('dict key: ')
    user_input_dict[key] = input('dict value:')
print(user_input_dict)

del_key = 0
del_key = input('input key for remove:')
dict_test.pop(int(del_key))
print(dict_test)

list_test = [elem for elem in range(5)]
print(list_test)
try:
    print(list_test[5])
except IndexError as message:
    print('list index out of range')

try:
    print(dict_test[7])
except KeyError as message:
    dict_test[7] = 'KeyError: 7'
print(dict_test)


# ------------My database------------:
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
        key = input()
        print('write value for your key:')
        value = input()
        if key.isdigit() == True:
            key = int(key)
        if value.isdigit() == True:
            value = int(value)
        user_dict.update({key: value})
    elif int(user_numb) == 2:
        print(user_dict)
        print('what number of record you want to delete?')
        del_key = input()
        if del_key.isdigit() == False:
            print('This is not correct number!')
            continue
        elif int(del_key) > len(user_dict) or int(del_key) <= 0:
            print('Your base doesnot have this number!')
            continue
        user_dict.pop(int(del_key)+1)
    elif int(user_numb) == 3:
        print('What number of record you want to change?')
        reg_key = input()
        if reg_key.isdigit() == False:
            print('This is not number!')
            continue
        elif int(reg_key) > len(user_dict) or int(reg_key) <= 0:
            print('Your base doesnt have this number!')
            continue
        print('write value for your key:')
        value = input()
        if value.isdigit() == True:
            value = int(value)
        user_dict[int(reg_key)-1] = value
    elif int(user_numb) == 4:
        work = False
    else:
        print('your input false, please write true number!')
