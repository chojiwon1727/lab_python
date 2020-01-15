import math
import matplotlib.pyplot as plt
import numpy as np


def odds(p):
    """ 일어날 확률과 일어나지 않을 확률의 비율(성공확률 / 실패확률) """
    return p / (1-p)


def log_adds(p):
    """ odds에 log를 취한 값 """
    return math.log(odds(p))


def sigmoid(t):
    """ logistic 함수 : log_odds(odds에 log를 취한 값)를 알고 있을 때, 성공 확률 p를 계산"""
    return 1 / (1 + math.exp(-t))


if __name__ == '__main__':
    p = 0.8
    print(f'p = {p}, odds(p) = {odds(p)}, log_odds(p) = {log_adds(p)}')

    t = 1.39
    probability = sigmoid(t)
    print(f'probability = {probability}')

    # odds 그래프
    xs = np.linspace(0.01, 0.99, 100)     # 0~1사이 구간을 100개로 나눠서 100개의 점을 구함
    # print(xs)
    ys = [odds(x) for x in xs]
    plt.plot(xs, ys)
    plt.ylim(bottom=0.0, top=10.0)
    for i in range(1,5):
        plt.axhline(y = (2*i), color='0.5')
        plt.axvline(x=(0.2*i), color='0.5')
    plt.title('odds')
    plt.show()

    # log_odds 그래프
    ys = [log_adds(x) for x in xs]
    plt.plot(xs, ys)
    plt.axhline(color='0.5')
    plt.axvline(color='0.5')
    plt.axvline(x=0.5, color='0.5')
    plt.axvline(x=1.0, color='0.5')
    plt.title('log odds')
    plt.show()

    # sigmoid 그래프
    xs = np.linspace(-10, 10, 100)
    ys = [sigmoid(x) for x in xs]
    plt.plot(xs, ys)
    plt.axvline(color='0.5')
    plt.axhline(y=0.5, color='0.5')
    plt.axhline(y=1.0, color='0.5')
    plt.title('Logistic(sigmoid)')
    plt.show()