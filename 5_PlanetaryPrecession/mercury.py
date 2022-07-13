# generates Fig 4.8 in Giordano
# James Keen - 2/14/20

import matplotlib.pyplot as plt
import numpy as np

# constants
pi = np.pi
dt = 0.0001 # time step, in years
alpha = 0.01

# variables, with initial values
x = 0.47 # AU
y = 0    # AU
Vx = 0   # in AU/year
Vy = 8.2 # in AU/year 
t = 0
oldR = 0
r = 0
flip = True
count = 0

# empty arrays for x,y positional data
x_array = []
y_array = []

# this loop calculates the positional data for each time step and populates the arrays to be plotted
while t < 1:
    
    oldR = r
    x_array.append(x)
    y_array.append(y)
    
    r = np.sqrt(x**2 + y**2)
    
    #this if elif determines where the max r's are, and draws a line to that spor each time
    if oldR > r and flip == False and t > 0.2:
        xx = np.linspace(0,x,100)
        yy = np.linspace(0,y,100)
        plt.plot(xx,yy,'k')
        flip = True    
    elif oldR < r:
        flip = False
    
    
    Vx -= ((4 * pi**2 * x) / r**3) * (1 + alpha/r**2) * dt
    Vy -= ((4 * pi**2 * y) / r**3) * (1 + alpha/r**2) * dt
    
    x += Vx * dt
    y += Vy * dt
    
    t += dt

# set up the figure parameters and plot the data
#plt.figure(figsize = (5,5))
plt.plot(x_array,y_array,'k')
plt.axis([-0.6,0.6,-0.6,0.6],'equal')
plt.title('Simulation of the precession of Mercury')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.text(-0.1,0.5,r'$\alpha$ = 0.01',fontsize = 12)
plt.xticks(ticks = [-0.5,0,0.5])
plt.yticks(ticks = [-0.5,0,0.5])
plt.tick_params(direction = 'in', right = True, top = True)
plt.show()
