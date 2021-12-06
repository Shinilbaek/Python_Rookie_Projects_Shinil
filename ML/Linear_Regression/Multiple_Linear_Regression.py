import numpy as np
import pandas as pd

# Training Set
# First three columns refer to x1,x2,x3
# Last columns refers to y

data = np.array([[3, 2, 9, 20],
                 [4, 10, 2, 72],
                 [3, 4, 9, 21],
                 [12, 3, 4, 20]])

# Seperate independent variable and controlled variable 
X = data[:, :-1]
Y = data[:, -1]

# Add constant term coefficients to the coefficient matrix
X = np.mat(np.c_[np.ones(X.shape[0]),X])
# Convert array to matrix
Y = np.mat(Y)

B = np.linalg.inv(X.T * X) * (X.T) *(Y.T)
# Output coefficient, the first term is a constant term
# The others are regression coefficients
print("B:", B, "\n")

# Correlation coefficient
Q_e = 0
Q_E = 0
Y_mean = np.mean(Y)
for i in range(Y.size):
    Q_e += pow(np.array((Y.T)[i] - X[i] * B), 2)
    Q_E += pow(np.array(X[i] * B) - Y_mean, 2)
R2 = Q_E / (Q_e + Q_E)
print("R2", R2)

data_train = np.mat([1,50,50,50]) 
print('The prediction of "[50,50,50]')
print(data_train * B)