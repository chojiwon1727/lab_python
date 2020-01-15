"""
Logistic Regression(로지스틱 회귀 분석)
"""

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

iris = load_iris()
x = iris.data
y = iris.target
features = iris.feature_names
iris_df = pd.DataFrame(x, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
iris_df['species'] = y

print(iris_df.head())
print(iris_df.describe())

sns.pairplot(iris_df, hue='species', vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
plt.show()

# 데이터(x)와 타겟(y)를 학습/검증 세트로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1217)  # np.random.seed()와 동일

# 분류 알고리즘 중에서 logistic regression 선택
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
pred = log_reg.predict(x_test)
print('y_true : ', y_test)
print('predict : ', pred)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

