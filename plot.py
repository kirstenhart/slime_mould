# -*- coding: utf-8 -*-

# Creates plot of Region and Planned Path

import numpy as np
import matplotlib.pyplot as plt
import LocMinFuncs


#create grid of loc min function
def get_grid(x1,x2,f):
    y = []
    for x_1 in x1:
        for x_2 in x2:
            y.append(f((x_1,x_2)))
    y = np.array(y).reshape(len(x1),len(x2))
    
    return y

#func takes in two 1D arrays and returns y
def loc_min_func(x1,x2,f):
    y = []
    # path = np.stack((x1,x2))
    for i in range(len(x1)):
        y.append(f((x1[i],x2[i])))
    return y

#create plot
def get_plot(x1,x2, y, Y):
    # fig = plt.figure()
    ax = plt.axes(projection='3d')
    #First plot the loc min func
    ax.contour3D(x1, x2, y, 25, cmap='spring')
    # Second, plot the scatter of UAV path.
    ax.scatter(x1,x2,Y,c='b')#,cmap='Blues')
        #axis labels
    ax.set_xlabel('x2')
    ax.set_ylabel('x1')
    ax.set_zlabel('y')
    
def plot(x1 = np.linspace(-40,40,100), x2 = np.linspace(-40,20,100), f = LocMinFuncs.ackley):
    #initialize test values and function
    # x1 = np.linspace(-40,40,100) #1x40
    # x2 = np.linspace(-40,20,100) #1x40
    # f = LocMinFuncs.ackley

    # little y creates plot of function
    y = get_grid(x1,x2,f)
    # big Y => Planned Path
    Y = loc_min_func(x1,x2,f)
    #create plot
    get_plot(x1,x2, y, Y)