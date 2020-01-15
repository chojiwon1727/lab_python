import pandas as pd
import matplotlib.pyplot as plt

col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
iris = pd.read_csv('iris.csv', header=None, names=col_names)

iris_by_class = iris.groupby('Class')
# for name, group in iris_by_class:
#     print(group)

xy = []   # x축에 사용할 변수(컬럼)와 y축에 사용할 변수(컬럼)를 저장하기 위함
for i in range(4):
    for j in range(i+1,4):
        xy.append((col_names[i], col_names[j]))

print(len(xy))
print(xy)

fig, ax = plt.subplots(2,3)    # 하나의 화면(fig)을 행2 * 열3으로 나눠서 6개의 칸(ax)으로 나타내겠다는 의미
xy_idx = 0
for row in range(2):
    for col in range(3):
        axis = ax[row, col]     # => axis = ax[row][col]
        x = xy[xy_idx][0]      # x축 데이터 이름
        y = xy[xy_idx][1]      # y축 데이터 이름
        for name, group in iris_by_class:
            ax[row][col].scatter(group[x],group[y], label=name)
        axis.set_title(f'{x} vs {y}')     # subplot의 제목
        axis.set_xlabel(x)                # subplot의 x 레이블
        axis.set_ylabel(y)                # subplot의 y 레이블
        xy_idx += 1            # 다음 x,y축 데이터 이름으로 이동
plt.legend()
plt.show()