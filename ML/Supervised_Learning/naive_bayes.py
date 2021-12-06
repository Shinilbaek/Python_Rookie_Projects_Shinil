import numpy as np
from sklearn.naive_bayes import BernoulliNB

# Simple random dataset
np.random.seed(2517)
X = np.random.randint(2,size=(6,100))
Y = np.array([1,2,3,4,4,5])

model = BernoulliNB()
model.fit(X,Y)

print(model.predict(X[2:3]))