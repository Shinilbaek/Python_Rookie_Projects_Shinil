import numpy as np
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
# import moxing as mox
# import os

data = np.array([
    [2.697, 6.254, 1.000],
    [1.872, 2.014, 0.000],
    [2.312, 8.120, 0.000],
    [1.983, 4.990, 1.000],
    [9.320, 3.920, 0.000],
    [1.321, 5.583, 1.000],
    [2.215, 1.560, 0.000],
    [1.659, 2.932, 0.000],
    [8.650, 7.316, 1.000],
    [1.685, 4.763, 0.000],
    [1.786, 2.523, 1.000]
])
x = data[:,:2]
y = data[:,2]
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3)
# train_test_split(x,y,test_size=0.3)

model = LogisticRegression()
model.fit(train_x,train_y)

# Test the model
pred_y = model.predict(test_x)
# Check accuracy
print(pred_y == test_y)
print(model.score(test_x,test_y))