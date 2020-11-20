from SMA import BaseSMA, OriginalSMA
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

def func_square(solution):
    # if you have 100m of fence, how big of an area can you enclose?
    fence_used = 2*solution[0]+2*solution[1]
    encl_area = solution[0] * solution[1]
    if fence_used > 100 or (solution[0] < 1 or solution[1] < 1):
        return 100 # return 100 for invalid states
    return fence_used - 0.16 * encl_area


## You can create different bound for each dimension like this
#lb = [-15, -10, -3, -15, -10, -3, -15, -10, -3, -15, -10, -3, -15, -10, -3, -100, -40, -50]
#ub = [15, 10, 3, 15, 10, 3, 15, 10, 3, 15, 10, 3, 15, 10, 3, 20, 200, 1000]
#problem_size = 18
## if you choose this way, the problem_size need to be same length as lb and ub

## Or bound is the same for all dimension like this
# lb = [-100]
# ub = [100]
# problem_size = 2
## if you choose this way, the problem_size can be anything you want

## Fence example
lb = [0, 0]
ub = [100, 100]
problem_size = 2


## Setting parameters
obj_func = func_square
verbose = False
epoch = 100
pop_size = 50

md1 = BaseSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
best_pos1, best_fit1, list_loss1 = md1.train()
# return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
print('Global Best Solution:')
print(md1.solution[0])
print('\nFitness:')
print(md1.solution[1])
#print(md1.loss_train)

# md2 = OriginalSMA(obj_func, lb, ub, problem_size, verbose, epoch, pop_size)
# best_pos2, best_fit2, list_loss2 = md2.train()
# # return : the global best solution, the fitness of global best solution and the loss of training process in each epoch/iteration
# print(best_pos2)
# print(best_fit2)
# print(list_loss2)