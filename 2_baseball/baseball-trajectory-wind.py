import matplotlib.pyplot as plt 
import numpy as np
import math
# set up Constants
dt = 0.01 # time step interval, 
Vd = 35 # m/s
delta = 5 # m/s
grav = 9.8 # gravity, in m/1s

xylist = []
xylist.append([]) # no wind x 
xylist.append([]) # no wind y 
xylist.append([]) # tail wind x
xylist.append([]) # tail wind y
xylist.append([]) # head wind x
xylist.append([]) # head wind y


# initial settings
x = 0.0 # initial x position,
y = 1.0 # initial y position,
t = 0.0 # initial time
vTot = 49 # initial velocity,
vx = vTot * math.cos(math.radians(35)) 
vy = vTot * math.sin(math.radians(35))

# getNewV function calculates adjusted values for velocities in both x and y directions after applying wind drag
def getNewV (Vx, Vy, Vwind, xy):
    if xy == 0:
        WindDif = Vx-Vwind 
        V = Vx
    else:
        WindDif = Vy
        V = Vy
        V -= (grav*dt)
    Vadj = math.sqrt((Vx - Vwind)**2+Vy**2) # magnitude of total air Velocity adjusted with wind speed
    V -= windDrag(Vadj, WindDif) * (0.0039 + (0.0058/(1 + math.exp((Vadj - Vd)/delta)))) * dt 
    return V;

# calculates a portion of the wind drag effect 
def windDrag (Vadj, Winddif):
    drag = Vadj * Winddif
    return drag;

# resets main parameters to original values - called before each plot 
def reset():
    global x
    x = 0.0
    global y
    y = 1.0
    global vTot
    vTot = 49
    global vx
    vx = vTot * math.cos(math.radians(35))
    global vy
    vy = vTot * math.sin(math.radians(35))
    return;
    # ball with no wind 

while y > -5 :
    xylist[0].append(x) 
    xylist[1].append(y) 
    x += (vx * dt)
    y += (vy * dt)
    vx = getNewV(vx, vy, 0, 0) 
    vy = getNewV(vx, vy, 0, 1)

reset()
# ball with tail wind 
while y > -5 :
    xylist[2].append(x) 
    xylist[3].append(y) 
    x += (vx * dt)
    y += (vy * dt)
    vx = getNewV(vx, vy, 4.4, 0) 
    vy = getNewV(vx, vy, 4.4, 1)

reset()
# ball with head wind 
while y > -5 :
    xylist[4].append(x) 
    xylist[5].append(y) 
    x += (vx * dt)
    y += (vy * dt)
    vx = getNewV(vx, vy, -4.4, 0) 
    vy = getNewV(vx, vy, -4.4, 1)

#Set specifications for the plot's display plt.margins(0)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.yticks(ticks = (0,10,20,30))
plt.xticks(ticks = (0,50,100,150))
plt.title('Trajectory of a batted baseball') 
plt.plot(xylist[0],xylist[1],"-k",xylist[2],xylist[3],":k",xylist[4],xylist[5],"-.k",lw = 1) 
plt.annotate('headwind', xy=(103, 12), xytext=(85,8),
    arrowprops=dict(arrowstyle = '->',shrinkA = 10,
    connectionstyle = 'arc3,rad=-0.1'),ha='center',va = 'top') 
plt.annotate('tailwind', xy=(110, 18), xytext=(120,23),
    arrowprops=dict(arrowstyle = '->',shrinkA = 10,
    connectionstyle = 'arc3,rad=-0.1'),ha='center',va = 'bottom') 
plt.annotate('no wind', xy=(115, 8.5), xytext=(135,12),
    arrowprops=dict(arrowstyle = '->',shrinkA = 10,
    connectionstyle = 'arc3,rad=-0.1'),ha='center',va = 'bottom') 
plt.axis([0,150,0,30])
plt.tick_params(direction = 'in', right = True, top = True) 
plt.show()