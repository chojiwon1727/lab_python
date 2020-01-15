"""
Boston house prices dataset
"""
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 1. 보스턴 집값 데이터 세트 로딩

datasets =load_boston()    # -> Bunch : 파이썬의 dict와 비슷한 타입(key:value) -> dict를 상속받아 만들어진 class
# print(type(datasets))
# print(datasets.keys())     # -> ['data', 'target', 'feature_names', 'DESCR', 'filename'] 출력
# print(datasets.DESCR)      # -> datasets에 대한 설명

# 1) 데이터와 타켓 구분
X = datasets.data      # -> datasets['data']와 동일
y = datasets.target    # -> datasets['target']과 동일
# print('X.shape : ',  X.shape)
# print(X[:2])
# print('y.shape : ',  y.shape)
# print(y[:2])
features = datasets.feature_names    # -> datasets['feature_names']와 동일
# print(features)

# 2. 데이터 탐색 -> y와 각 변수에 대한 산점도 그래프
#    -> 변수들중 어떤 변수가 y값과 어떤 관계(선형, 2차식 등)가 있는지 탐색
fig, ax = plt.subplots(4,4)
ax_flat = ax.flatten()            # 반복을 편리하게 하기 위해 4*4차원을 1차원으로 펼치는 방법
for i in range(len(features)):    # 변수 개수만큼 반복
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)      # y ~ feature 산점도 그래프
    axis.set_title(features[i])   # subplot에 title추가
plt.show()

# -> 변수 RM은 선형관계로 보이고 LSTAT는 선형 혹은 2차식으로 보임

# 3. 학습 세트/검증 세트 나눔
np.random.seed(1217)
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.3)
print(f'X_train len : {len(X_train)}, X_test len : {len(X_test)}')

# 4. 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# price = b0 + b1*rm : 주택가격 ~ 방의 개수(rm)
X_train_RM = X_train[:, np.newaxis, 5]     # 2차원 배열을 만들기 위해 np.newaxis 사용 -> 선형회귀가 2차원 배열만 사용 가능하기 때문
X_test_RM = X_test[:, np.newaxis, 5]
print(f'X_train_rm : {X_train_RM.shape}, X_test_rm : {X_test_RM.shape}')

lin_reg = LinearRegression()    # Linear Regression 객체 생성
lin_reg.fit(X_train_RM, y_train)     # fit(적합) / 학습(training) -> b0, b1 찾음
print(f'intercept:{lin_reg.intercept_}, coefficients:{lin_reg.coef_}')

# 5. 검증 세트를 사용해서 예측 -> 그래프
pred_RM = lin_reg.predict(X_test_RM)
# 실제값(scatter), 예측(plot) 그래프
plt.scatter(X_test_RM, y_test)
plt.plot(X_test_RM, pred_RM, 'r')
plt.title('Price ~ RM')
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()

# 6. Mean Square Error 계산
mse = mean_squared_error(y_test, pred_RM)
rmse = np.sqrt(mse)
print(f'Rrice ~ RM : RMSE = {rmse}')

# 7. R2-score 계산
r2_1 = lin_reg.score(X_test_RM, y_test)
r2_2 = r2_score(y_test, pred_RM)
print(f'r2_1 : {r2_1}, r2_2 : {r2_2}')


# Price ~ LSTAT 선형회귀 : price = b0 + b2 * lstat
X_train_lstat = X_train[:, np.newaxis, 12]
X_test_lstat = X_test[:, np.newaxis, 12]

lin_reg.fit(X_train_lstat, y_train)    # Linear Regression 객체는 위에서 생성했기 때문에 생성할 필요 없음
print(f'price ~ lstat: intercept:{lin_reg.intercept_}, coefficients:{lin_reg.coef_}')

pred_lstat = lin_reg.predict(X_test_lstat)
plt.scatter(X_test_lstat, y_test)   # 실제값
plt.plot(X_test_lstat, pred_lstat, 'r')  # 예측값
plt.title('Price ~ LSTAT')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

mse = mean_squared_error(y_test, pred_lstat)
rmse = np.sqrt(mse)
print(f'Rrice ~ RMSE : RMSE = {rmse}')

r2 = lin_reg.score(X_test_lstat, y_test)
print(f'Price ~ LSTAT : R^2 = {r2}')

