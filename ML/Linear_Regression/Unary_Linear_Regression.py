import numpy as np
import matplotlib.pyplot as plt


# Training Set
x_train = [4,8,5,10,12]
y_train = [20,50,30,70,60]

# ploting function
def draw(x_train,y_train):
    plt.scatter(x_train,y_train)

# Least squares method
# Find best slope a and intercept b

def fit(x_train,y_train):
    size = len(x_train)
    numerator = 0 
    # initialize the numerator
    denominator = 0
    # initialize the denominator
    for i in range(size):
        numerator += (x_train[i] - np.mean(x_train)) *\
                     (y_train[i] - np.mean(y_train))
        denominator += (x_train[i] - np.mean(x_train)) **2
    a = numerator/denominator
    b = np.mean(y_train) - a*np.mean(x_train)
    return a,b

# Calculate prediction y with given x

def predict(x,a,b):
    # Unary Linear Regression Model
    y = a*x+b
    return y 

x_test = np.linspace(4,15,9)

def fit_line(a,b,x_test):
    # Test in the test set and plot
    y = a*x_test +b
    plt.plot(x_test,y)
    plt.show()

if __name__ == "__main__":
    draw(x_train,y_train)
    a,b = fit(x_train,y_train)
    print(a,b)
    fit_line(a,b,x_test)