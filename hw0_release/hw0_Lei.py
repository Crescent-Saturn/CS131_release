#Imports the print function from newer versions of python
from __future__ import print_function

#Setup

# The Random module for implements pseudo-random number generators
import random

# Numpy is the main package for scientific computing with Python. 
# This will be one of our most used libraries in this class
import numpy as np


#Imports all the methods in each of the files: linalg.py and imageManip.py
from linalg import *
from imageManip import *


#Matplotlib is a useful plotting library for python 
import matplotlib.pyplot as plt
# This code is to make matplotlib figures appear inline in the
# notebook rather than in a new window.

# %matplotlib inline
plt.rcParams['figure.figsize'] = (10.0, 8.0)  # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# Some more magic so that the notebook will reload external python modules;
# see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython
# %load_ext autoreload
# %autoreload 2
# %reload_ext autoreload

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
a = np.array([[1, 2, 3]])
b = np.array([[-1, 2, 5]])

a = a.T
b = b.T
print("M = \n", M)
print("a = ", a)
print("b = ", b)

aDotB = dot_product(a, b)
print(aDotB)


ans = matrix_mult(M, a, b)
print(ans)

print(svd(M))
