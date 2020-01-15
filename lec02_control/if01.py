num = int(input('>>> 정수를 입력하세요'))
if num > 0:
    print(f'num = {num}')

if num > 0:
    print('양수')
else:
    print('0 또는 음수')

print('프로그램 종료')

score = 85
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')
print('프로그램 종료')


num = int(input('>>> 정수를 입력하세요'))
if num % 2 == 0:
    if num % 4 == 0:
        print('4의 배수')
    else:
        print('4의 배수가 아닌 짝수')
else:
    print('홀수')
print('프로그램 종료')
