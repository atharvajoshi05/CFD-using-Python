# -*- coding: utf-8 -*-
"""
2D Steady State Diffusion with Source Term

Top Wall kept at 1, remaining walls at 0

"""


import numpy as np
import matplotlib.pyplot as plt

# Number of grid points
N = 101

# Domain size
L = 1

# Corresponding grid spacing
h = np.float64(L/(N-1))

# Iteration number
iterations = 0

# Thermal conductivity
k = 0.1;

# Cross-section area
A = 0.001;

# Source
q = 50; #in W/m3

# Initializing temperature field
T = np.zeros((N,N))
T[0,:] = 1. #Top Wall
T[1,:] = 1.
T[:,0] = 1.
T[:,1] = 1.
# Initializing iterated temperature
T_new = np.zeros((N,N))
T_new[0,:] = 1.
T_new[1,:] = 0.
T_new[:,0] = 0.
T_new[:,1] = 0.


# Error related variables
epsilon = 1.E-8
numerical_error = 1

# Plot for numerical error
plt.figure(10)

# Checking the error tolerance
while numerical_error > epsilon:
    # Computing for all interior points
    for i in range(1,N-1):
        for j in range(1,N-1):
            a_E = np.float64(k*A/h)
            a_W = np.float64(k*A/h)
            a_N = np.float64(k*A/h)
            a_S = np.float64(k*A/h)
            a_P = a_E + a_W + a_N + a_S
            T_new[i,j] = (a_E*T[i,j+1]+a_W*T[i,j-1]+a_N*T[i-1,j]+a_S*T[i+1,j] + h*q*A)/a_P
    
    # Resetting the numerical error and recalculate
    numerical_error = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            numerical_error = numerical_error + abs(T[i,j] - T_new[i,j])
     
    # Iteration advancement and reassignment
    iterations = iterations + 1
    T = T_new.copy()
    
    # Plotting numerical error
    if iterations%500 ==0:
        plt.figure(10)
        plt.semilogy(iterations, numerical_error, 'ko')
        plt.pause(0.01)
    
# Plotting the results

# Defining the position vector and the grid from indices
x_dom = np.arange(N) * h
y_dom = L - np.arange(N) * h
[X, Y] = np.meshgrid(x_dom, y_dom)

# Plotting the variation as a contour
plt.figure(11)
plt.contourf(X, Y, T, 12)

# Displaying the colorbar
plt.colorbar(orientation='vertical')

# Displaying the gridlines
plt.grid(True, color='k')

# Providing a title to the plot
plt.title("T(x,y)")

# Showing the plot on screen
plt.show()
