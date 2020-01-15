import numpy as np
from math import sqrt
scores = []

# 1) 난수생성해서 리스트에 저장하기
for i in range(10):
    x = np.random.randint(0, 101)
    scores.append(x)
print(scores)

# --> for 구문에서 두줄로 쓰지 않고 scores.append(np.random.randint(0,101))로 써도 됨
# for 구문에서 i 변수는 문법상에서만 필요한 변수이기 때문에 사용하지는 않음
# 파이썬에서는 i 변수를 사용하지 않고 _ 로 사용해도 허용함

# 2) 총점 계산
total = 0
for score in scores:
    total += score
print(f'총점 = {total}')

# total += score는 total = total + score의 의미
# --> 함수만 사용해도 됨 print(f'총점 = {sum(scores)}')

# 3) 평균 계산
v_avg = total / len(scores)
print(f'평균 : {v_avg}')

# --> np의 함수 사용 가능 print(f'평균 : {np.mean(scores)}')

# 4) 표준편차 계산
sum_of_squares = 0
for score in scores:
    sum_of_squares += (score - v_avg) ** 2

sd = sqrt(sum_of_squares / len(scores))
print(f'표준편차 = {sd}')

# --> np의 함수 사용 가능 print(f'표준편차 = {np.std(scores}')

# 5) 최대값, 최소값
max_score = scores[0]
for score in scores:
    if max_score < score:
        max_score = score
print(f'최대값 : {max_score}')

# 함수 사용 가능 print(f'최대값 = {max(scores)}')

# 6) 최소값
min_score = scores[0]
for score in scores:
    if min_score > score:
        min_score = score
print(f'최소값 : {min_score}')
# 함수 사용 가능 print(f'최소값 = {min(scores)}')


# 5), 6) 한번에 작성 가능
max_score = scores[0]
min_score = scores[0]

for score in scores:
    if max_score < score:
        max_score = score
    if min_score > score:
        min_score = score
print(f'최대값 : {max_score}', f'최소값 : {min_score}')


sorted_scores = sorted(scores)
print(sorted_scores)

