import random
from collections import Counter

trials = 10_000
ch = ['D', 'S']

def experiment(type, n, t):
    """
    :param type: 실험 타입(동전던지기, 주사위던지기, ...)
    :param n: 개수
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []
    for _ in range(t):
        case = []
        for _ in range(n):
            rand = random.choice(type)
            case.append(rand)
        cases.append(tuple(case))
    return cases


ch_exp = experiment(ch, 2, trials)
ch_count = Counter(ch_exp)
print(ch_count)

num_of_case = 0
for key, value in ch_count.items():
    if key[0] == 'D':
        num_of_case += value
p_first_D = num_of_case / trials
print(f'p(A) : {p_first_D}')

num_of_case = 0
for key, value in ch_count.items():
    if key[1] == 'S':
        num_of_case += value
p_second_S = num_of_case / trials
print(f'p(B) : {p_second_S}')

num_of_case = 0
for key, value in ch_count.items():
    if key[0] == 'D' and key[1] == 'D':
        num_of_case += value
p_both_D = num_of_case / trials
print(f'p(C) : {p_both_D}')

num_of_case = 0
for key, value in ch_count.items():
    if key[0] == 'D' and key[1] == 'S':
        num_of_case += value
p_A_B = num_of_case / trials
print(f'P(A,B) : {p_A_B}')

num_of_case = 0
for key, value in ch_count.items():
    if key[0] == 'D' and key[1] == 'D':
        num_of_case += value
p_A_C = num_of_case / trials
print(f'P(A,C) : {p_A_C}')


A_B = p_first_D * p_second_S
A_C = p_first_D * p_both_D

print(f'P(A,B) 와 P(A)*P(B)는 같다 -->  {A_B} == {p_A_B}')
print(f'P(A,C) 와 P(A)*P(C)는 다르다 -->  {A_C} != {p_A_C}')




