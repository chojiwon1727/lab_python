"""
중심극한정리(Central Limit Theorem)
모집단이 어떤 분포이든 상관없이 표본의 크기가 충분히 크다면
가능한 모든 표본들의 평균은 모평균 주위에서 정규분포를 따름
만약 모집단의 평균이 mu이고 표준편차가 sigma인 정규분포를 따른다면
표본 평균의 분포는 평균이  mu이고 분산이 sigma/sqrt(n)인 정규분포가 됨(단, n은 충분히 커야 함)

베르누이 확률 변수(Bernoulli random variable) : 어떤 시행의 결과가 ‘성공’, ‘실패’ 중 하나로
나타나고, 성공의 확률이 p, 실패의 확률이 1-p라 할 때 그 결과가 성공이면 확률 변수는 1을 갖고,
결과가 실패면 확률변수는 0인 확률변수 x
베르누이 확률 질량 함수(PMF : Probability Mass Function)
: pmf(x) = p if x = 1, 1-p if x = o
             = (p ** x) ((1 - p) ** (1 - x))
이항 확률 변수(binomial random variable)
: n개의 독립적인 베르누이 확률 변수들을 더한 것

※ 예시
▷ 베르누이 확률 변수 -> 동전 한 개를 던질 때 앞면의 수
▷ 이항 확률 변수 -> 동전 한 개를 n번 던질 때 앞면의 수

▶ 연속분포가 아니기 때문에 개수를 세어야 하는데, 그 개수가 커지면 커질수록 정규분포에
     가까워짐!(중심극한정리)
▷ 베르누이 확률 변수의 기대값 ->  평균 : p, 표준편차 :  sqrt(p(1-p))
▷ 중심극한정리 : n이 적당히 크다면, 이항 확률 변수는 대략 평균이 np이고, 표준편차가
                 sqrt(np(1-p))인 정규분포의 확률변수와 같음

▶ 표본(sample)의 평균(np)과 분산(p(1-p))을 알아내면, 모집단(population)의 평균(n)과
분산(p(1-p))를 예측할 수 있음!!
"""
import random
from collections import Counter
from math import sqrt

import matplotlib.pyplot as plt

from scratch06.ex06 import normal_cdf, normal_pdf


def bernoulli_trial(p):
    """베르누이 확률 변수 1 또는 0을 확률 p에 따라서 리턴해주는 함수"""
    x = random.random()   # random() : 0이상 1미만의 난수 리턴
    return 1 if x < p else 0


def binomial(n, p):
    """1이 나올 확률이 p인 베르누이 시행을 n번 했을 때 1이 나올 횟수를 리턴하는 함수"""
    s = 0
    for _ in range(n):
        s += bernoulli_trial(p)
    return s


if __name__ == '__main__':
    trials = 10_000
    n = 30
    p = 0.5
    data = [binomial(n, p) for _ in range(trials)]
    print(data[0:10])
    # 이항 확률 변수와 그에 따른 확률값 그리기
    histogram = Counter(data)
    x_bar = [key for key in histogram.keys()]
    y_bar = [value/trials for value in histogram.values()]
    plt.bar(x_bar, y_bar, color='grey')

    # 이항 확률 변수의 정규분포 근사
    mu = n*p
    sigma = sqrt(n*p*(1-p))
    x_line = range(min(data), max(data) + 1)
    y_line = [normal_pdf(x, mu, sigma) for x in x_line]
    plt.plot(x_line, y_line)
    plt.show()



