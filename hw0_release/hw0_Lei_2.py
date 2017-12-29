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


image1_path = "U:\Desktop\Learning\CS131_release-master\hw0_release\image1.jpg"
image2_path = "U:\Desktop\Learning\CS131_release-master\hw0_release\image2.jpg"


def display(img):
    # Show image
    plt.imshow(img)
    plt.axis('off')
    plt.show()


image1 = load(image1_path)
image2 = load(image2_path)

display(image1)
display(image2)


new_image = change_value(image1)
# display(new_image)

grey_image = convert_to_grey_scale(image1)
# display(grey_image)


without_red = rgb_decomposition(image1, 'R')
without_blue = rgb_decomposition(image1, 'B')
without_green = rgb_decomposition(image1, 'G')

# display(without_red)
# display(without_blue)
# display(without_green)


image_l = lab_decomposition(image1, 'L')
image_a = lab_decomposition(image1, 'A')
image_b = lab_decomposition(image1, 'B')

# display(image_l)
# display(image_a)
# display(image_b)


image_h = hsv_decomposition(image1, 'H')
image_s = hsv_decomposition(image1, 'S')
image_v = hsv_decomposition(image1, 'V')

# display(image_h)
# display(image_s)
# display(image_v)

image_mixed = mix_images(image1, image2, channel1='R', channel2='G')
display(image_mixed)
