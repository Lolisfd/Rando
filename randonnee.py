# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:15:38 2016

@author: lolis
"""
import numpy as np
import struct


def lire_header(path):
        f = open(path)
        lines = f.readlines()
        f.close()
        out = {}
        for line in lines:
            if "=" in line:
                key = line.split("=")[0].split()[0]
                if key in ["lines", "samples"]:
                    out[key] = int(line.split("=")[1])
        return out

def read_data(path):
    f = open(path, "rb")
    out = np.fromfile(f, dtype= np.float32)
    f.close()
    return out

header_path = "BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data_path = "BossonsDEM_ll8m"
data = read_data(data_path)

dx = 1.03112519e1 #taille du pixel
dy = 7.19750606e1 #taille du pixel en y
nx = header["samples"]
ny = header["lines"]
x = np.arange(nx)*dx
y = np.arange(ny)*dy
X,Y = np.meshgrid(x,y)
Z = data.reshape(ny,nx)

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm

fig = plt.figure(0)
plt.clf()
plt.contourf(X,Y,Z,300,cmap = matplotlib.cm.terrain)
cbar = plt.colorbar()
cbar.set_label("Altitude, $z$ [m]")
plt.contour(X,Y,Z,50, colors = "k")
plt.grid()
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")
plt.show()



