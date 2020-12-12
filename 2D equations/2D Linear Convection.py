# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:20:55 2020

@author: Atharva

"""
from mpl_toolkits.mplot3d import Axes3D   #New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm


#variable declarations
nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx)) #create a 1xn vector of 1's
un = numpy.ones((ny, nx)) 

#Assign initial conditions
#set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) as 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 

#Plot Initial Conditions

fig = pyplot.figure(figsize=(11, 7), dpi=100)  # specifying the size and resolution
ax = fig.gca(projection='3d')                      
X, Y = numpy.meshgrid(x, y)     # generating a mesh grid for 3D plotting                       
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

# Applying BCs using For Loops

u = numpy.ones((ny, nx))
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): #loop across number of time steps
    un = u.copy()
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j, i] = (un[j, i] - (c * dt / dx * (un[j, i] - un[j, i - 1])) -
                                  (c * dt / dy * (un[j, i] - un[j - 1, i])))
            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

# Applying BCs using Array Operations

'''
u = numpy.ones((ny, nx))
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

'''
