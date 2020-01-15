from collections import Counter

import pandas as pd
import os
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from scratch12.ex04 import summarize_by_class, calculate_class_probability


def train_test_split(df, test_size):
    """
    df=데이터 프레임, test_size = 테스트 세트의 비율
    학습 세트와 검증 세트를 리스트 혹은 ndarray 형태로 리턴
      -> [[],[],[],...], [[],[],[],...]
    (데이터와 레이블이 같이 있는 학습세트와 검증세트 두개 리턴)
    """
    # length = len(df)
    # indices = np.array([i for i in range(length)])
    # np.random.shuffle(indices)
    # cut = int(length * (1-test_size))
    #
    # train_set = df[indices[:cut]]
    # test_set = df[indices[cut:]]
    # return train_set, test_set

    np.random.seed(1213)
    array = df.to_numpy()
    np.random.shuffle(array)
    cut = int(len(array) * (1-test_size)) # 학습, 테스트 세트 나누기 위한 인덱스
    train_set = array[:cut]
    test_set = array[cut:]
    return train_set, test_set


def predict(summaries, x_test):
    """
    테스트 세트의 예측값들의 array 리턴
    [0, 1, 1, 2, 0, 0, 2, ...]
    ==== 방법 ====
    x_test의 원소 개수만큼 반복하면서
    각 원소(예측값을 찾으려는 데이터)의 class에 속할 확률을 계산해서
    그 확률중 최대값을 갖는 key값을 predict 리스트에 추가
    """
    # predict = []
    # for i in x_test:
    #     probabilities = calculate_class_probability(summaries, i)
    #     max_label, max_val = sorted(probabilities.items(), key = lambda x:-x[1])[0]
    #             --> sorted(dict): dict의 key를 오름차순 정렬
    #                 sorted(dict.values()) : dict의 value를 오름차순 정렬
    #                 sorted(dict.items()) : (key, value) 튜블을 key값 기준으로 오름차순 정렬
    #             --> sorted(iterable, key=정렬기준함수) : 정렬 기준 함수의 리턴값을 기준으로 iterable 타입을 정렬
    #     predict.append(max_label)
    # return predict

    predict = []
    for i in x_test:
        probabilities = calculate_class_probability(summaries, i)
        max_label, max_prob = None, -1
        for k, v in probabilities.items():
            if v > max_prob:
                max_prob = v
                max_label = k
        predict.append(max_label)
    return predict


if __name__ =='__main__':
    # ========== iris data ==========
    iris_file = os.path.join('..', 'scratch11', 'iris.csv')
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris_dataset = pd.read_csv(iris_file, header=None, names=col_names)
    # print(iris_dataset.loc[:,'Class'])

    # class컬럼의 중복 제거 값 확인 -> 결과 : {'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'}
    # -> set : 중복을 허락하지 않는 datatype
    # species = set(iris_dataset.loc[:, 'Class'])
    # print(species)
    # spesies = Counter(iris_dataset.loc[:, 'Class'])
    # print(spesies)

    iris_dataset = iris_dataset.replace({'Class': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']},
                                        {'Class': [0, 1, 2]})
    # 값 변경하는 다른 방법
    # iris_dataset.loc[iris_dataset['Class'] == 'Iris-setosa', 'Class'] = 0
    # iris_dataset.loc[iris_dataset['Class'] == 'Iris-versicolor', 'Class'] = 1
    # iris_dataset.loc[iris_dataset['Class'] == 'Iris-virginica', 'Class'] = 2

    # print(iris_dataset.head())
    # iris_dataset = iris_dataset.to_numpy()   -> train_test_split()안에 넣어서 할 필요 없음

    iris_train, iris_test = train_test_split(iris_dataset, test_size=0.2)
    # print(iris_train[:5])
    # print(iris_train[-5:])

    summaries = summarize_by_class(iris_train)
    # print('summaries')
    # print(summaries)

    pred = predict(summaries, iris_test)
    # print(pred)

    conf_matrix = confusion_matrix(iris_test[:,-1], pred)
    print(conf_matrix)
    report = classification_report(iris_test[:,-1], pred)
    print(report)


    # ========== wisc bc data ==========
    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')

    wisc_dataset = pd.read_csv(cancer_file)
    wisc_dataset = wisc_dataset.iloc[:, 1:]
    # 'id' 컬럼 지우는 또 다른 방법
    # wisc_dataset.drop(columns ='id', inplace=True)
    # del wisc_dataset['id']

    # print(set(wisc_dataset.loc[:,'diagnosis']))
    wisc_dataset = wisc_dataset.replace({'diagnosis': ['B','M']}, {'diagnosis': [0, 1]})
    # wisc_dataset.loc[wisc_dataset['idagnosis'] == 'B', 'diagnosis'] = 0
    # wisc_dataset.loc[wisc_dataset['idagnosis'] == 'M', 'diagnosis'] = 1

    wisc_dataset = wisc_dataset.loc[:, ::-1]    # 제일 앞 컬럼(diagnosis)를 제일 뒤로 보내기
    # 컬럼 순서 바꾸는 다른 방법
    # 1) reindex 사용하는 방법
    #     column_names = wisc_dataset.columns.tolist()  -> 컬럼 이름을 list로 뽑는 방법
    #     print(column_names)
    #     column_names.remove('diagnosis')
    #     column_names.append('diagnosis')
    #     wisc_dataset = wisc_dataset.reindex(columns=column_names)
    # 2) 컬럼을 선택하는 방식으로 순서 바꾸기
    #     wisc_dataset = wisc_dataset[column_names]

    # wisc_dataset = wisc_dataset.to_numpy()
    # print(wisc_dataset.iloc[:10])

    wisc_train, wisc_test = train_test_split(wisc_dataset, test_size=0.2)
    summaries = summarize_by_class(wisc_train)

    pred = predict(summaries, wisc_test)
    # print(pred)

    conf_matrix = confusion_matrix(wisc_test[:, -1], pred)
    print(conf_matrix)
    report = classification_report(wisc_test[:, -1], pred)
    print(report)
