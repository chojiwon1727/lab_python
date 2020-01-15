"""
편미분(Partial Differentiation)을 이용한 경사 하강법
"""
import random

from scratch04.ex01 import scalar_multiply, add, distance


def partial_difference_quotient(f, v, i, h=0.001):
    """
    기울기 구하는 함수
    (f([x1, ..., xi+h, ..., xn]) - f([x1, ..., xi, ..., xn])) / h

    :param f:  f(vector) = float인 함수
    :param v: 기울기(gradient)를 계산할 위치 - 벡터(리스트)
    :param i: 기울기(gradient)를 계산할 성분의 인덱스 - 정수
    :param h: i번째 성분의 변화량
    :return: 편미분 결과 -> i번째 성분 방향의 gradient
    """

    w = [v_j + (h if i == j else 0) for j, v_j in enumerate(v)]

    # w=[]
    # for j, v_j in enumerate(v):
    #     if j == i:
    #         v_j += h
    #     w.append(v_j)
    return (f(w)-f(v))/h


def estimate_gradient(f, v, h=0.001):
    """
    [df/dx1, df/dx2, ..., df/dxi, ..., df/dxn]
    도함수들을 리스트로 만들어주는 함수

    :param f: f(vector) = float 함수
    :param v: 기울기를 구하려는 점의 좌표 [x1, ..., xn]
    :param h: 증분(increment)
    :return: 모든 성분의 gradient들로 이루어진 벡터(리스트)
    """
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]


def gradient_step(v, gradient, step=-0.1):
    """
    [vi + step * df/dvi]
    --> 앞에서 만든 move 함수와 동일한 기능

    :param v: 이동 전 점의 위치
    :param gradient: 점(v)에서의 그래프
    :param step: 이동시키는 가중치(학습률)
    :return: 기울기의 방향으로 이동한 새로운 점의 위치
    """
    increment = scalar_multiply(step, gradient)
    return add(v, increment)


if __name__ == '__main__':
    # f([x1, x2]) = x1**2 + x2**2 그래프에서 경사하강법 적용하기-최소값(0,0)
    # g([x1, x2]) = (x1-1)**2 + (x2+1)**2 - 최소값(1,-1)

    def f(v):
        """v = [x1, x2] 가정   -> v는 리스트"""
        return v[0] ** 2 + v[1] ** 2

    random.seed(1129)
    init_v = [random.randint(-10, 10), random.randint(-10, 10)]  # 기울기를 계산할 최초의(x1, y1)좌표
    print(f'init_v = {init_v}')

    tolerance = 0.000001   # 반복문을 종료할 임계값
    count = 0
    while True:
        count += 1
        gradient = estimate_gradient(f, init_v) # 선택한 좌표(x1, y1)에서 기울기 계산
        next_v = gradient_step(init_v, gradient, step=-0.5) # 다음 좌표로 점 이동
        print(f'{count}: next_v = {next_v}')
        if distance(next_v, init_v) < tolerance: # 좌표의 이동거리 계산
            break
        else:
            init_v = next_v
    print()

    def g(v):
        return (v[0]-1)**2 + (v[1]+1)**2

    random.seed(1129)
    init_v = [random.randint(-10, 10), random.randint(-10, 10)]  # 기울기를 계산할 최초의(x1, y1)좌표
    print(f'init_v = {init_v}')

    tolerance = 0.000001  # 반복문을 종료할 임계값
    count = 0
    while True:
        count += 1
        gradient = estimate_gradient(g, init_v)  # 선택한 좌표(x1, y1)에서 기울기 계산
        next_v = gradient_step(init_v, gradient, step=-0.5)  # 다음 좌표로 점 이동
        print(f'{count}: next_v = {next_v}')
        if distance(next_v, init_v) < tolerance:  # 좌표의 이동거리 계산
            break
        else:
            init_v = next_v




























