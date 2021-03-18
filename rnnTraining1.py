import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('frequency1.csv')
X = dataset.iloc[1:10000, 1:130].values
y = dataset.iloc[1:10000, 0].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

print(X_train)
print(y_train)
print(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)