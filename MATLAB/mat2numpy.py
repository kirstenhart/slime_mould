# Amanda Dings
# Modified: 12/2/2020
# Script to convert a 2d array saved as .mat to a 2d numpy array

from scipy.io import loadmat
from numpy import save
import os

os.chdir('/Users/adings/slime_mould/MATLAB/')
for i in range(20):
    mat_fname = 'field_{}_obs.mat'.format(i+1)
    print(os.getcwd())
    mat_contents = loadmat(mat_fname)
    my_array = mat_contents['field']

    npy_fname = 'field_{}_obs'.format(i+1)
    save(npy_fname, my_array)
