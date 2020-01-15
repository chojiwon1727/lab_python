import numpy as np


print('가위 바위 보 게임')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('------------------')
print('가위 바위 보 중 선택>>>')

user = int(input())

computer = np.random.randint(1,4)
print(computer)

if user == 1:
    if user == computer:
        print('비김')
    elif user < computer:
        print('짐')
    else:
        print('이김')
elif user == 2:
    if user == computer:
        print('비김')
    elif user < computer:
        print('짐')
    else:
        print('이김')
else:
    if user == computer:
        print('비김')
    elif computer == 1:
        print('짐')
    else:
        print('이김')

