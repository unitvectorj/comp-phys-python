# generates Figure 3.22-right from Giordano
#James Keen 2/10/20

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#set up constants
r = 1
alpha = 0.01
Vtot = 1
dt = 0.01

#set u p circle parts
circleX = np.linspace(-1,1,401)
circleY = np.sqrt(r**2 - circleX**2) + alpha
circleY2 = -circleY - alpha

#set up variables with initial states
x = 0.2
y = 0
t = 0
Vx = Vtot * np.cos(np.pi/7.9)
Vy = Vtot * np.sin(np.pi/7.9)
x_array = []
y_array = []
oldX = 0
oldY = 0
yAdj = 0
num = 0
frames = []
fig = plt.figure()
# this is the main loop for plotting all the points
while t < 80:
    oldX = x
    oldY = y
    
    
    x_array.append(x)
    y_array.append(y)
    frame = plt.plot(x_array,y_array, markersize = 1,animated = True)
    frames.append(frame)
    x += Vx * dt
    y += Vy * dt
    # these ifs calculate if the 'ball' has gone over the edge and the normal angle at the point of contact
    if (y > alpha):
        yAdj = y-alpha
    elif (y < -alpha):
        yAdj = y+alpha
    elif(y < alpha and y > -alpha):
        yAdj = 0
    dist = np.sqrt(x**2 + yAdj**2)
    if (dist >= r):
        #this if and while block checks if the 'ball' has gone over the edge, backtracks, then takes much smaller steps to get as close to the edge as possible
        if (dist-r > 0.0000001):
            x = oldX
            y = oldY
        while ((r-dist) > 0.0000001):
            x += (Vx * dt**3)
            y += (Vy * dt**3)
            if (y > alpha):
                yAdj = y-alpha
            elif(y < -alpha):
                yAdj = y+alpha
            elif(y < alpha and y > -alpha):
                yAdj = 0
            dist = np.sqrt(x**2 + yAdj**2)
        normAngle = np.arctan2(yAdj,x) + np.pi # once the point of hitting the wall is calculated, the normal angle is calculated
        # then these set the new angle for the trajectory
        if (y > alpha or y < -alpha): # if the ball is in the circular parts
            velAngle = np.arctan2(Vy,Vx) + np.pi
            angleDiff = velAngle - normAngle
            velAngle = normAngle - angleDiff
            Vx = Vtot * np.cos(velAngle)
            Vy = Vtot * np.sin(velAngle)
        elif (y <= alpha and y >= -alpha): # if the ball is in the flat part
            Vx = -Vx
    t += dt  
    
# plots the circle halves and the trajectory
#plt.plot(circleX,circleY,'.k',circleX,circleY2,'.k',x_array, y_array, '.k', markersize = 1)

# these set the label and tick values and positions
plt.axis([-1.1,1.1,-1.1,1.1],'equal')
plt.xticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.yticks(ticks = [-1,-0.5,0,0.5,1],labels = ['-1','-0.5','0','0.5','1'])
plt.tick_params(direction = 'in', right = True, top = True)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Stadium billiard  $\alpha$ = 0.01')
ani = animation.ArtistAnimation(fig, frames, interval=5, blit = True,
                                repeat_delay=1000)

plt.show()
