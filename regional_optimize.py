# -*- coding: utf-8 -*-

# SMA Test

import numpy as np
from SMA import BaseSMA, OriginalSMA
import LocMinFuncs
import plot


def path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size,pos = np.array([-3,2])):
    p=[]
    p.append(pos)
    # resolution = 5.85
    resolution = 5.93
    bnd = np.array([ub,lb]) #bounds
    # while True:
    for i in range(30):
        # m_ub = []
        # m_lb = []
        m_ub = list((bnd/resolution + pos)[0])
        m_lb = list((bnd/resolution + pos)[1])
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
    ub = [4,4]
    lb = [-4,-4]
    problem_size = 2
    
    ## Setting parameters
    obj_func = LocMinFuncs.ackley
    verbose = False
    epoch = 20
    pop_size = 50
    
    # overall global min
    md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    best_pos1, best_fit1, list_loss1 = md1.train()
    p = path(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
    print('Global Best Solution:')
    print(md1.solution[0])
    print(type(md1.solution[0]))
    print(p)
    
    plot.plot(p[:,0],p[:,1],obj_func)
    # print('\nFitness:')
    # print(md1.solution[1])
    # #print(md1.loss_train)