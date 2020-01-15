import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()
x = boston.data
y = boston.target
features = boston.feature_names

# numpy.ndarray타입을 pandas.dataframe 타입으로 변환
boston_df = pd.DataFrame(x, columns=features)

# 데이터프레임에 가격 컬럼 추가
boston_df['PRICE'] = y
print(boston_df.head())
print(boston_df.shape)
print(boston_df.describe())

# 전체 데이터 프레임에서 관심 컬럼(변수)들만 선택
columns = ['LSTAT', 'INDUS', 'NOX', 'RM', 'PRICE']
subset_df = boston_df[columns]
print(subset_df.head())

sns.pairplot(subset_df)
plt.show()

# 상관 행렬(correlation matrix) : 상관계수들로 이루어진 행렬
corr_matrix = subset_df.corr().round(2)     # DataFrame.corr() : 상관계수 계산

# heatmap : 상관계수(correlation coefficient)가 클 수록 진한 색으로 표시됨
sns.heatmap(corr_matrix, annot=True)
plt.show()