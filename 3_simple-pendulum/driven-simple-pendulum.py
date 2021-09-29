# generates the right-most image of Figure 3.6 from Giordano
# James Keen - 2/6/2020

import matplotlib.pyplot as plt
import numpy as np
import math

# Constants
length = 9.8 # meters
dt = 0.04 # time step, in seconds
grav = 9.8 # gravity, in m/s^2
q = 0.5 # proportionality constant 
Omd = (2/3)  # big Omega sub D (driving frequency)

# Variables at initial value
omega1, omega2, omega3 = 0, 0, 0 # angular velocities, in radians/s
theta1, theta2, theta3 = 0.2, 0.2, 0.2 # angles, in radians
Fd1, Fd2, Fd3 = 0.0, 0.5, 1.2 # Driving Force in radians/s^2
t = 0.0 #time, in seconds

# Arrays for data
time_array = []
omega1_array = []
omega2_array = []
omega3_array = []

# this while loop performs all the calculations for each array at each time step
while t <= 60.0:
    time_array.append(t) # adds an element for each time step (will be used to plot all three data sets)
    
    # builds omega array for plot 1 (Fd1 = 0.0)
    omega1_array.append(omega1)
    omega1 -= (((grav/length) * math.sin(theta1)) + (q * omega1) - (Fd1 * math.sin(Omd * t))) * dt
    theta1 += (omega1 * dt)
    
    # builds omega array for plot 2 (Fd2 = 0.5)
    omega2_array.append(omega2)
    omega2 -= (((grav/length) * math.sin(theta2)) + (q * omega2) - (Fd2 * math.sin(Omd * t))) * dt
    theta2 += (omega2 * dt)
    
    # builds omega array for plot 3 (Fd3 = 1.2)
    omega3_array.append(omega3)
    omega3 -= (((grav/length) * math.sin(theta3)) + (q * omega3) - (Fd3 * math.sin(Omd * t))) * dt
    theta3 += (omega3 * dt)
    
    t += dt

# adjust array values in order to plot them with different origin points
omega1_array = [x + 7 for x in omega1_array]
omega2_array = [x + 6 for x in omega2_array]
omega3_array = [x + 3 for x in omega3_array]

# Plot display settings
plt.plot(time_array,omega1_array,'-k',time_array,omega2_array,'-k',time_array,omega3_array,'-k')
plt.axis([0,60,0,8])
plt.yticks(np.arange(9),('','','-1','0','1','','0','0','1'))
plt.xticks(ticks = [0,20,40,60])
plt.title(r"$\dot{\omega}$ versus time", fontsize = 10)
plt.text(46,7.3, r"$\mathrm{F_D}$ = 0", fontsize = 12)
plt.text(46,5, r"$\mathrm{F_D}$ = 0.5", fontsize = 12)
plt.text(40,1.3, r"$\mathrm{F_D}$ = 1.2", fontsize = 12)
plt.xlabel("time (s)")
plt.ylabel(r"$\dot{\omega}$ (radians/s)")
plt.tick_params(direction = 'in', right = True, top = True)

plt.show()