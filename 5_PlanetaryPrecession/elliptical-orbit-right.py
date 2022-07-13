# generates Fig 4.6 right in Giordano
# James Keen - 2/14/20

import matplotlib.pyplot as plt
import numpy as np

# constants
pi = np.pi
dt = 0.001 # time step, in years

# variables, with initial values
x = 1
y = 0
Vx = 0
Vy = 1.5 * pi
t = 0
beta = 2.01

# empty arrays for x,y positional data
x_array = []
y_array = []

# this loop calculates the positional data for each time step and populates the arrays to be plotted
while t < 3.5:
    
    x_array.append(x)
    y_array.append(y)
    
    r = np.sqrt(x**2 + y**2)
    
    Vx -= ((4 * pi**2 * x) / (r**beta * r)) * dt
    Vy -= ((4 * pi**2 * y) / (r**beta * r)) * dt
    
    x += Vx * dt
    y += Vy * dt
    
    t += dt


# set up the figure parameters and plot the data
plt.figure(figsize = (5,5))
plt.plot(x_array,y_array, '.k', markersize = 0.9)
plt.axis([-1,1,-1,1],'equal')
plt.hlines(0,-1,1,'k',linestyles = 'dotted')
plt.vlines(0,-1,1,'k',linestyles = 'dotted')
plt.title('Simulation of elliptical orbit')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.text(-0.75,0.8,r'$\beta$ = 2.01',fontsize = 12)
plt.xticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.yticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.tick_params(direction = 'in', right = True, top = True)
plt.show()
