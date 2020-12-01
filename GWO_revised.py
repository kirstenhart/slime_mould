#!/usr/bin/env python

# ------------------------------------------------------------------------------------------------------------

from numpy import random as rand
from numpy.random import uniform, choice
from numpy import ndarray, fabs
from copy import deepcopy
from root import Root
import time  

class GreyWolf(Root):
    """

    """

    ID_WEIGHT = 0
    ID_FIT = 1

    def __init__(self, obj_func=None, lb=None, ub=None, problem_size=50, verbose=True, epoch=750, pop_size=100, z=0.03):
        Root.__init__(self, obj_func, lb, ub, problem_size, verbose)
        self.maxEpochs = epoch
        self.pop_size = pop_size
        self.z = z
        self.seed = 0
        self.Rand, self.exception = rand.RandomState(self.seed), None


    def rand(self, dimension=1):
        """Get random distribution of shape D in range from 0 to 1.

        Args:
            dimension (numpy.ndarray[int]): Shape of returned random distribution.

        Returns:
            Union[numpy.ndarray[float], float]: Random number or numbers :math:`\in [0, 1]`.
        """
        if isinstance(dimension, (ndarray, list)): return self.Rand.rand(*dimension)
        elif dimension > 1: return self.Rand.rand(dimension)
        else: return self.Rand.rand()

    def create_solution(self):
        weights = uniform(self.lb, self.ub)
        fitness = self.get_fitness_position(weights)
        return [weights, fitness]

    def train(self):
        start_time = time.clock() 
        wolves = [self.create_solution() for _ in range(self.pop_size)]

        wolves, g_best = self.get_sorted_pop_and_global_best_solution(wolves, self.ID_FIT, self.ID_MIN_PROB)

        # need to initial Alpha, Beta, Delta, etc.
        # copy the population based on the fitness values into Alpha, Beta and Delta wolves
        Alpha, Beta, Delta = deepcopy(wolves[0]), deepcopy(wolves[1]), deepcopy(wolves[2])

        #print("Initial Global Best",g_best[self.ID_FIT])

        for epoch in range(self.maxEpochs):

            # takes into account the iteration count
            a = 2 - epoch * (2 / self.maxEpochs)

            for i,wolf in enumerate(wolves):
                weight = wolf[self.ID_WEIGHT]
                A1, C1 = 2 * a * self.rand(self.problem_size) - a, 2 * self.rand(self.problem_size)
                X1 = Alpha[self.ID_WEIGHT] - A1 * fabs(C1 * Alpha[self.ID_WEIGHT] - weight)
                A2, C2 = 2 * a * self.rand(self.problem_size) - a, 2 * self.rand(self.problem_size)
                X2 = Beta[self.ID_WEIGHT] - A2 * fabs(C2 * Beta[self.ID_WEIGHT] - weight)
                A3, C3 = 2 * a * self.rand(self.problem_size) - a, 2 * self.rand(self.problem_size)
                X3 = Delta[self.ID_WEIGHT] - A3 * fabs(C3 * Delta[self.ID_WEIGHT] - weight)
                wolves[i][self.ID_WEIGHT] = self.amend_position((X1 + X2 + X3) / 3)
                wolves[i][self.ID_FIT] = self.get_fitness_position(wolves[i][self.ID_WEIGHT])

            # Sorted population and update the global best
            wolves, g_best = self.update_sorted_population_and_global_best_solution(wolves, self.ID_MIN_PROB, g_best)
            Alpha, Beta, Delta = deepcopy(wolves[0]), deepcopy(wolves[1]), deepcopy(wolves[2])
            self.loss_train.append(g_best[self.ID_FIT])
            if self.verbose:
                print("> Epoch: {}, Best fit: {}".format(epoch + 1, g_best[self.ID_FIT]))
        
        self.solution = g_best
        end_time = time.clock()
        time_elapsed = end_time - start_time
        return g_best[self.ID_POS], g_best[self.ID_FIT], self.loss_train, time_elapsed
