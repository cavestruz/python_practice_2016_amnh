'''Function to plot what we have'''
import matplotlib.pyplot as plt

def plot_fit(xdata=None,ydata=None,y=None,popt=None,func=None) :
    # original y data that helped create perturbed y data 
    plt.plot(xdata,y,color='g')
    # perturbed y data
    plt.plot(xdata,ydata,marker="*",color='m')
    # best fit y data to the perturbed data
    plt.plot(xdata,func(xdata,popt[0],popt[1],popt[2]),marker='o',color='r')
    
    plt.show()
