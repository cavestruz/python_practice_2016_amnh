import numpy as np
from scipy_functions import func

def gendat(xdata) :
    y = func(xdata, 2.5, 1.3, 0.5)
    ydata = y + 0.2 * np.random.normal(size=len(xdata))
    return y, ydata
