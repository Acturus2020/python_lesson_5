abc = 'abcdefghijklmnopqrstuvwxyz'
SIZE = 10
temp_size = SIZE
temp_size2 = SIZE
back = False
n = 1
n2 = SIZE
for row in range(1, SIZE):
    temp_size -= 1
    for dot in range(1, temp_size+1):
        print('--', end='')
    change = SIZE-1
    change2 = SIZE-1
    for let2 in range(1, n+1):
        print(abc[change], end='')
        print('-', end='')
        change -= 1
    n+=1
    n2-=1
    change2 = n2+1
    if temp_size < SIZE-1:
        for let2 in range(1, n-1):

            print(abc[change2], end='')
            print('-', end='')
            change2 += 1

    for dot in range(1, temp_size+temp_size):
        print('-', end='')

    print('')

for let in range(1, SIZE+SIZE):
    if back:
        print(abc[temp_size2-1], end='')
        temp_size2 +=1
    else:
        print(abc[temp_size2-1], end='')
        temp_size2 -= 1
    if let == SIZE-1:
        back = True
    if let != (SIZE+SIZE-1):
        print('-', end='')
print('')

temp_size = 0
temp_size2 = SIZE
n = SIZE
n2 = 1
for row in range(1, SIZE):
    temp_size += 1
    for dot in range(1, temp_size+1):
        print('--', end='')
    change = SIZE-1
    for let2 in range(1, n):
        print(abc[change], end='')
        print('-', end='')
        change -= 1
    n -= 1

    change2 = n2+1
    n2 += 1
    if temp_size < SIZE - 1:
        for let2 in range(1, n):
            print(abc[change2], end='')
            print('-', end='')
            change2 += 1

    for dot in range(1, temp_size+temp_size):
        print('-', end='')
    print('')
