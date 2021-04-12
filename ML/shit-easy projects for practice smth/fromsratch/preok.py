import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


dataframe = pd.read_csv('linear-regression-dataset.csv')
x = dataframe[['deneyim']]
y = dataframe[['maas']]
clf = LinearRegression()
clf.fit(x, y)


plt.scatter(x, y)
plt.plot(x, clf.predict(x))
print(x - clf.predict(x))
plt.show()
