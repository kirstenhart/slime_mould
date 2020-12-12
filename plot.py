# -*- coding: utf-8 -*-

# Creates plot of Region and Planned Path
# 
# To test code, just run "plot()" 
# x1,x2 are set to default values
# function set to Ackley by default
#
# To run real values run:
# plot(x1,x2,f)
# f = local min function, values below
# LocMinFuncs.ackley
#            .bukin6
#            .crossit
#            .drop
#            .egg
#
import numpy as np
import matplotlib.pyplot as plt
import LocMinFuncs


#create grid of loc min function
def get_grid(x1 = np.linspace(-5,5,31), x2 = np.linspace(-5,2.5,31), f = LocMinFuncs.ackley):
    y = []
    # print(x1)
    # x1 = np.sort(x1)
    # x2 = np.sort(x2)
    # print(x2)
    x1_max = np.max(x1)
    x2_max = np.max(x2)
    x1_min = np.min(x1)
    x2_min = np.min(x2)
    x1 = np.linspace(x1_min,x1_max,len(x1))
    x2 = np.linspace(x2_min,x2_max,len(x2))#[::-1]
    # print(x2)
    # print(x1)
    for x_1 in x1:
        for x_2 in x2:
            y.append(f((x_1,x_2))) 
    y = np.array(y).reshape(len(x1),len(x2))
    
    return x1,x2,y

#func takes in two 1D arrays and returns y
def loc_min_func(x1,x2,f):
    y = []
    # path = np.stack((x1,x2))
    for i in range(len(x1)):
        y.append(f((x1[i],x2[i])))
    return y

#create plot
def get_plot(x1,x2, y, Y, new_x1, new_x2):
    # fig = plt.figure()
    fig, ax = plt.subplots(1,1)
    ax = plt.axes(projection='3d')
    #First plot the loc min func
    # print("Y is this:",y)
    # print(y.shape)
    cont = ax.contour3D(new_x1, new_x2, y, 50, cmap='spring')
    # ax.plot_surface(x1, x2, y, cmap='spring',linewidth=0, antialiased=False)
    # ax.plot_wireframe(x1, x2, y, rstride=10, cstride=10)
    
    # Second, plot the scatter of UAV path.
    ax.scatter(x1,x2,Y,c='b')#,cmap='Blues')
    # ax.plot(x1,x2,Y,'-o')
        #axis labels
    ax.set_xlabel('x2')
    ax.set_ylabel('x1')
    ax.set_zlabel('y')
    ax.legend(labels=("Path","Y"))
    fig.colorbar(cont)
    ax.view_init(30, 210)
    
    
    #get total distance
    
def get_dist(x1,x2,Y):
    euc = []
    for i in range(1,len(x1)):
        step = np.sqrt((x1[i]-x1[i-1])**2 + (x2[i]-x2[i-1])**2 + (Y[i]-Y[i-1])**2)
        euc.append(step)
    dist = sum(euc)
    return dist

def plot(x1 = np.linspace(-5,1,50), x2 = np.linspace(5,1,50), f = LocMinFuncs.ackley):
    #initialize test values and function
    # x1 = np.linspace(-40,40,100) #1x40
    # x2 = np.linspace(-40,20,100) #1x40
    # f = LocMinFuncs.ackley

    # little y creates plot of function
    new_x1, new_x2, y = get_grid(x1,x2,f)
    # y = get_grid()
    # big Y => Planned Path
    Y = loc_min_func(x1,x2,f)
    dist = get_dist(x1,x2,Y)
    # print(dist)
    #create plot
    get_plot(x1,x2, y, Y, new_x1, new_x2)
    return dist
