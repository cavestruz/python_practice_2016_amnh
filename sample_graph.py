'''This makes our first sample plot'''
import numpy as np
import matplotlib.pyplot as plt

mydata = np.loadtxt('data.txt')
x = mydata[:,0]
y = mydata[:,1]
line = plt.plot(x,y)
plt.show()
