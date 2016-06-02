'''Functions to fit'''
import numpy as np

def func(x, a, b, c):
    '''This returns an array from performing e^?? on 
    x where x is the element by element array.  a, b, 
    c are just constants of the function.'''
    return a * np.exp(-b * x) + c
