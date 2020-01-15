from collections import Counter
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report


def train_test_split(point, label, test_size):
    """
    len(point) == len(label) 가정

    :param point: numpy.ndarray (n x m)
    :param label: numpy.ndarray 원소의 개수가 n개인 1차원 배열(n x 1)
    :param test_size: 0.0 ~ 1.0의 float
    :return: point_train, point_test, label_train, label_test
    """
    length = len(point)

    indices = np.array([i for i in range(length)])      # 인덱스를 저장하는 array 생성 -> point와 label의 인덱스가 같이 움직여야 하므로
    # print(f'shuffle 전 : {indices}')

    np.random.shuffle(indices)   # 인덱스를 임의로 섞음
    # print(f'shuffle 후 : {indices}')

    cut = int(length * (1-test_size))     # Train set의 개수

    point_train = point[indices[:cut]]
    label_train = label[indices[:cut]]
    point_test = point[indices[cut:]]
    label_test = label[indices[cut:]]

    return point_train, point_test, label_train, label_test


class MyScaler:
    def fit(self, point):
        """point의 각 column별 평균과 표준편차 저장"""
        self.feature_means = np.mean(point, axis=0)   # axis=0 : 컬럼별(pandas는 반대)  -> 안주면 point의 전체 평균 1개 저장
        self.feature_stds = np.std(point, axis=0)     # self로 만든 변수는 같은 class내의 다른 함수에서도 사용 가능
        # print(self.feature_means)
        # print(self.feature_stds)

    def transform(self, point):
        """point의 평균을 0, 표준편차를 1로 변환해서 리턴 """
        dim = point.shape
        transformed = np.empty(dim)    # point와 동일한 행,열 크기로 아무것도 들어있지 않은 array생성
        for row in range(dim[0]):      # row 개수만큼 반복
            for col in range(dim[1]):  # col 개수만큼 반복
                transformed[row, col] = (point[row, col] - self.feature_means[col]) / self.feature_stds[col]
        return transformed


class MYKnnClassifier:
    def __init__(self, n_neighbors=5):  # 객체 생성
        """ K값을 몇개로 할 것인지 저장 """
        self.k = n_neighbors

    def fit(self, point_train, label_train):  # 모델 훈련
        """ 레이블을 가지고 있는 데이터(point)를 저장 """
        self.points = point_train
        self.labels = label_train

    def predict(self, point_test):  # 예측
        """
        테스트 세트 point_test의 각 점들마다
        1) 학습세트(point_train)에 있는 모든 점들과의 거리 계산
        2) 계산된 거리들 중에서 가장 짧은 거리 k개 선택
        3) k개의 선택된 레이블 중에서 가장 많은 것을 예측값(pred)으로 함(다수결)
           -> 예측값은 테스트세트의 point개수만큼 나와야 함
        """
        predicts = []    # 예측값들의 배열 리턴
        for testpoint in point_test:   # 테스트 세트에 있는 점들의 개수만큼 반복
            distances = self.distance(self.points, testpoint) # 학습 세트의 점들과의 거리를 계산
            # print(f'test point: {testpoint} / distances: {distances}')
            pred = self.majority_vote(distances) # 다수결로 예측값 결정
            predicts.append(pred) # 예측값을 리스트에 저장
        return np.array(predicts)

    def distance(self, point_train, testpoint):
        """
        점(벡터) testpoint와 점(벡터)들 point_train사이의 거리들의 array리턴
        :param point_train: train set
        :param testpoint: test point 1개
        :return: point_train과 testpoint의 거리들(점 하나-test point와 점 여러개-point_train간 거리들)
        """
        return np.sqrt(np.sum((point_train - testpoint)**2, axis=1))

    def majority_vote(self, distances):
        # 1. 거리 순서로 정렬된 인덱스 찾기
        indices_by_distance = np.argsort(distances)
        # print(indices_by_distance)

        # 2. 가장 가까운 k개의 레이블 찾기
        k_nearest_neighbor = []

        # for i in range(self.k):
        #     idx = indices_by_distance[i]
        #     k_nearest_neighbor.append(self.labels[idx])

        # for i in indices_by_distance[0:self.k]:
        #     k_nearest_neighbor.append(self.labels[i])

        k_nearest_neighbor = [self.labels[i] for i in indices_by_distance[0:self.k]]
        # print(k_nearest_neighbor)

        # 3. 가장 많은 득표를 얻은 레이블 찾기
        vote_counter = Counter(k_nearest_neighbor)
        # print(vote_counter)
        vote_label = vote_counter.most_common(1)[0][0]
        # -> most_common(n) : 가장 자주 등장하는 순위 n번째 까지를 리스트 출력
        # 리스트안에 튜플로 출력하기 때문에 ex[('a', 2)] 0번째 인덱스에서 0번째 인덱스를 꺼내야 함
        # 만약 가장 빈도수가 높은 레이블이 2개 이상이 나오면 임의로 선택을 하거나 가중치를 둬서 선택을 해야함
        # 따라서 k값을 홀수로 주는 것이 좋음

        return vote_label

if __name__ == '__main__':
    np.random.seed(1210)

    point = np.random.randint(10, size=(10,2))
    # print(point)
    label = np.array(['a', 'b', 'a', 'b', 'a']*2)
    # print(label)
    point_train, point_test, label_train, label_test = train_test_split(point, label, test_size=0.2)
    # print(f'point_train : \n{point_train}')
    # print(f'label_train : \n{label_train}')
    # print(f'point_test : \n{point_test}')
    # print(f'label_test : \n{label_test}')

    scaler = MyScaler()   # scaler객체(생성자) 생성
    scaler.fit(point_train)    # 참조변수를 찾아가서 거기 있는 메소드 호출
    point_train_scaled = scaler.transform(point_train)
    point_test_scaled = scaler.transform(point_test)
    # print(point_test_scaled)

    knn = MYKnnClassifier(n_neighbors=3)    # k-nn 분류기 객체 생성 - 생성자 호출
    # print('k = ', knn.k)
    knn.fit(point_train_scaled, label_train)    # 모델 학습
    pred = knn.predict(point_test_scaled)     # test set을 넘겼을 때 예측값(pred)
    # print(pred)
    # print(label_test == pred)





