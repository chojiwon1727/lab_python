from sklearn.metrics import classification_report, confusion_matrix
from scratch11.ex03 import train_test_split, MyScaler, MYKnnClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 1. iris데이터
    col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris = pd.read_csv('iris.csv', header=None, names=col_name)
    # print(iris.shape)
    # print(iris.head())
    # 데이터 프레임을 이용해서 각 특성(변수)들과 Class(레이블)과의 관계 그래프
    iris_by_class = iris.groupby('Class')
    for name, group in iris_by_class:
        # print(name, len(group))
        plt.scatter(group['sepal_length'], group['sepal_width'], label=name)    # -> 그래프 class수만큼 그려줌
    plt.legend()
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.show()

    for name, group in iris_by_class:
        # print(name, len(group))
        plt.scatter(group['petal_length'], group['petal_width'], label=name)    # -> 그래프 class수만큼 그려줌
    plt.legend()
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.show()

    iris_point = iris.iloc[:,0:3].to_numpy()
    iris_label = iris.iloc[:,4].to_numpy()

    point_train, point_test, label_train, label_test = train_test_split(iris_point, iris_label, test_size=0.2)

    scaler = MyScaler()
    scaler.fit(point_train)
    point_train = scaler.transform(point_train)
    point_test = scaler.transform(point_test)

    knn = MYKnnClassifier(5)
    knn.fit(point_train, label_train)
    pred = knn.predict(point_test)

    report = classification_report(label_test, pred)
    confusion = confusion_matrix(label_test, pred)
    # print('아이리스 데이터')
    # print(np.mean(label_test == pred))
    # print(confusion)
    # print(report)


    # 2. 암데이터
    wisc = pd.read_csv('wisc_bc_data.csv')
    # print(wisc.head())

    wisc_point = wisc.iloc[:,2:].to_numpy()
    wisc_label = wisc.iloc[:, 1].to_numpy()

    point_train, point_test, label_train, label_test = train_test_split(wisc_point, wisc_label, test_size=0.2)

    scaler = MyScaler()
    scaler.fit(point_train)
    point_train = scaler.transform(point_train)
    point_test = scaler.transform(point_test)

    knn = MYKnnClassifier()
    knn.fit(point_train, label_train)
    pred = knn.predict(point_test)

    report = classification_report(label_test, pred)
    confusion = confusion_matrix(label_test, pred)
    # print('암데이터')
    # print(np.mean(label_test == pred))
    # print(confusion)
    # print(report)
