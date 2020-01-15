"""
선형회귀에서 잔차의 최소를 구하는 경사하강법
"""
import random

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step


def linear_gradient(x, y, theta):
    """
    특정 데이터(x, y)에서 기울기와 y절편에 대한
    편미분 벡터를 리턴하는 함수

    :param x: 실제 데이터
    :param y: 실제 데이터
    :param theta: 성분 2개를 가지는 벡터[theta1, theta2]=[기울기, y절편]
    :return: 벡터
    """
    slope, intersect = theta
    y_hat = slope * x + intersect   # 예상값
    error = y_hat - y    # 오차
    gradient = [error * x, error]   # error**2을 최소화하는 slope과 intersect를 찾는 문제
    return gradient


def minibatches(dataset, batch_size, shuffle=True):
    # 데이터 세트를 무작위로 섞음
    if shuffle:
        random.shuffle(dataset)

    # 배치 시작 인덱스: 0, batch_size, 2*batch_size, ...
    batch_starts = [s for s in range(0, len(dataset), batch_size)]
    # [[ds[0], ..., ds[size-1]], [ds[size], ... ds[2size-1]], ...]
    mini = [dataset[s:s+batch_size] for s in batch_starts]
    return mini


# 모든 점들이 y=20*x+5에 있음-> 과연 기울기 20, 절편5를 찾을 수 있을까?

dataset = [(x, 20 * x + 5)for x in range(-50,51)]

if __name__ == '__main__':
    print('\n=== 확률적 경사 하강법 ===')
    theta = [1, 1]  # 임의의 파라미터 초기값[기울기, y절편] : y = x + 1
    step = 0.001  # 파라미터의 값을 변경할 때 사용할 가중치(학습률)

    for epoch in range(200):  # 임의의 횟수(epoch)만큼 반복
        random.shuffle(dataset)  # data set을 랜덤하게 섞음
        for x, y in dataset: # 각각의 epoch마다 샘플(x, y) 추출해서
            gradient = linear_gradient(x, y, theta)   # 각 점에서 gradient 계산
            theta = gradient_step(theta, gradient, step=-step) # 파라미터 theta변경(move)
        if (epoch + 1) % 10 == 0:       # 200번 epoch하고 있는데, 10번마다만 print
            print(f'{epoch}: {theta}')

    print('\n=== 배치 경사 하강법 ===')
    step = 0.001
    theta = [1, 1]  # 임의의 값으로 [기울기, 절편] 설정
    for epoch in range(5000):
        # 모든 샘플에서의 gradient를 계산
        gradients = [linear_gradient(x, y, theta)
                     for x, y in dataset]
        # gradients의 평균을 계산
        gradient = vector_mean(gradients)
        # 파라미터 theta(기울기, 절편)을 변경
        theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')

    print('\n=== 미니 배치 경사 하강법 ===')
    theta = [1, 1]  # 임의의 파라미터 시작값
    step = 0.001  # 학습률
    for epoch in range(1000):
        mini_batches = minibatches(dataset, 20, True)
        for batch in mini_batches:
            gradients = [linear_gradient(x, y, theta)
                         for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')