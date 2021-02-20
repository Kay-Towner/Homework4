#By: Kay Towner
#2.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from scipy import interpolate

#a)
def equation(x):
    """This function is to initialize the
    equation used later by the other functions.
    """
    y = np.sqrt(x) + np.cos(x)
    return y

def analyt_deriv(x):
    """Function to note the analytical derivative to the
    func: "equation"
    """
    return ((1)/(2 * np.sqrt(x))- np.sin(x))

#b)
if __name__ == "__main__":
    x_sparse = np.arange(0, 4*np.pi, 0.8)
    x_finely = np.arange(0, 4*np.pi, 0.01)

    #true and deriv anylized finely:
    y_true_func = equation(x_finely)
    y_deriv = analyt_deriv(x_finely)

    #true and deric anylized sparse:
    y_true_func2 = equation(x_sparse)
    y_deriv2 = analyt_deriv(x_sparse)

#when plotting the sparse points:
#c)
    plt.plot(y_true_func, y_deriv, '.')
    plt.show()

#d)    
    yder = interpolate.splev(x_sparse, tck, der=1)
    plt.figure()
    plt.plot(y_true_func, y_deriv, '--'  )
    plt.legend(['cubic, Spline', 'True Deriv'])
    plt.title('Part 2 part d')
    plt.show()
    
#plotting the points all together:

    
















    

