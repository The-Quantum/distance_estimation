# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:46:30 2024

@author: jpila
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# xPts = np.array(["Correction", "Homographie", "C + H"])
N = 3
yHPts = np.array([11.55, 0.075, 0.01])

yWPts = np.array([3.6,0.11,0])

# Position of bars on x-axis
ind = np.arange(N)

# # Figure size
# plt.figure(figsize=(10,5))

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind, yHPts , width, label='Blue bar label')
plt.bar(ind + width, yWPts, width, label='Orange bar label')

plt.xlabel('Here goes x-axis label')
plt.ylabel('Here goes y-axis label')
plt.title('Here goes title of the plot')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Xtick1', 'Xtick3', 'Xtick3'))

# Finding the best position for legends and putting it
plt.legend(loc='best')
plt.show()