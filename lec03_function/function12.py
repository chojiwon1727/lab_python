"""
함수에서 return의 의미
1) 함수 종료
2) 함수를 호출한 곳에 값을 반환

yield : 반복문 안에서만 함수의 결과를 반환할 때
"""

def test():
    x = 0
    while x < 4:
        return x         # return은 이 위치에서 함수를 종료하기 때문에 밑에 있는 x += 1은 실행될 수 없음
        x += 1

for i in range(4):
    print(test())

def four():
    x = 0
    while x < 4:
        yield x
        x += 1

for i in four():
    print(i)

print(four())

print(range(1, 4))

def my_range(start = 0, end = 1):
    x = start
    while x < end:
        yield x
        x += 1

print(my_range(1,5))

for i in my_range(1,5):
    print(i, end=' ')

