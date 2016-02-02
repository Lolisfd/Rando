# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:19:40 2016

@author: Amandine et Lorena

"""

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()

