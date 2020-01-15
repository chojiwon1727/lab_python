import scipy.stats as stats
import matplotlib.pyplot as plt


# 균등분포(uniform distribution)
xs = [x/10 for x in range(-30, 31)]  #그래프를 그릴 x구간(-30~30까지 1단위의 숫자로 그래프를 그리는것 보다 10으로 나눠서 0.1단위로 그리는 것이 그래프가 더 부드럽기 때문에 나눔)
ys1 = [stats.uniform.pdf(x) for x in xs]
ys2 = [stats.uniform.cdf(x) for x in xs]
plt.plot(xs, ys1, color='blue', label='PDF')
plt.plot(xs, ys2, color='red', label='CDF')
plt.legend()
plt.title('Uniform Distribution PDF & CDF')
plt.show()

ys1 = [stats.norm.pdf(x) for x in xs]
ys2 = [stats.norm.cdf(x) for x in xs]
plt.plot(xs, ys1, label = 'PDF')
plt.plot(xs, ys2, label = 'CDF')
plt.legend()
plt.title('Standard Nominal Distribution PDF & CDF')
plt.show()