# Price ~ LSTAT + LSTAT^2 선형회귀
# price = b0 + b2*lstat + lstat^2
poly = PolynomialFeatures(degree=2, include_bias=False)

# 학습세트에 다항식 항 추가 -> fit / train에 사용
X_train_lstat_poly = poly.fit_transform(X_train_lstat)     # 데이터에 다항식 항들을 컬럼으로 추가해주는 class객체
# 검증 세트에 다항식 항 추가 -> predict / test에 사용
X_test_lstat_poly = poly.fit_transform(X_test_lstat)

lin_reg.fit(X_train_lstat_poly, y_train)
print(f'price ~ lstat: intercept:{lin_reg.intercept_}, coefficients:{lin_reg.coef_}')

pred_lstat_poly = lin_reg.predict(X_test_lstat_poly)
plt.scatter(X_test_lstat, y_test)    # -> 그래프를 그릴때는 다항식 필요없이 x값만 있으면 됨

xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100,1))
# test_set의 최소~최대값까지의 구간을 100개로 나눔
#  -> lin_reg이 2차원 배열만 사용하기 때문에 reshape으로 100*1의 2차원 배열로 만들어줌
xs_poly = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')

# plt.plot(X_test_lstat, pred_lstat_poly, 'r')
plt.title('Price ~ lstat + lstat^2')
plt.show()

mse = mean_squared_error(y_test, pred_lstat_poly)
rmse = np.sqrt(mse)
print(f'Rrice ~ lstat : RMSE = {rmse}')

r2 = lin_reg.score(X_test_lstat_poly, y_test)
print(f'Price ~ LSTAT : R^2 = {r2}')

# 다중선형회귀(RM, LSTAT)
print()
X_train_rm_lstat = X_train[:, [5, 12]]    # 이미 2개 컬럼을 사용해서 2차원 배열이므로 np.newaxis 사용X
X_test_rm_lstat = X_test[:, [5, 12]]
lin_reg.fit(X_train_rm_lstat, y_train)
print(f'price ~ rm + lstat: intercept:{lin_reg.intercept_}, coefficients:{lin_reg.coef_}')

pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)
print(y_test[:5])
print(pred_rm_lstat[:5])

mse = mean_squared_error(y_test, pred_rm_lstat)
rmse = np.sqrt(mse)
print(f'Rrice ~ rm + lstat : RMSE = {rmse}')

r2 = lin_reg.score(X_test_rm_lstat, y_test)
print(f'Price ~ rm + lstat : R^2 = {r2}')

print('\nprice ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2')
# price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2
# price = b0 + b1*rm + b2*lstat + b3*rm^2 + b4*rm*lstat + b5*lstat^2

X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)

lin_reg.fit(X_train_rm_lstat_poly, y_train)
print(f'intercept:{lin_reg.intercept_}')
print(f'coefficients:{lin_reg.coef_}')

pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)

mse = mean_squared_error(y_test, pred_rm_lstat_poly)
rmse = np.sqrt(mse)
r2 = lin_reg.score(X_test_rm_lstat_poly, y_test)
print(f' RMSE = {rmse}, R^2 = {r2}')


print('\nPrice ~ RM + LSTAT^2')
# Price ~ RM + LSTAT^2
# price = b0 + b1*rm + b2*lstat + b3*lstat^2
# X_train_RM, X_train_lstat, X_train_poly

X_train_rm_lstat2 = np.c_[X_train_RM, X_train_lstat_poly]
X_test_rm_lstat2 = np.c_[X_test_RM, X_test_lstat_poly]
print('X_train_rm_lstat2 shape : ', X_train_rm_lstat2.shape)
print(X_train_rm_lstat2[:2])
print('X_test_rm_lstat2 shape : ', X_test_rm_lstat2.shape)
print(X_test_rm_lstat2[:2])

lin_reg.fit(X_train_rm_lstat2, y_train)
print(f'intercept:{lin_reg.intercept_}')
print(f'coefficients:{lin_reg.coef_}')

pred_rm_lstat2 = lin_reg.predict(X_test_rm_lstat2)
print(f'y_true : {y_test[:5]}')
print(f'pred : {pred_rm_lstat2[:5].round(2)}')

mse = mean_squared_error(y_test, pred_rm_lstat2)
rmse = np.sqrt(mse)
r2 = lin_reg.score(X_test_rm_lstat2, y_test)
print(f'RMSE = {rmse}, R^2 = {r2}')