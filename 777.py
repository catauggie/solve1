from scipy.optimize import minimize
def f(x):
    return x ** 2
%matplotlib inline
import matplotlib.pyplot as plt

x = np.arange(-3, 3, .1)
y = f(x)

plt.plot(x,y)
plt.show()
