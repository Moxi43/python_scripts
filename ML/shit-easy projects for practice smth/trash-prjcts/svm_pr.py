from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\code\\ML-practicE\\trash-prjcts\\linear-regression-dataset.csv")

y = df.maas.to_numpy()
X = df.drop('maas', axis=1).to_numpy()



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = SVC(kernel='linear')

X_train.reshape(-1, 1)
y_train.reshape(-1, 1)


clf.fit(X_train, y_train)

prediction = clf.predict(X_test)
print(X_test, y_test)
print(prediction)
print(accuracy_score(prediction, y_test))
