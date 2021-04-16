import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

popular_auto = [
    'Audi',
    'Honda',
    'Suzuki',
    'Nissan',
    'Aston Martin',
    'Mitsubishi',
    'Renault',
    'Hundai',
    'Daewoo',
    'Fiat',
    'Ford',
    'Mazda',
    'Geely',
    'Mersedes'
]
gigant_company = ['Amazon', 'Google', 'Apple', 'Facebook']
my_list = ['Vilen', 'Mateush', 1990, ['Doom', 'Quake', 'Conter strike', 'Half life'], 'Aquarius']

print(popular_auto)
print(gigant_company)
print(my_list)

print('----- sorted lists -----')
print(sorted(popular_auto))
print(sorted(gigant_company))
# print(sorted(my_list))

print('----- min -----')
print(min(popular_auto))
print(min(gigant_company))
# print(min(my_list))

print('----- max -----')
print(max(popular_auto))
print(max(gigant_company))
# print(max(my_list))

print('----- pop -----')
return_value = popular_auto.pop(0)
print(return_value)
return_value = gigant_company.pop(1)
print(return_value)
return_value = my_list.pop(3)
print(return_value)

print('----- for print elements -----')
for elem in popular_auto:
    print(elem)
for elem in gigant_company:
    print(elem)
for elem in my_list:
    print(elem)

print('----- for and random numbers -----')
mass_for = []
mass_rand = []
for numb in range(0, 10):
    mass_for.append('for')
    mass_rand.append(random.randint(0, 99999))
print(mass_for)
print(mass_rand)

print('----- user input data 5 times -----')
mass_user = []
for numb in range(0, 5):
    mass_user.append(input())

for numb in enumerate(mass_user):
    print(numb)

# while True:
#     print('cycle work4')

password = '0'
while password != '1':
    password = input()
