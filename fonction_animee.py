# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:19:40 2016

<<<<<<< HEAD

@author: Amandine et Lorena

>>>>>>> origin/master
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

fig = plt.figure("Animation !") 
plt.clf()
line, = plt.plot([], [])
plt.xlim(-10., 10.)
plt.ylim(-5., 5.)


def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    line.set_data(X[:i], C[:i])
    #line.set_data(X[:i], S[:i])
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init,
frames=1000, interval=20, blit=True)

plt.show()



