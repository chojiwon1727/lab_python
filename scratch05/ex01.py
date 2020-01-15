import math
from collections import Counter
from scratch04.ex01 import dot


def mean(x):
    """
    리스트 x의 모든 아이템들의 평균을 계산해서 리턴

    :param x: 원소가 n개인 1차원 list
    :return: 평균
    """
    sum = 0
    for i in x:
        sum += i
    return  sum / len(x)


def median(x):
    """
    리스트 x를 정렬했을 때 중앙에 있는 값을 찾아서 리턴
    리스트 x의 개수가 홀수이면 중앙값 리턴,
    리스트 x의 개수가 짝수이면 중앙에 있는 두 값의 평균 리턴

    :param x: 원소가 n개인 1차원 list
    :return: 중앙값
    """
    sort_x = sorted(x)
    n = len(sort_x)
    mid_point = n//2

    if n%2 == 1:       # n이 홀수이면
        median_value = sort_x[mid_point]

    elif n%2 == 0:     # n이 짝수이면
        median_value = (sort_x[mid_point] + sort_x[mid_point-1]) / 2

    return median_value


def quantile(x, p):
    """
    리스트 x의 p분위에 속하는 값을 찾아서 리턴

    :param x: 원소가 n개인 1차원 list
    :param p: 0 ~ 1.0사이의 값(0.5 = 50%값 리턴)
    :return: 해당 분위수 값
    """
    n = len(x)
    p_index = int(p * n)
    return sorted(x)[p_index]


def mode(x):
    """
    리스트에서 가장 많이 나타나는 값을 리턴
    만약 최빈값이 여러개인 경우 최빈값들의 리스트 리턴
    from collection import Counter

    :param x: 원소가 n개인 1차원 리스트
    :return: 최빈값들의 리스트
    """
    counts = Counter(x)         # dict
    max_count = max(counts.values())       # list
    # freq = []
    # for key, value in counts.items():
    #     if value == max_count:
    #         freq.append(key)
    # return freq
    return [key for key, value in counts.items() if value == max_count]


def x_range(x):
    """
    리스트의 범위를 리턴
    :param x: 원소가 n개인 1차원 리스트
    :return: 범위
    """
    return max(x) - min(x)


def de_mean(x):
    """
    편차들(데이터 - 평균)의 리스트
    :param x: 원소가 n개인 1차원 리스트
    :return: 편차들의 리스트
    """
    mu = mean(x)
    return [x_i - mu for x_i in x]


def variance(x):
    """
    (x1 - mean)**2 + (x2 - mean)***2 + ... + (xn - mean)**2 / n-1
    :param x: 원소가 n개인 1차원 리스트
    :return: 분산
    """
    # x_mean = mean(x)
    # sum = 0
    # for i in x:
    #     sum += (i - x_mean)**2
    # return sum / (len(x)-1)

    # demean = de_mean(x)
    # sum = 0
    # for i in demean:
    #     sum += i**2
    # return sum / (len(x)-1)

    demean = de_mean(x)
    return dot(demean, demean) / (len(x)-1)


def standard_deviation(x):
    """
    sqrt(variance)
    :param x: 원소가 n개인 1차원 리스트
    :return: 표준편차
    """
    return math.sqrt(variance(x))


def covariance(x,y):
    """
    공분산
    Cov = sum((x_i - x_bar)(y_i - y_bar)) / (n-1)

    :param x: 원소가 n개인 1차원 리스트
    :param y: 원소가 n개인 1차원 리스트
    :return: 공분산
    """
    # if len(x) != len(y):
    #     raise ValueError('x와 y의 길이는 같아야 합니다!')
    # de_x = de_mean(x)
    # de_y = de_mean(y)
    # result = []
    # for i, j in zip(de_x, de_y):
    #     result.append(i*j)
    # return sum(result) / (len(x) - 1)

    # if len(x) != len(y):
    #     raise ValueError('x와 y의 길이는 같아야 합니다!')
    # de_x = de_mean(x)
    # de_y = de_mean(y)
    # sum = 0
    # for i, j in zip(de_x, de_y):
    #     sum += (i*j)
    # return sum / (len(x) - 1)

    # x_bar = mean(x)
    # y_bar = mean(y)
    # x_dev = [x_i - x_bar for x_i in x]
    # y_dev = [y_i - y_bar for y_i in y]
    # sum_of_sq = 0
    # for xd, yd in zip(x_dev, y_dev):
    #     sum_of_sq += xd * yd
    # return sum_of_sq / (len(x) - 1)

    x_bar = mean(x)
    y_bar = mean(y)
    x_dev = [x_i - x_bar for x_i in x]
    y_dev = [y_i - y_bar for y_i in y]
    sum_of_dev = dot(x_dev, y_dev)
    return sum_of_dev / (len(x) - 1)


def correlation(x,y):
    """
    상관계수
    Corr = Cov(x,y) / (sd(x)*sd(y))
    :param x: 원소가 n개인 1차원 리스트
    :param y: 원소가 n개인 1차원 리스트
    :return: 상관계수
    """
    if standard_deviation(x) != 0 and standard_deviation(y) != 0:
       corr = covariance(x, y) / (standard_deviation(x)*standard_deviation(y))
    else:
        corr = 0
    return corr


if __name__ == '__main__':
    A = [10,10,10,20,20,30,30,40,40,40]
    B = [90,70,80,20,30,10,20,20,40,40]
    print('mean = ', mean(A))
    print('median = ', median(A))
    print('quantile = ', quantile(A, 0.1))
    print('mode = ', mode(A))
    print('Range = ', x_range(A))
    print('variance = ', variance(A))
    print('standard deviation = ', standard_deviation(A))
    print('Covariance = ', covariance(A,B))
    print('correlation = ', correlation(A, B))


