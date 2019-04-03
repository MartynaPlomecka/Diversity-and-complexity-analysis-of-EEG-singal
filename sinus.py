#creating different sine waves
import matplotlib
import numpy as np
import math
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

T = 6.28
ts = 1/10000
t = np.arange(0,T,ts)


def sin(t, a=1., f=400, k=0):
    return [a * math.sin(2*math.pi*f*ti+k) for ti in t]


sinuses = [
    sin(t, 1, 1),
    sin(t, 1, 2),
    sin(t, 1, 4),
    sin(t, 1, 8),
    sin(t, 1, 16),
    sin(t, 1, 32)
]

if __name__ == '__main__':
    plt.plot(t, sin(t, 1, 10))
    plt.plot(t, sin(t, 2, 10)) #higher amplitude
    plt.plot(t, sin(t, 1, 15)) #higher frequency
    plt.plot(t, sin(t, 2, 15)) #higher amplitude&frequency
    plt.plot(t, sin(t, 1, 10, 2)) #phase
    plt.plot(t, sin(t, 2, 10, 2)) #phase & amplitude
    plt.show()



