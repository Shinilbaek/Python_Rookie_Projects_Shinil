from sklearn.neighbors import KNeighborsClassifier
import numpy as np

import timeit

# Simple Dataset
X = np.array([[1, 1], [1, 1.5], [2, 2.5], [2.5, 3], [1.5, 1], [3, 2.5]])
Y = ['A', 'A', 'B', 'B', 'A', 'B']

# algorithm = 'ball_tree' or 'kd_tree' or 'brute' or 'auto'
model = KNeighborsClassifier(n_neighbors=3, algorithm='ball_tree')
t1 = timeit.timeit()
model.fit(X,Y)
t2 = timeit.timeit()
print(f'Time: {t2-t1}')

print(model.predict([[1.75,1.75]]))
print(model.predict_proba([[1.75,1.75]]))
print(model.score(X,Y))