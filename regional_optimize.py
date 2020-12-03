# -*- coding: utf-8 -*-

# SMA Test

import numpy as np
from SMA import BaseSMA, OriginalSMA
import LocMinFuncs
import plot

#to modify starting point, update 'pos' in path() func call
def path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos = np.array([-6,6])):
    p=[]
    p.append(pos)
    # resolution = 5.85
    resolution = 10
    bnd = np.array([ub,lb]) #bounds
    # while True: 
    for i in range(10): #number of steps to take
        print("****** i *****:", i)
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
        md1 = BaseSMA(obj_func, m_lb, m_ub, problem_size, verbose, epoch, pop_size)
        best_pos1, best_fit1, list_loss1 = md1.train()
        pos = md1.solution[0]
        p.append(pos)
    p = np.array(p)
    return p

def main():
        
    #Ackley
    ub = [1000,1000]
    lb = [0,0]
    problem_size = 2
    
    ## Setting parameters
    obj_func = LocMinFuncs.some_obstacles
    pos = np.array([800,800]) #starting position
    verbose = False
    epoch = 20
    pop_size = 5
    
    # overall global min
    md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos)
    print('Global Best Solution:')
    print(md1.solution[0])
    print(type(md1.solution[0]))
    print(p)
    
    dist = plot.plot(p[:,0],p[:,1],obj_func)
    print("Total Distance:",dist)
    print('\nFitness:')
    print(md1.solution[1])
    #print(md1.loss_train)