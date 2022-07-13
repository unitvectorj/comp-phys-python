# generates Fig 4.12 right in Giordano
# James Keen - 2/19/20

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim

# constants
pi = np.pi
dt = 0.01 # time step, in years
Jmass = 0.0095 # 10 times mass of Jupiter as a ratio of Sun's mass 1.9 x 10^27 / 2.0 x 10^30
Emass = 0.000003 # mass of Earth as a ratio of Sun's mass 
# the following 3 are calculated here to save from having to be calculated at each time step
GMs = 4 * pi**2 
GMsMj = 4 * pi**2 * Jmass 
GMsMe = 4 * pi**2 * Emass 

# variables, with initial values
Ex = 1
Ey = 0
EVx = 0
EVy = 2 * pi
Jx = 5
Jy = 0
JVx = 0
JVy = 0.9045 * pi # obtained this by trial and error
t = 0

# empty arrays for x,y positional data
Ex_array = []
Ey_array = []
Jx_array = []
Jy_array = []







# this loop calculates the positional data for each time step and populates the arrays to be plotted
while t < 12:
    
    # populate the position arrays for Earth
    Ex_array.append(Ex)
    Ey_array.append(Ey)
    
    # populate the position arrays for Jupiter
    Jx_array.append(Jx)
    Jy_array.append(Jy)
    
    # calculate radii at each time step
    Er = np.sqrt(Ex**2 + Ey**2)
    Jr = np.sqrt(Jx**2 + Jy**2)
    EJr = np.sqrt((Ex-Jx)**2 + (Ey-Jy)**2)
    
    # calculate Earth's component velocities
    EVx -= (((GMs * Ex) / (Er**3)) + ((GMsMj * (Ex-Jx))/(EJr**3))) * dt
    EVy -= (((GMs * Ey) / (Er**3)) + ((GMsMj * (Ey-Jy))/(EJr**3))) * dt
    
    # calculate Jupiter's component velocities
    JVx -= (((GMs * Jx) / (Jr**3)) + ((GMsMe * (Jx-Ex))/(EJr**3))) * dt
    JVy -= (((GMs * Jy) / (Jr**3)) + ((GMsMe * (Jy-Ey))/(EJr**3))) * dt
    
    # gives Earth's new position
    Ex += EVx * dt
    Ey += EVy * dt
    
    # gives Jupiter's new position
    Jx += JVx * dt
    Jy += JVy * dt
    
    t += dt

# set up the figure parameters and plot the data
plt.figure(figsize = (5,5))
plt.plot(Ex_array,Ey_array, '.k', Jx_array, Jy_array,'.k',markersize = 1.5)
plt.axis([-7,7,-7,7],'equal')
plt.hlines(0,-7,7,'k',linestyles = 'dotted')
plt.vlines(0,-7,7,'k',linestyles = 'dotted')
plt.title('3-Body Simulation   Earth plus Jupiter')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.text(-6.5,6,'Mass of Jupiter',fontsize = 12)
plt.text(-5.1,5.1,r'= 10 $\mathrm{M_J}$', fontsize = 12)
plt.xticks(ticks = [-5,0,5],labels = ['-5','0','5'])
plt.yticks(ticks = [-5,0,5],labels = ['-5','0','5'])
plt.tick_params(direction = 'in', right = True, top = True)
plt.show()
