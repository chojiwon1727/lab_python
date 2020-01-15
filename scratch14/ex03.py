from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import math


def logistic(x):
    """ logistic sigmoid 함수 """
    return 1 / (1 + math.exp(-x))


def predict(row, betas):
    """
    row 의 x1, x2값과 betas의 b0, b1, b2를 사용해서
    회귀식 y = b0 + b1*x1 + b2*x2를 만들고
    회귀식을 로지스틱 함수의 파라미터에 전달해서
    예측값(y_hat)을 찾아내는 확률을 리턴하는 함수

    회귀식 : y_hat = betas[0] + betas[1]*row[0] + betas[2]*row[1]
    """
    y_hat = betas[0]
    for i in range(len(betas) - 1):
        y_hat += betas[i+1] * row[i]
    return logistic(y_hat)


def coefficient_sgd(dataset, learning_rate, epochs):
    """
    y = b0 + b1*x1 + b2*x2의 계수들(b0, b1, b2)을
    stochastic gradient descent 방법으로 추정(estimate)

    :learning_rate : gradient 동일(최대값찾기)/반대(최소값찾기) 방향으로 움직이는 정도
    """
    # 회귀식에서 가장 처음에 사용할 betas 초기값을 0으로 시작
    betas = [0 for _ in range(len(dataset[0]))]
    for epoch in range(epochs):
        sse = 0  #sse : sum of squared errors(오차 제곱들의 합)
        for sample in dataset:
            prediction = predict(sample, betas)    # betas로 추정한 예측값값
            error = sample[-1] - prediction
            sse += error**2
            # betas(b0, b1, b2)를 아래와 같은 방법으로 업데이트
            # b_new = b + leaning_rate * error * prediction * (1-prediction) * x
            betas[0] = betas[0] + learning_rate * error * prediction * (1-prediction) * 1
            for i in range(len(sample)-1):
                betas[i+1] = betas[i+1] + learning_rate * error * prediction * (1-prediction) * sample[i]
        print(f'>>> epoch : {epochs}, sum of squared errors : {sse}')
    return betas


if __name__ == '__main__':
    iris = load_iris()
    # print(iris.DESCR)

    x = iris.data
    y = iris.target
    features = iris.feature_names

    for i in range(len(features)):
        plt.scatter(x[:, i], y, label=features[i])
    plt.legend()
    plt.show()

    # class구분에 상관이 높아 보이는 petal length와 petal width만 선택
    x = x[:, 2:4]
    # print(x[:5])

    # setosa 5개와 setosa가 아닌 품종 5개를 샘플링
    indices = [10 * x for x in range(10)]
    sample_data = np.c_[x[indices, :], y[indices]]
    # print(sample_data)

    np.random.seed(1218)
    betas = np.random.random(3)    # 난수 b0, b1, b2 생성
    for sample in sample_data:
        prediction = predict(sample, betas)
        error = sample[-1] - prediction     # error = 실제값 - 예측값
        print(f'실제값 : {sample[-1]}, 예측값 : {prediction}, 오차 : {error}')

    learning_rate = 0.3
    epochs = 100
    betas = coefficient_sgd(sample_data, learning_rate, epochs)
    print(f'betas = {betas}')

    # 모델 성능 측정(iris 데이터에서 sample_data에 포함되지 않았던 데이터 활용)
    test_sample1 = np.r_[x[1, :], y[1]]
    prediction = predict(test_sample1, betas)
    print(f'실제값 : {test_sample1[-1]}, 예측값 : {prediction}')

    test_sample2 = np.r_[x[51, :], y[51]]
    prediction = predict(test_sample2, betas)
    print(f'실제값 : {test_sample2[-1]}, 예측값 : {prediction}')