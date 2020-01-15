import random

import matplotlib.pyplot as plt


def f(x):
    return x**2


def f_derivative(x):
    return 2*x


def tangent(x, a, x1, y1):
    """
    기울기가 a이고 점(x1, y1)을 지나는 직선의 방정식
    y - y1 = a(x - x1)
    """
    return a * (x-x1) + y1


def difference_quotient(f, x, h):
    """함수 f의 도함수의 근사값"""
    return (f(x+h) - f(x)) / h


def move(x, direction, step=-0.1):
    """
    x좌표를 새로운 x로 이동
    direction : 접선의 기울기
    step > 0인 경우는 접선과 같은 방향으로 이동 -> 최소값찾기
    step < 0인 경우는 접선과 반대 방향으로 이동 -> 최대값찾기
    """
    return x + step * direction


if __name__ == '__main__':
    xs = [x/10 for x in range(-30, 31)]
    ys = [f(x) for x in xs]

    # x**2 그래프에서 x=-1에서의 접선을 그리기 위해서
    # 직선의 방정식 y=ax+b에서 기울기 a와 y절편 b를 찾아야함
    # 기울기 a는 x**2의 미분값으로 찾으면 되고
    # y절편은 (x1, f(x1))을 지나는 직선임을 이용해서 찾으면 됨

    a = f_derivative(-1)     # 접선의 기울기
    x1, y1 = -1, f(-1)       # x=-1에서 곡선과 접선이 만나는 점의 좌표
    tangents = [tangent(x, a, x1, y1) for x in xs]

    # 도함수의 근사값을 사용해서 x=-1에서의 기울기를 찾음
    # h의 값이 0에 가까울 수록 더 정확한 접선의 기울기가 됨
    h=1
    a2 = difference_quotient(f, x=-1, h=h)

    tangent_estimate = [tangent(x, a2, x1, y1) for x in xs]

    plt.plot(xs, ys)
    plt.plot(xs, tangents, label='actual')
    plt.plot(xs, tangent_estimate, label=f'estimate:{h}')
    plt.axhline(y=0, color='black')    # y=0의 보조선
    plt.axvline(x=0, color='black')    # x=0의 보조선
    plt.legend()
    plt.show()

    # 실제 기울기(actual)와 기울기 근사값(estimate) 비교
    xs = [x for x in range(-10,11)]
    actual = [f_derivative(x) for x in xs]
    estimate_1 = [difference_quotient(f, x, h=1) for x in xs]
    estimate_2 = [difference_quotient(f, x, h=0.1) for x in xs]

    plt.scatter(xs, actual, label='actual', marker='x')
    plt.scatter(xs, estimate_1, label='h=1', marker='+')
    plt.scatter(xs, estimate_2, label='h=0.1', marker='o')
    plt.legend()
    plt.show()

    # 경사하강법
    xs = [x/10 for x in range(-30, 31)]
    ys = [f(x) for x in xs]      # y=x**2 그래프의 y값들
    plt.plot(xs, ys, color='black')  # 2차방정식 곡선 그래프

    init_x = 2  # 최소값을 찾기 위해 시작할 x 좌표
    for _ in range(5):
        gradient = difference_quotient(f, init_x, h=0.01)        # x=init_x에서 접선의 기울기
        tangent_estimate = [tangent(x, gradient, init_x, f(init_x)) for x in xs]   # 접선을 그래프로 그리기
        plt.plot(xs, tangent_estimate, label=f'x={init_x}')
        init_x = move(init_x, gradient, step=-0.9)  # x 좌표를 새로운 좌표로 이동
    plt.legend()
    plt.ylim(bottom=-1)
    plt.show()

    # 임의의 점에서 시작해서 y=x**2의 최소값을 찾음
    random.seed(1128)
    init_x = random.randint(-10,10)    # 위험한 코드 -> 처음부터 random값으로 0이 나올 수 있음
    print(f'init_x = {init_x}')

    tolerance = 0.0000001
    count = 0
    while True: # 두 x좌표(move전, 후) 값 사이의 거리가 tolerance이하이면 반복문 종료
        count += 1  # 최소값을 몇번만에 찾았는지 알아보기 위해서 사용
        gradient = difference_quotient(f, init_x, h=0.001) # x 좌표에서의 접선의 기울기 계산
        next_x = move(init_x, gradient, step=-0.1) # 접선의 기울기를 이용해서 x좌표를 이동
        print(f'{count}: x={next_x}')
        if abs(next_x - init_x) < tolerance: # 이동전, 후 x값의 차이가 tolerance이하이면 종료
            break
        else:
            init_x = next_x



















