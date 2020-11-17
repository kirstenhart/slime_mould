#!/usr/bin/env python

from GWO import GWO
from numpy import sum, pi, exp, sqrt, cos


## You can create whatever function you want here
def func_sum(solution):
    return sum(solution ** 2)


def func_ackley(solution):
    a, b, c = 20, 0.2, 2 * pi
    d = len(solution)
    sum_1 = -a * exp(-b * sqrt(sum(solution ** 2) / d))
    sum_2 = exp(sum(cos(c * solution)) / d)
    return sum_1 - sum_2 + a + exp(1)


## You can create different bound for each dimension like this
# lb = [-15, -10, -3, -15, -10, -3, -15, -10, -3, -15, -10, -3, -15, -10, -3, -100, -40, -50]
# ub = [15, 10, 3, 15, 10, 3, 15, 10, 3, 15, 10, 3, 15, 10, 3, 20, 200, 1000]
# problem_size = 18
## if you choose this way, the problem_size need to be same length as lb and ub

## Or bound is the same for all dimension like this
lb = [-100]
ub = [100]
problem_size = 100
## if you choose this way, the problem_size can be anything you want


## Setting parameters
obj_func = func_ackley
verbose = True
epoch = 1000
pop_size = 50

md1 = GWO(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
# return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
print(md1.solution[0])
print(md1.solution[1])
print(md1.loss_train)

