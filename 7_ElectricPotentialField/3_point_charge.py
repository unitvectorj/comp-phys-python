# generates Figure 5.9 in Giordano
# by James Keen - 2/28/20

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# constants
x = np.linspace(-1,1,21)
y = np.linspace(-1,1,21)
X,Y = np.meshgrid(x,y)

# variables with initial values
count = 0
oldV = 0

# arrays
U = np.zeros((21,21))
W = np.zeros((21,21))
V = np.zeros((21,21,21))
V[10][10][10] = 1

while count < 150: # got this count through experimentation with Fig 5.5
    #the top section on z-plane
    for j in range(1,20):
        for i in range(1,10):
            k = 10
            V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    # negative y coordinates on x-z plane
    for j in range(1,10):
        i = 10
        k = 10
        V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    # positive coordinates on x-z plane
    for j in range(11,20):
        i = 10
        k = 10
        V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    # the bottom section on z-plane
    for j in range(1,20):
        for i in range(11,20):
            k = 10
            V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    # negative z coordinates for all x-y points
    for k in range(1,10):
        for j in range(1,20):
            for i in range(1,20):
                V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    # positive z coordinates for all x-y points
    for k in range(11,20):
        for j in range(1,20):
            for i in range(1,20):
                V[i][j][k] = (V[i+1][j][k] + V[i-1][j][k] + V[i][j+1][k] + V[i][j-1][k] + V[i][j][k+1] + V[i][j][k-1]) / 6
    count += 1

# creates two new arrays with averaged magnitudes for x (U) and y (W) directions, for plotting vectors in E-field plot




for j in range(0,20):
    for i in range(0,20):
        k=10 # just looking at the plane that will be plotted
        if j == 10: #for all the values along the center line
            if i < 10: # left of center
                U[i][j] = 0
                W[i][j] = -V[i][j][k]
            elif i == 10: # at very center
                U[i][j] = 0
                W[i][j] = 0
            else: # right of center
                U[i][j] = 0
                W[i][j] = V[i][j][k]
        elif j < 10: # above center line
            U[i][j] = -V[i][j][k] * (np.cos(np.arctan((-10+i)/(-10+j))))
            W[i][j] = -V[i][j][k] * (np.sin(np.arctan((-10+i)/(-10+j))))
        elif j > 10: # below center line
            U[i][j] = V[i][j][k] * (np.cos(np.arctan((-10+i)/(-10+j))))
            W[i][j] = V[i][j][k] * (np.sin(np.arctan((-10+i)/(-10+j))))








# this function sets all the parameters for the 2D plots
def setAxesParams(axis,limit,title,xlabel,ylabel):
    fsize = 6
    titlefsize = 7
    axis.set_xlim(-limit,limit)
    axis.set_ylim(-limit,limit)
    axis.tick_params(direction = 'in', top = True, right = True)
    axis.set_xticks([-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4])
    axis.set_xticklabels(['-.4','','-.2','','0','','0.2','','0.4'],fontsize = fsize)
    axis.set_yticks([-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4])
    axis.set_yticklabels(['-.4','','-.2','','0','','0.2','','0.4'],fontsize = fsize)
    axis.axhline(color='k',linewidth = 0.5)
    axis.axvline(color='k',linewidth = 0.5)
    axis.plot([-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4],[0,0,0,0,0,0,0,0],'|k',[0,0,0,0,0,0,0,0],[-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4],'_k',markersize = 2)
    axis.set_title(title,fontsize = titlefsize)
    axis.set_xlabel(xlabel,fontsize = fsize)
    axis.text(-limit-0.1,-0.05,'y',fontsize = fsize)
    return axis

# defines the figure and plots on it
fig = plt.figure(constrained_layout = True)
grid = fig.add_gridspec(5,4,wspace = 0.01,hspace = 0.01)

# the 3D plot
ax1 = fig.add_subplot(grid[0:3,2:4],projection = '3d')
ax1.autoscale_view()
ax1.margins(0)
ax1.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) #these set the background panes to be invisible
ax1.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.xaxis._axinfo["grid"]['color'] =  (1,1,1,0) #these set the background grid to be invisible
ax1.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax1.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax1.set_axis_off() #turns off the axis lines
xs = (0.8,-1.2,-1)
ys = (-1.3,0.3,-1)
zs = (0,0,1.1)
texts = ('x','y','V')
for i in range(0,3): #this takes the 4 lists above and places the labels in 3d-space
    ax1.text(xs[i],ys[i],zs[i],texts[i])
ax1.plot_surface(X,Y,V[:][10][:], edgecolor = 'black')
ax1.plot([-1,-1],[-1,-1],[0,1],'k') #this is the vertical line to the left of the 3d plot

# the Equipotential lines plot
ax2 = fig.add_subplot(grid[1:3,0:2], aspect = 'equal',autoscale_on = False)
ax2 = setAxesParams(ax2,0.4,'Electrical potential around a point charge in 3D','x','y')
lines = np.linspace(0,1,13)
ax2.contour(X,Y,V[:][:][10],lines)

# the E-field plot
ax3 = fig.add_subplot(grid[3:5,1:3], aspect = 'equal',autoscale_on = False)
ax3 = setAxesParams(ax3,0.5,'Field lines around a point charge in 3D','x','y')
ax3.quiver(X,Y,U,W,width = 0.01,scale = 1.5, scale_units = 'xy',pivot = 'tail')

plt.show()