"""
scikit-learn 패키지를 이용한 knn(k Nearest Neighbor : 최근접이웃)
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 1. 데이터 준비
    # 1) csv파일에 헤더가 없기 때문에 컬럼 이름 정의
    col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

    # 2) csv파일에서 DataFarme 생성
    dataset = pd.read_csv('iris.csv', header=None, names=col_name)
    # print(dataset.shape)
    # print(dataset.head())
    # print(dataset.info())
    # print(dataset.describe())
    # print(dataset.loc[0:5])
    # print(dataset.iloc[0:5])

    # 2. 데이터 전처리
    # - 데이터 세트를 데이터(포인트)와 레이블로 구분
    X = dataset.iloc[:, :-1].to_numpy()
    # print(X)
    y = dataset.iloc[:, 4].to_numpy()
    # print(y)

    # - 데이터를 training set, test set으로 나누기
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)     # 150 * 0.2 = 30(test_seize)
    # print(len(x_train), len(x_test), len(y_train), len(y_test))
    # print(x_train[:3])
    # print(y_train[:3])

    # 3. 거리 계산을 위해서 각 특성들을 스케일링(표준화)
    # -> Z-score 표준화 : 평균0, 표준편차1로 변환
    scaler = StandardScaler()    # Scaler객체 생성
    scaler.fit(x_train)       # 스케일링(표준화)를 위한 평균과 표준편차 계산
    x_train = scaler.transform(x_train)    # 스케일링(표준화) 수행
    x_test = scaler.transform(x_test)
    for col in range(4):
        print(f'train평균 : {x_train[:, col].mean()}, train표준편차 : {x_train[:, col].std()}')
        print(f'test평균 : {x_test[:, col].mean()}, test표준편차 : {x_test[:, col].std()}')
        print()

    # 4. 학습과 예측(training / prediction)
    # 분류기 생성
    classifier = KNeighborsClassifier(n_neighbors=5)    # 거리를 계산할 때 최단거리 5개를 뽑겠다는 의미(홀수가 좋음)
    # 분류기 학습
    classifier.fit(x_train, y_train)
    # 예측
    y_pred = classifier.predict(x_test)
    print(y_pred)

    # 5. 모델평가
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    report = classification_report(y_test, y_pred)
    print(report)

    # 6. 모델 개선(향상) - k값을 변화시킬 때 에러가 얼마나 줄어드는가가
    errors = []
    for i in range(1,31):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        pred_i = knn.predict(x_test)
        errors.append(np.mean(pred_i != y_test))
    print(errors)

    plt.plot(range(1,31), errors, marker='o')
    plt.title('Mean Error with K-value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()

