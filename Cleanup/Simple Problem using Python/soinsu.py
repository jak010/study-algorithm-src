Number = int(input("Input Number : "))
d = 2

while d <= Number:
    if Number % d == 0:
        print(d, '', end='')
        Number = Number / d
    else:
        d = d + 1

print('\n')
