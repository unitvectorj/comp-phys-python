# generates Figure 3.3 from Giordano
# James Keen - 2/3/2020

import matplotlib.pyplot as plt

# Constants
length = 1 # meters
dt = 0.04 # time step, in seconds
grav = 9.8 # gravity, in m/s^2

# Variables at initial value
omega = 0 #angular velocity, in radians/s
theta = 0.2 #angle, in radians
t = 0.0 #time, in seconds

# Arrays for data
theta_array = []
time_array = []

# this while loop performs all of the desired actions
while t <= 10.0:
    theta_array.append(theta)
    time_array.append(t)
    omega -= ((grav/length) * theta * dt)
    theta += (omega * dt)
    t += dt

# Plot display settings
plt.plot(time_array,theta_array)    
plt.axis([0,10,-0.3,0.3])
plt.xticks(ticks = (0,2,4,6,8,10))
plt.tick_params(direction = 'in', right = True, top = True)
plt.title('Simple Pendulum - Euler-Cromer method')
plt.text(1.9,0.24, "Length = 1m    time step = 0.04s")
plt.xlabel("time (s)")
plt.ylabel(r"$\dot{\Theta}$ (radians)")

plt.show()