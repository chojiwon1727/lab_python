for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan} x {n} = {dan * n}')
    print('----------------------------')


for dan in range(2,10):
    for n in range(1,10):
        if dan >= n:
            print(f'{dan} x {n} = {dan * n}')
    print('-----------')


for dan in range(2,10):
    for n in range(1,10):
        print(f'{dan} x {n} = {dan * n}')
        if dan == n:
            break
    print('-----------')

for i in range(1,10):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(1,10):
    if i == 5:
        continue
    print(i, end=' ')
print()