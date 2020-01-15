import numpy as np
"""
list comprehension
"""

numbers = [1,2,3,4,5]

numbers2 = []
for i in range(1,6):
    numbers2.append(i)
print(numbers2)

numbers3 = [n for n in range(1,6)]
print(numbers3)

# 2,4,6,8,10 저장
even = [2*n for n in range(1,6)]
print(even)

#1,4,9,16,25 저장
squ = [n**2 for n in range(1,6)]
print(squ)

# 랜덤넘버 10개 저장

ran = [np.random.randint(0,101) for _ in range(10)]
print(ran)

even2 = []
for n in range(1,11):
    if n % 2 == 0:
        even2.append(n)
print(even2)

even3 = [n for n in range(1,11) if n % 2 == 0]
print(even3)

# 주사위 2개를 던졌을 때 경우의 수
dice1 = []
for x in range(1,7):
    for y in range(1,7):
        dice1.append((x,y))
print(dice1)

dice2 = [(x, y) for x in range(1,7) for y in range(1,7)]
print(dice2)

# 주사위 2개를 던졌을 때 x >= y 만 저장
dice3 = []
for x in range(1,7):
    for y in range(1,7):
        if x >= y:
            dice3.append((x,y))
print(dice3)


dice4 = [(x,y) for x in range(1,7) for y in range(1,7) if x >= y]
print(dice4)

# 시험점수(0~100) 10개를 가지는 리스트
scores = [np.random.randint(0,101) for _ in range(10)]
print(scores)

# 평균보다 높은 점수들의 리스트
mean = np.mean(scores)
above_mean = []
for s in scores:
    if s > mean:
        above_mean.append(s)
print(above_mean)

above_mean2 = [s for s in scores if s > mean]
print(above_mean2)