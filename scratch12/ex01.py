from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

iris = datasets.load_iris()
print(type(iris))
print(iris)
print('data shape: ',iris.data.shape)
print('iris target: ',iris.target_names)
print('iris features:', iris.feature_names)

point = iris.data
print('type point:', type(point))
print(point[:5])

label = iris.target
print('type label:', type(label))
print(label[:5])

# point, label = datasets.load_iris(return_X_y=True)

point_train, point_test, label_train, label_test = train_test_split(point, label, train_size=0.2)

scaler = StandardScaler()
scaler.fit(point_train, label_train)
point_train_transformed = scaler.transform(point_train)
point_test_transformed = scaler.transform(point_test)

# 머신러닝 모델 선택 - Naive Bayes
gnb = GaussianNB()
gnb.fit(point_train_transformed, label_train)
pred = gnb.predict(point_test_transformed)

# 모델 평가
conf_matrix = confusion_matrix(label_test, pred)
report = classification_report(label_test, pred)
print(np.mean(label_test == pred))
print(conf_matrix)
print(report)