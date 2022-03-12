# -*- coding: utf-8 -*-
"""
1D Diffusion with Neumann BC dT/dx=0 on left boundary.

"""

import numpy as np
import matplotlib.pyplot as plt

#Number of Grid Points
N = 101 

#Domain Size
L = 1 

#Corresponding Grid Spacing
h = np.float64(L/(N-1))

#Thermal Conductivity
k = 0.1;

#Cross Section Area
A = 0.001;

#Iteration Number
iterations = 0

#Initializing Temperature Field
T = np.zeros(N)
T[N-1] = 1.
#Initializing Iterated Temperature
T_new = np.zeros(N)
T_new[N-1] = 1.

#Error related variables
epsilon = 1.E-8
numerical_error = 1

#Checking the error tolerance
while numerical_error > epsilon:
    #Computing for all interior points
    for i in range(0,N-1):  #starting from zero since we need to take care of the Neumann boundary
        a_E = np.float64(k*A/h)
        a_W = np.float64(k*A/h)
        if i==0: 
            a_W = 0 #treatment for neumann boundary
        a_P = a_E + a_W
        T_new[i] = (a_E*T[i+1]+a_W*T[i-1])/a_P
    
    #Resetting the numerical error and recalculate
    numerical_error = 0
    for i in range(1,N-1):
        numerical_error = numerical_error + abs(T[i]-T_new[i])
        
    #Iteration Advancement and Reassignment
    iterations = iterations + 1
    T = T_new.copy()
    
#Plotting the results
plt.figure()

#Defining the position from indexes
x_dom = np.arange(N) * h

#Plotting the variation with customization
plt.plot(x_dom, T, 'gx--', linewidth=2, markersize=10)

# Displaying the gridlines
plt.grid(True, color='k')

#Labelling and providing a title to the plot
plt.xlabel('Position', size=10)
plt.ylabel('Temperature', size=10)
plt.title('T(x)')
plt.axis([None, None, 0, 1])

#Showing the plot on screen
plt.show()   


