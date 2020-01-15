import matplotlib.pyplot as plt

x = [i for i in range(10)]
print(x)

y1 = [2 **x for x in range(10)]
print(y1)
plt.plot(x, y1, 'go-', label='example1')

y2 = [2**x for x in range(9,-1,-1)]
print(y2)
plt.plot(x, y2, 'r--', label='example2')

y3 = [x + y for x, y in zip(y1, y2)]
print(y3)
plt.plot(x, y3, 'b:', label='example3')

plt.legend(loc='best')
plt.title('Line Chart Example')
plt.show()

