"""gradient descent 연습"""
import matplotlib.pyplot as plt
import scratch08.ex01 as ex01


def g(x):
    """y = (1/3)x**3 - x"""
    return x**3 / 3-x


if __name__ =='__main__':
    xs = [x/10 for x in range(-30,30)]
    ys = [g(x) for x in xs]
    plt.plot(xs, ys)
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    print('Local 최소값')
    init_x = 2
    count = 0
    tolerance = 0.0001
    while True:
        count += 1
        gradient = ex01.difference_quotient(g, init_x, h=0.001)
        next_x = ex01.move(init_x, gradient, step=-0.5)
        print(f'{count}: x={next_x}')
        if abs(next_x - init_x) < tolerance:
            break
        else:
            init_x = next_x

    print()
    print('Local 최대값')
    init_x = -2
    count = 0
    while True:
        count += 1
        gradient = ex01.difference_quotient(g, init_x, h=0.001)
        next_x = ex01.move(init_x, gradient, step=0.5)
        print(f'{count}: x={next_x}')
        if abs(next_x - init_x) < tolerance:
            break
        else:
            init_x = next_x
    plt.show()

