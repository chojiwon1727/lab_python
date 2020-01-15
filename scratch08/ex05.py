import random
import matplotlib.pyplot as plt

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step
from scratch08.ex04 import minibatches, linear_gradient

with open('mpg.csv', encoding='UTF-8') as f:     # with ~ as : 파일 사용이 모두 끝났을 때 close()자동 호출
    f.readline()  # 첫번째 라인을 읽고 버림 - 컬럼 이름(head)
    df = [line.strip().split(sep=',') for line in f]

print(df[0:5])

# 배기량(displ)과 시내 연비(cty)만 추출
displ = [float(row[2]) for row in df]
cty = [float(row[7]) for row in df]
displ_cty = [(d, c) for d, c in zip(displ, cty)]
print(displ_cty[0:5])


def mini_batch_gd(dataset, epochs=5000, learning_rate=0.001, batch_size=1, shuffle=True):
    dataset = dataset.copy()
    theta = [random.randint(-10,10), random.randint(-10,10)]
    print(f'theta 초기값: {theta}')
    for epoch in range(epochs):
        if shuffle:
            random.shuffle(dataset)
        mini_batch = minibatches(dataset, batch_size, shuffle)
        for batch in mini_batch:
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -learning_rate)
    return theta


print('\n=== stochastic gradient descent ===')
theta_stochastic = mini_batch_gd(displ_cty, epochs=200, shuffle=False)
print(theta_stochastic)

print('\n=== batch gradient descent ===')
theta_batch = mini_batch_gd(displ_cty, epochs=5000, learning_rate=0.01, batch_size=len(displ_cty))
print(theta_batch)

print('\n=== mini batch gradient descent ===')
theta_mini = mini_batch_gd(displ_cty, epochs=1000, learning_rate=0.01, batch_size=32)
print(theta_mini)


def linear_regression(x, theta):
    slope, intercept = theta
    return slope * x + intercept


plt.scatter(displ, cty)
ys_stochastic = [linear_regression(x, theta_stochastic) for x in displ]
plt.plot(displ, ys_stochastic, color='red', label='Stochastic GD')

ys_batch = [linear_regression(x, theta_batch) for x in displ]
plt.plot(displ, ys_batch, color='green', label='Batch GD')

ys_mini = [linear_regression(x, theta_mini) for x in displ]
plt.plot(displ, ys_mini, color='yellow', label='Mini-Batch GD')

plt.legend()
plt.xlabel('displacement(cc)')
plt.ylabel('efficiency(mpg)')
plt.title('Fuel Efficiency vs Displacement')
plt.show()