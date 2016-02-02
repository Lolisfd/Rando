# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:19:40 2016

@author: Ama 
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = np.linspace(0.,10.,1000)
y = np.sin(-x / 10.) * np.sin(2.* np.pi * x)


fig = plt.figure("Animation !") 
plt.clf()
line, = plt.plot([], [])
plt.xlim(0., 10.)
plt.ylim(0., 10.)


def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func=init,
frames=1000, interval=20, blit=True)

plt.show()


