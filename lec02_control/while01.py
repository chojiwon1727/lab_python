# 1,2,3,...10출력

n = 1
while n <= 10:
    print(n, end=' ')
    n += 1
print()

n = 1
while n < 10:
    print(f'2 x {n} = {2 * n}')
    n += 1
print()

dan = 2
while dan < 10:
    n = 1
    while n < 10:
        print(f'{dan} x {n} = {dan*n}')
        n += 1
    dan += 1
    print('---------')
print()

dan = 2
while dan < 10:
    n = 1
    while n < 10:
        print(f'{dan} x {n} = {dan*n}')
        if dan == n:
            break
        n += 1
    dan += 1
    print('---------')
print()