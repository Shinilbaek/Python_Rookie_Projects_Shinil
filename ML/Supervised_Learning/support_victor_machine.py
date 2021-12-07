import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# Set simple dataset
X_1 = np.array([5.1,4.9,4.7,4.6,5.0,5.4,4.6,5.0,4.4,4.9,5.4,4.8,4.8,4.3,5.8,5.7,5.4,5.1,5.7])
X_2 = np.array([1.4,1.4,1.3,1.5,1.4,1.4,1.5,1.4,1.5,1.5,1.6,1.4,1.1,1.2,1.5,1.3,1.4,1.7,1.5])
X_a = np.transpose(np.vstack([X_1,X_2]))
X_3 = np.array([6.4,6.9,5.5,6.5,5.7,6.3,4.9,6.6,5.2,5.0,5.9,6.0,6.1,5.6,6.7,5.6,5.8,6.2,5.6])
X_4 = np.array([4.5,4.9,4.0,4.6,4.5,4.7,3.3,4.6,3.9,3.5,4.2,4.0,4.7,3.6,4.4,4.5,4.1,4.5,3.9])
X_b = np.transpose(np.vstack([X_3,X_4]))
X = np.mat(np.vstack([X_a,X_b]))

Y = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

# C is the penalty factor, if C is greater, the svm model is easily overfitting
model = svm.SVC(C=3,kernel='linear',gamma=10)
model.fit(X,Y)

w = model.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(0,10,num = 38)
yy = a * xx - (model.intercept_[0]) / w[1]

print("support vectors = ", model.support_vectors_)
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a*xx + (b[1]-a*b[0])

plt.plot(xx, yy, 'k-')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors='none')
plt.scatter(X[:, 0].flat, X[:, 1].flat, c=Y, cmap=plt.cm.Paired)
plt.axis('tight')
#plt.savefig('./svm_test.jpg)
plt.show()