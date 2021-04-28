n = 11
m = 33
dash = '-'
symbol = '.|.'
center_n = (n - 3) / 2
center_m = (m - 3) / 2
x = 0
print(center_m)
while center_m >= 1:
    print(dash*int(center_m), end='')
    print(symbol, end='')
    print(symbol*x, end='')
    print(dash*int(center_m))
    center_m -= 3
    x += 2
welcome = (m - 3) / 2
print((int(welcome)- 2)*dash , end='')
print('WELCOME', end='')
print((int(welcome)- 2)*dash)
center_m += 3
x -= 2
while center_m <= welcome:
    print(dash*int(center_m), end='')
    print(symbol, end='')
    print(symbol*x, end='')
    print(dash*int(center_m))
    center_m += 3
    x -= 2
