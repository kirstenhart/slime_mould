 # -*- coding: utf-8 -*-

# SMA Test

import numpy as np
from SMA import BaseSMA, OriginalSMA
import LocMinFuncs
import plot
from GWO import GreyWolf

#to modify starting point, update 'pos' in path() func call
def path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos = np.array([-6,6]), Alg="SMA"):
    p=[]
    p.append(pos)
    resolution = 5
    # resolution = 10
    bnd = np.array([ub,lb]) #bounds
    # while True: 
    for i in range(10): #number of steps to take
        # print("****** i *****:", i)
        # if np.any(np.abs(pos)) > 6:
        #     resolution = 5
        # # elif np.any(np.abs(pos)) > 1:
        # #     resolution = 6.3
        # else:
        #     resolution = 6.3
            
        # regional area size
        m_ub = list((bnd/resolution + pos)[0])
        m_lb = list(pos-100)
        #previous working line
        # m_lb = list((bnd/resolution + pos)[1])
        
        # for j in range(0,2):
        #     m_ub.append(ub[j]/resolution + pos[j])
        #     m_lb.append(lb[j]/resolution + pos[j])
        # print(m_ub,"\n",m_lb,"\n")
        if Alg == "SMA":
            md1 = BaseSMA(obj_func, m_lb, m_ub, problem_size, verbose, epoch, pop_size)
            best_pos1, best_fit1, list_loss1, time_elapsed1  = md1.train()
            pos = md1.solution[0]
            p.append(pos)
        if Alg == "GWO":
            md3 = GreyWolf(obj_func, m_lb, m_ub, problem_size, verbose, epoch, pop_size)
            best_pos3, best_fit3, list_loss3, time_elapsed3 = md3.train()
            pos = md3.solution[0]
            p.append(pos)
    p = np.array(p)
    return p

def SMA():
        
    #Ackley
    ub = [1000,1000]
    lb = [0,0]
    problem_size = 2
    
    ## Setting parameters
    obj_func = LocMinFuncs.some_obstacles
    # obj_func = LocMinFuncs.ackley
    pos = np.array([800,800]) #starting position
    verbose = False
    epoch = 20
    pop_size = 5
    
    # SMA
    
    # overall global min
    # md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    # best_pos1, best_fit1, list_loss1 = md1.train()
    # p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos)
    
    # print('Global Best Solution:')
    # print(md1.solution[0])
    # print(type(md1.solution[0]))
    # print(p)
    
    # dist = plot.plot(p[:,0],p[:,1],obj_func)
    # print("Total Distance:",dist)
    # print('\nFitness:')
    # print(md1.solution[1])
    #print(md1.loss_train)
    
    # GWO
    
        # overall global min
    # md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    # best_pos1, best_fit1, list_loss1, time_elapsed1 = md1.train()
    # p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos,"SMA")
    
    # print('Global Best Solution:')
    # print(md1.solution[0])
    # print(type(md1.solution[0]))
    # print(p)
    
    # dist = plot.plot(p[:,0],p[:,1],obj_func)
    # print("Total Distance:",dist)
    # print('\nFitness:')
    # print(md1.solution[1])
    # #print(md1.loss_train)
    
    
    # From Test Algorithms
    
    md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1, time_elapsed1 = md1.train()
    # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos,"SMA")
    dist = plot.plot(p[:,0],p[:,1],obj_func)
    print('Global Best Solution:')
    print(md1.solution[0])
    print(type(md1.solution[0]))
    print(p)
    
    print("Total Distance:",dist)
    print("Original SMA Best Fit:", best_fit1)
    print("SMA Time Elapsed: ", time_elapsed1)


    

    # Reduce the number of epochs on the SMA so that they both run for about the same amount of time
    print("Same amount of time given to both:")
    ratio = time_elapsed3 / time_elapsed1

    md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, int(epoch * ratio), pop_size)
    best_pos1, best_fit1, list_loss1, time_elapsed1 = md1.train()
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos,"SMA")
    dist = plot.plot(p[:,0],p[:,1],obj_func)
    print('Global Best Solution:')
    print(md1.solution[0])
    print(type(md1.solution[0]))
    print(p)
    print("Total Distance:",dist)
    print("\tOriginal SMA Best Fit:", best_fit1)
    print("\tSMA Time Elapsed: ", time_elapsed1)


    
def GWO():
    ub = [1000,1000]
    lb = [0,0]
    problem_size = 2
    
    ## Setting parameters
    obj_func = LocMinFuncs.some_obstacles
    # obj_func = LocMinFuncs.ackley
    pos = np.array([800,800]) #starting position
    verbose = False
    epoch = 20
    pop_size = 5
    
    
    md3 = GreyWolf(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    best_pos3, best_fit3, list_loss3, time_elapsed3 = md3.train()
    # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos,"GWO")
    dist = plot.plot(p[:,0],p[:,1],obj_func)
    print('Global Best Solution:')
    print(md3.solution[0])
    print(type(md3.solution[0]))
    print(p)
    print("Total Distance:",dist)
    print("GWO Best Fit:", best_fit3)
    print("GWO Time Elapsed: ", time_elapsed3)
    
    
    md3 = GreyWolf(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    best_pos3, best_fit3, list_loss3, time_elapsed3 = md3.train()
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos,"GWO")
    dist = plot.plot(p[:,0],p[:,1],obj_func)
    print('Global Best Solution:')
    print(md3.solution[0])
    print(type(md3.solution[0]))
    print(p)
    print("Total Distance:",dist)
    print("\tGWO Best Fit:", best_fit3)
    print("\tGWO Time Elapsed: ", time_elapsed3)
    
    