# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:33:03 2020

@author: Atharva
"""

import numpy
from matplotlib import pyplot
import time ,sys



nx=81 # no. of points, try changing this no. from 41 to 81
nt=50  # no. of timesteps
dt =0.01 #amount of time each time step covers


dx = 2/(nx-1)

#Establishing initial conditions

u = numpy.ones(nx)  # setting every value of array nx elements long as one

u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
print(u)      
    
pyplot.plot(numpy.linspace(0, 2, nx), u);

#Establishing finite difference method 

un = numpy.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()    #copying the existing values of u into un
    for i in range(1, nx): 
    #for i in range(nx):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx), u);
 
'''
CONCLUSION

As the no. of sampling points increase the two graphs seem to converge better

'''