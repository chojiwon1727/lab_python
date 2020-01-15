from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import numpy as np

wisc = datasets.load_breast_cancer()
point = wisc.data
label = wisc.target

point_train, point_test, label_train, label_test = train_test_split(point, label, test_size=0.2)

scaler = StandardScaler()
scaler.fit(point_train)
point_train_transformed = scaler.transform(point_train)
point_test_transformed = scaler.transform(point_test)

gnb = GaussianNB()
gnb.fit(point_train_transformed, label_train)
pred = gnb.predict(point_test_transformed)

conf_matrix = confusion_matrix(label_test, pred)
report = classification_report(label_test, pred)
print(np.mean(label_test == pred))
print(conf_matrix)
print(report)
