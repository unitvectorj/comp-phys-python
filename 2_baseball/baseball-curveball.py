import matplotlib.pyplot as plt
import numpy as np
import math

# set up Constants
dt = 0.01 # time step interval, in seconds
Vd = 35 # m/s
delta = 5 # m/s
grav = 9.8 # gravity, in m/s
omega = 60 * math.pi # angular velocity, in radians/s
SoM = 0.00041 # S sub 0 divided by mass, as given in the text

# initialize array of arrays to hold x,y,z values
xyzlist = []
xyzlist.append([]) # x
xyzlist.append([]) # y
xyzlist.append([]) # z

# initial settings
x = 0.0 # initial x position, in meters
y = 1.0 # initial y position, in meters
z = 0.0 # initial z position, in meters
t = 0.0 # initial time
vx = 31.3 # initial velocity, in m/s (70 mph)
vy = 0.0 # initial velocity
vz = 0.0 # initial velocity
Vtot = math.sqrt( vx**2 + vy**2 + vz**2)

# getNewV function calculates adjusted values for velocities in both x and y directions after applying wind drag
def getNewV (Vtot, Vx, Vy, Vz, xyz):
    if xyz == 0: # x
        V = Vx
        V -=  Vtot * Vx * (0.0039 + (0.0058/(1 + math.exp((Vtot - Vd)/delta)))) * dt
    elif xyz == 1: # y
        V = Vy
        V -= (grav*dt)
    elif xyz == 2: # z
        V = Vz
        V += SoM * omega * Vx * dt
    return V;

while x < 17 :
    #convert coordinates into feet for plotting
    Xfeet = x * 3.28084
    Yfeet = y * 3.28084
    Zfeet = z * 3.28084
    xyzlist[0].append(Xfeet)
    xyzlist[1].append(Yfeet)
    xyzlist[2].append(Zfeet)
    x += (vx * dt)
    y += (vy * dt)
    z += (vz * dt)
    Vtot = math.sqrt( vx**2 + vy**2 + vz**2)
    vx = getNewV(Vtot, vx, vy, vz, 0)
    vy = getNewV(Vtot, vx, vy, vz, 1)
    vz = getNewV(Vtot, vx, vy, vz, 2)

#Set specifications for the plot's display
plt.margins(0)
plt.xlabel('x (feet)')
plt.ylabel('y or z (feet)')
plt.vlines(0,-3,3.5, linewidth = .5, linestyle = 'dashed')
plt.vlines(60,-3,3.5, linewidth = .5, linestyle = 'dashed')
plt.yticks(ticks = (-4,-2,0,2,4))
plt.xticks(ticks = (0,20,40,60))
plt.title('Sidearm curve ball')
plt.plot(xyzlist[0],xyzlist[1],":k",xyzlist[0],xyzlist[2],"-k",lw = 1)
plt.annotate('pitcher', xy=(0.5,-1.8), xytext=(8,-3),
            arrowprops=dict(arrowstyle = '->',shrinkA = 10,
            connectionstyle = 'arc3,rad=0.1'),ha='center',va = 'top')
plt.annotate('home plate', xy=(59.5, -2.2), xytext=(50,-3),
            arrowprops=dict(arrowstyle = '->',shrinkA = 10,
            connectionstyle = 'arc3,rad=-0.1'),ha='center',va = 'top')
plt.annotate('horizontal deflection (z)', xy=(28, 0.2), xytext=(23,-0.8),
            arrowprops=dict(arrowstyle = '->',shrinkA = 10,
            connectionstyle = 'arc3,rad=0.1'),ha='center',va = 'bottom')
plt.annotate('vertical deflection (y)', xy=(31, 1.7), xytext=(35,2.8),
            arrowprops=dict(arrowstyle = '->',shrinkA = 10,
            connectionstyle = 'arc3,rad=-0.1'),ha='center',va = 'bottom')
plt.axis([-5,65,-4,4])
plt.tick_params(direction = 'in', right = True, top = True)
plt.show()