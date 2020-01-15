import random
from collections import Counter

coin = ['H', 'T']
dice = [1,2,3,4,5,6]
trials = 10_000


def experiment(type, n, t):
    """
    :param type: 실험 타입(동전던지기, 주사위던지기, ...)
    :param n: 개수
    :param t: 실험 횟수
    :return: 리스트
    """
    cases = []     # 동전 던지기 실험 결과를 저장
    for _ in range(t):   # 실험 횟수만큼 반복
        case = []   # 각 실험의 결과를 저장
        for _ in range(n):  # 동전 개수만큼 반복
            rand = random.choice(type)   # 'H' 또는 'T'
            case.append(rand)     # 1회 실험 결과에 저장
        cases.append(tuple(case))      # 1회 실험이 끝날 때마다 각 결과 저장
    return cases


coin_exp = experiment(coin, 2, 10_000)
# print(coin_exp[0:10])

# 동전 던지기 실험 경우의 수
coin_event_counts = Counter(coin_exp)
print(coin_event_counts)
print()


def how_many_heads(x):
    counter = Counter(x)
    # print(counter)
    return counter['H']

num_of_cases = 0
for event, count in coin_event_counts.items():
    if how_many_heads(event) == 1:
        num_of_cases += count
print()
p_h1 = num_of_cases / trials
print('앞면이 1개인 경우 : ', p_h1)

num_of_cases = 0
for event, count in coin_event_counts.items():
    if event ==('H', 'H') or event == ('H', 'T'):
        num_of_cases += count
p_first_h = num_of_cases / trials
print('첫번째 동전이 앞면일 경우 : ', p_first_h)

num_of_cases = 0
for event, count in coin_event_counts.items():
    if how_many_heads(event) == 1 or how_many_heads(event) == 2:
        num_of_cases += count
p = num_of_cases / trials
print('적어도 한개의 동전이 앞면일 경우 : ', p)

num_of_cases = 0
for event, count in coin_event_counts.items():
    if how_many_heads(event) == 0:
        num_of_cases += count
p = num_of_cases / trials
print('적어도 한개의 동전이 앞면일 경우(여사건사용) : ', 1-p)
print('==================================')

coin2 = [0,1]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2):
        if 1 == random.choice(coin2):
            num_of_heads += 1
    cases.append(num_of_heads)
# print(cases[0:10])
coin_event_counts = Counter(cases)
print(coin_event_counts[0] / trials)
print(coin_event_counts[1] / trials)
print(coin_event_counts[2] / trials)
print('==================================')

# 주사위 2개를 던진 경우 합이 8일 확률과 적어도 하나가 짝수일 확률
dice_exp = experiment(dice, 2, trials)
# print(dice_exp[0:10])
dice_event_count = Counter(dice_exp)
# print(len(dice_event_count))
# print(dice_event_count)
# print(dice_event_count.keys())

num_of_cases = 0
for key, value in dice_event_count.items():
    if sum(key) == 8:
        num_of_cases += value
p_sum8 = num_of_cases / trials
print(f'주사위 2개를 던진 경우 합이 8일 확률 : {p_sum8}')

# num_of_cases = 0
# for key, value in dice_event_count.items():
#     if key == (2, 6) or key == (3,5) or key == (4,4) or key == (5,3) or key == (6,2):
#         num_of_cases += value
# p_sum_8 = num_of_cases / trials
# print(f'주사위 2개를 던진 경우 합이 8일 확률 : {p_sum_8}')

num_of_cases = 0
for key, value in dice_event_count.items():
    if key[0] % 2 == 0 or key[1] % 2 == 0:
        num_of_cases += value
p_po = num_of_cases / trials
print(f'주사위 2개를 던진 경우 적어도 하나가 짝수일 확률 : {p_po}')

# num_of_cases = 0
# for key, value in dice_event_count.items():
#     if key == (1,1) or key == (1,3) or key == (1,5) \
#         or key == (3,1) or key == (3,3) or key == (3,5) \
#         or key == (5,1) or key == (5,3) or key == (5,5):
#         num_of_cases += value
# p_po = 1- (num_of_cases / trials)
# print(f'주사위 2개를 던진 경우 적어도 하나가 짝수일 확률 : {p_po}')














