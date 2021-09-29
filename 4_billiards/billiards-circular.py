# generates Figure 3.22-left from Giordano
#James Keen 2/7/20

import matplotlib.pyplot as plt
import numpy as np

#set up constants
r = 1
Vtot = 1
dt = 0.01

#set up variables with initial values
x = 0.2
y = 0
t = 0
Vx = Vtot * np.cos(np.pi/7.85)
Vy = Vtot * np.sin(np.pi/7.85)
x_array = []
y_array = []
oldX = 0
oldY = 0

#set up arrays for drawing the circle halves
circleX = np.linspace(-1,1,401)
circleY = np.sqrt(r**2 - circleX**2)
circleY2 = -circleY

# the main loop which will calculate all points for the trajectory plot
while t < 61.2:
    oldX = x
    oldY = y
    x_array.append(x)
    y_array.append(y)
    x += Vx * dt
    y += Vy * dt
    dist = np.sqrt(x**2 + y**2)
    
    if (dist >= r): # if the 'ball' goes outside the wall
        # the following if and while blocks move the ball back and reapproach the wall at a smaller timestep to get as close as possible
        if (dist - r > 0.000001):
            x = oldX
            y = oldY
        while ((r-dist) > 0.000001):
            x += (Vx * dt**2)
            y += (Vy * dt**2)
            dist = np.sqrt(x**2 + y**2)
            
        # then all the necessary angles and new velocity components are calculated
        normAngle = np.arctan2(y,x) + np.pi
        velAngle = np.arctan2(Vy,Vx) + np.pi
        angleDiff = velAngle - normAngle
        velAngle = normAngle - angleDiff
        Vx = Vtot * np.cos(velAngle)
        Vy = Vtot * np.sin(velAngle)
    t += dt    
    
# here the circles and trajectory are plotted
plt.plot(circleX,circleY,'.k',circleX,circleY2,'.k',x_array, y_array, '.k',markersize = 1)

# the labels and ticks are defined here
plt.axis([-1,1,-1,1],'equal', 'box')
plt.xticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.yticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.tick_params(direction = 'in', right = True, top = True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circular stadium - trajectory')

plt.show()