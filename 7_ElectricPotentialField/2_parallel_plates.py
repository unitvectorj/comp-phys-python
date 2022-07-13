# generates Figure 5.7 in Giordano
# by James Keen - 2/27/20

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
V = np.zeros((21,21))
for i in range(8,13):
    V[i][7] = 1
    V[i][13] = -1

while count < 150: # got this count through experimentation with Fig 5.5
    #the top section
    for j in range(1,20):
        for i in range(1,8):
            V[i][j] = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]) / 4
    #the section left of both plates
    for j in range(1,7):
        for i in range(7,14):
            V[i][j] = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]) / 4
    # the section between the plates
    for j in range(8,13):
        for i in range(7,14):
            V[i][j] = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]) / 4
    # the section right of the plates
    for j in range(14,20):
        for i in range(7,14):
            V[i][j] = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]) / 4
    # the bottom section
    for j in range(1,20):
        for i in range(13,20):
            V[i][j] = (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1]) / 4
    count += 1

# creates two new arrays with averaged magnitudes for x (U) and y (W) directions, for plotting vectors in E-field plot
for j in range(0,20):
    for i in range(0,20):
        U[i][j] = (V[i][j-1] - V[i][j+1])/2
        W[i][j] = (V[i-1][j] - V[i+1][j])/2

# this function sets all the parameters for the 2D plots
def setAxesParams(axis,limit,title,xlabel,ylabel):
    fsize = 6
    axis.set_xlim(-limit,limit)
    axis.set_ylim(-limit,limit)
    axis.tick_params(direction = 'in', top = True, right = True)
    axis.set_xticks([-1,-0.5,0,0.5,1])
    axis.set_xticklabels(['-1','','0','','1'],fontsize = fsize)
    axis.set_yticks([-1,-0.5,0,0.5,1])
    axis.set_yticklabels(['-1','','0','','1'],fontsize = fsize)
    axis.axhline(color='k',linewidth = 0.5)
    axis.axvline(color='k',linewidth = 0.5)
    axis.plot([-1,-0.5,0.5,1],[0,0,0,0],'|k',[0,0,0,0],[-1,-0.5,0.5,1],'_k',markersize = 2)
    axis.set_title(title,fontsize = fsize)
    axis.set_xlabel(xlabel,fontsize = fsize)
    axis.text(-limit-0.3,-0.05,'y',fontsize = fsize)
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
xs = (0.8,-1.2,-1,-1)
ys = (-1.3,-0.6,-1,-1)
zs = (0,0,-1.1,1.1)
texts = ('x','y','V=-1','V=1')
for i in range(0,4): #this takes the 4 lists above and places the labels in 3d-space
    ax1.text(xs[i],ys[i],zs[i],texts[i])
ax1.plot_surface(X,Y,V, edgecolor = 'black')
ax1.plot([-1,-1],[-1,-1],[-1,1],'k') #this is the vertical line to the left of the 3d plot

# the Equipotential lines plot
ax2 = fig.add_subplot(grid[1:3,0:2], aspect = 'equal',autoscale_on = False)
ax2 = setAxesParams(ax2,1.2,'Electrical potential near two metal plates','x','y')
lines = np.linspace(-1.0000001,0.9999999,12)
ax2.contour(X,Y,V,lines)

# the E-field plot
ax3 = fig.add_subplot(grid[3:5,1:3], aspect = 'equal',autoscale_on = False)
ax3 = setAxesParams(ax3,1.5,'Electric field near two metal plates','x','y')
widths = np.hypot(U,W)
widths = widths.flatten()
ax3.quiver(X[1::2,1::2],Y[1::2,1::2],U[1::2,1::2],W[1::2,1::2],angles = 'xy',scale = 2, scale_units = 'xy',pivot = 'tail')

plt.show()