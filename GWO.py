# -*- coding: utf-8 -*-

import random
import numpy
import math
import time
from numpy.random import uniform, choice
from numpy import abs, zeros, log10, where, arctanh, tanh
from root import Root

class GWO(Root):
    
    def __init__(self, obj_func=None, lb=None, ub=None, problem_size=50, verbose=True, epoch=750, pop_size=100, z=0.03):
        Root.__init__(self, obj_func, lb, ub, problem_size, verbose)
        self.epoch = epoch
        self.pop_size = pop_size
        self.z = z

    def create_solution(self, minmax=0):
        pos = uniform(self.lb, self.ub)
        fit = self.get_fitness_position(pos)
        weight = zeros(self.problem_size)
        return [pos, fit, weight]

    def train(self):
        # initialize alpha, beta, and delta
        alpha_pos = beta_pos = delta_pos = numpy.zeros(self.problem_size)
        alpha_score = beta_score = delta_score = float("inf")

        if not isinstance(self.lb, list):
            self.lb = [self.lb] * self.problem_size
        if not isinstance(self.ub, list):
            self.ub = [self.ub] * self.problem_size
        
        # initialize the positions(pop) of search agents
        pop = numpy.zeros((self.pop_size, self.problem_size))
        for i in range(self.problem_size):
            pop[:, i] = uniform(0, 1, self.pop_size) * (self.ub[i] - self.lb[i]) + self.lb[i] # TODO: ValueError: operands could not be broadcast together with shapes (50,) (100,)
        
        ## Convergence_curve = numpy.zeros(self.epoch)
        ## s = solution()
        ## timerStart = time.time() 
        ## s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

        # main loop
        for l in range(0, self.epoch):
            for i in range(0, self.pop_size):
                
                # return back the search agents that go beyond the boundaries of the search space
                for j in range(self.problem_size):
                    pop[i,j] = numpy.clip(pop[i,j], self.lb[j], self.ub[j])

                # calculate objective function for each search agent
                fitness = self.obj_func(pop[i,:])
                
                # update alpha, beta, and delta
                if fitness < alpha_score :
                    delta_score = beta_score  # Update delte
                    delta_pos = beta_pos.copy()
                    beta_score = alpha_score  # Update beta
                    beta_pos = alpha_pos.copy()
                    alpha_score = fitness # Update alpha
                    alpha_pos = pop[i,:].copy()
                
                if (fitness > alpha_score and fitness < beta_score ):
                    delta_score = beta_score  # Update delte
                    delta_pos = beta_pos.copy()
                    beta_score = fitness  # Update beta
                    beta_pos = pop[i,:].copy()
                
                if (fitness > alpha_score and fitness > beta_score and fitness < delta_score):                 
                    delta_score = fitness # Update delta
                    delta_pos = pop[i,:].copy()
                
            a = 2 - l * ((2) / self.epoch) # a decreases linearly fron 2 to 0
            
            # update the position of search agents including omegas
            for i in range(0,self.pop_size):
                for j in range (0,self.problem_size):     
                            
                    r1 = random.random() # r1 is a random number in [0,1]
                    r2 = random.random() # r2 is a random number in [0,1]
                    
                    A1 = 2 * a * r1 - a # Equation (3.3)
                    C1 = 2 * r2 # Equation (3.4)
                    
                    D_alpha = abs(C1 * alpha_pos[j] - pop[i,j]) # Equation (3.5)-part 1
                    X1 = alpha_pos[j] - A1 * D_alpha # Equation (3.6)-part 1
                            
                    r1 = random.random()
                    r2 = random.random()
                    
                    A2 = 2 * a * r1 - a # Equation (3.3)
                    C2 = 2 * r2 # Equation (3.4)
                    
                    D_beta = abs(C2 * beta_pos[j] - pop[i,j]) # Equation (3.5)-part 2
                    X2 = beta_pos[j] - A2 * D_beta # Equation (3.6)-part 2       
                    
                    r1 = random.random()
                    r2 = random.random() 
                    
                    A3 = 2 * a * r1 - a # Equation (3.3)
                    C3 = 2 * r2 # Equation (3.4)
                    
                    D_delta = abs(C3 * delta_pos[j] - pop[i,j]) # Equation (3.5)-part 3
                    X3 = delta_pos[j] - A3 * D_delta # Equation (3.5)-part 3             
                    
                    pop[i,j] = (X1 + X2 + X3) / 3  # Equation (3.7)
                                
            ## Convergence_curve[l] = alpha_score

            if (l % 1 == 0):
                print(['At iteration '+ str(l)+ ' the best fitness is '+ str(alpha_score)])
        
        # none of this will work, but it's for analysis
        ## timerEnd = time.time()  
        ## s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
        ## s.executionTime = timerEnd-timerStart
        ## s.convergence = Convergence_curve
        ## s.optimizer = "GWO"
        ## s.objfname=objf.__name__
      
        return self.solution
