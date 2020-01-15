import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

if __name__ == '__main__':
    wiscdata = pd.read_csv('wisc_bc_data.csv')

    point = wiscdata.iloc[:, 2:].to_numpy()
    label = wiscdata.iloc[:, 1].to_numpy()

    point_train, point_test, label_train, label_test = train_test_split(point, label, test_size=0.2)

    scaler = StandardScaler()
    scaler.fit(point_train)
    point_train = scaler.transform(point_train)
    point_test = scaler.transform(point_test)

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(point_train, label_train)
    pred = classifier.predict(point_test)

    confusionmatrix = confusion_matrix(label_test, pred)
    print(confusionmatrix)

    report = classification_report(label_test, pred)
    print(report)

    errors = []
    for i in range(1,31):
        classifier_i = KNeighborsClassifier(n_neighbors=i)
        classifier_i.fit(point_train, label_train)
        pred_i = classifier_i.predict(point_test)
        errors.append(np.mean(pred_i != label_test))
    print(errors)

    plt.plot(range(1, 31), errors, marker='o')
    plt.title('Mean Error with K-value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()




