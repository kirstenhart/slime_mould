# Amanda Dings
# Modified: 12/2/2020
# Script to convert a 2d array saved as .mat to a 2d numpy array

from scipy.io import loadmat
from numpy import save
mat_fname = 'some_obstacles.mat'
mat_contents = loadmat(mat_fname)
my_array = mat_contents['field']

save('some_obstacles', my_array)
