# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:19:17 2020

@author: Atharva
"""

import numpy                 
from matplotlib import pyplot   


nx = 81
dx = 2 / (nx - 1)
nt = 20    #the number of timesteps 
nu = 0.3   #the value of viscosity
sigma = .2 
dt = sigma * dx**2 / nu 


u = numpy.ones(nx)      #a numpy array with nx elements all equal to 1.
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

un = numpy.ones(nx) #placeholder array to advance the solution in time

for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx), u);

