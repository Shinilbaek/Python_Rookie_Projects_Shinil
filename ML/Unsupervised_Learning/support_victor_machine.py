import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# Set simple dataset
X = np.array([5.1,4.9,4.7,4.6,5.0,5.4,4.6,5.0,4.4,4.9,5.4,4.8,4.8,4.3,5.8,5.7,5.4,5.1,5.7,5.1])
Y = np.array([1.4,1.4,1.3,1.5,1.4,1.4,1.5,1.4,1.5,1.5,1.6,1.4,1.1,1.2,1.5,1.3,1.4,1.7,1.5])

# C is the penalty factor, if C is greater, the svm model is easily overfitting
#model = svm.SVC(C=3,kernel='linear',gamma=10)
#model.fit(X,Y)

