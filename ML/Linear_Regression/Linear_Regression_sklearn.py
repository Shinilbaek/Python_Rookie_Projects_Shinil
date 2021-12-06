from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

# Training Set
x_train = np.array([[2, 4], [5, 8], [5, 9], [7, 10], [9, 12]])
y_train = np.array([20, 50, 30, 70, 60])

model.fit(x_train,y_train)
# fit(x,y,sample_weight=None),x:Training Set y:Target sample_weight:num of sample
# coef_ : coeffient,intercept_
print(model.coef_)
print(model.intercept_)
print(model.score(x_train,y_train)) #R2
