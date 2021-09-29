import matplotlib.pyplot as plt

# set up Constants
po = 400 # Power, in Watts
dt = 0.1 # time step interval, in seconds
m = 70 # mass, in kg
A = 0.33 # cross-sectional area of bicycle and rider, in m^3
C = 1 # drag coefficient
rho = 1.225 # air density in kg/m^3

#set up initial parameters
v1 = 4.0 # initial velocity, in m/s
v2 = 4.0 # initial velocity, in m/s
t1 = 0.0 # initial time, for plot 1
t2 = 0.0 # initial time, for plot 2

#Initialize list to track time and velocity data for each timestep for each plot
t1list = []
v1list = []
t2list = []
v2list = []

# airdrag() calculates the Fdrag given velocity, the drag coefficient C, air density, cross-sectional area, mass of moving body, and the timestep
def airdrag (vel, coef, dens, area, mass, timestep):
    drag = (((coef*dens*area*vel*vel)/(2*mass))*timestep)
    return drag;

while t1 < 200:
    #create data for plot 1 at time interval of 0.05s
    v1list.append(v1)
    t1list.append(t1)
    v1 = v1+((po/(m*v1))*dt) #does not include air drag
    t1 += dt
    

while t2 < 200: 
    #create data for plot 2 at time interval of 0.1s
    v2list.append(v2)
    t2list.append(t2)
    v2 = v2+((po/(m*v2))*dt)-airdrag(v2,C,rho,A,m,dt) #does include air drag
    t2 += dt

#Set specifications for the plot's display
plt.margins(0)
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')
plt.title('Bicycle simulation: velocity vs. time')
plt.plot(t1list,v1list,"-b",t2list,v2list,':r')
plt.text(10,35,'No air resistance')
plt.text(75,7,'With air resistance')
plt.axis([0, 200,0,50])
plt.tick_params(direction = 'in', right = True, top = True)
plt.show()

