import random

coin = ['H', 'T']
dice = [1,2,3,4,5,6]
# print(random.choice(dice))

# 동전 1개를 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2임을 증명

H = []
T = []
for i in range(10000):
    random_coin = random.choice(coin)
    if random_coin == 'H':
        H.append(random_coin)
    else:
        T.append(random_coin)

count_H = len(H)
count_T = len(T)
prop_H = count_H / 10000
prop_T = count_T / 10000
print(f'Count H : {count_H}, Prop H : {prop_H}')
print(f'Count T : {count_T}, Prop T : {prop_T}')


# 동전 2개를 10_000번 던지는 실험
trial = 10_000
first = []
second = []

for i in range(trial):
    random_coin1 = random.choice(coin)
    first.append(random_coin1)
for j in range(trial):
    random_coin2 = random.choice(coin)
    second.append(random_coin2)

HT = []
TH = []
for i, j in zip(first, second):
    if i == "H" and j == 'T':
        HT.append(i)
    elif i == 'T' and j == 'H':
        TH.append(i)
HTTH = HT + TH
print(f'HT, TH - count : {len(HTTH)}, prop : {len(HTTH)/trial}')

HH = []
for i, j in zip(first, second):
    if  i == 'H' and j == 'H':
        HH.append(i)
HHHT = HH + HT
print(f'HH, HT - count : {len(HHHT)}, prop : {len(HHHT)/trial}')

HHHTTH = HT + HH + TH
print(f'HH, HT, TH - count : {len(HHHTTH)}, prop : {len(HHHTTH)/trial}')


first = []
second = []
third = []
for i in range(trial):
    random_coin1 = random.choice(coin)
    first.append(random_coin1)
for j in range(trial):
    random_coin2 = random.choice(coin)
    second.append(random_coin2)
for z in range(trial):
    random_coin3 = random.choice(coin)
    third.append(random_coin3)

HTT = []
THT = []
TTH = []
for i, j, z in zip(first, second, third):
    if i == 'H' and j == 'T' and z == 'T':
        HTT.append(i)
    elif i == 'T' and j == 'H' and z == 'T':
        THT.append(i)
    elif i == 'T' and j == 'T' and z == 'H':
        TTH.append(i)

coin3 = HTT + THT + TTH
print(f'HTT, THT, TTH - count : {len(coin3)}, prop : {len(coin3)/trial}')
