# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:04:48 2024

@author: jpila
"""

import numpy as np

objp = np.zeros((12,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:2].T.reshape(-1,2)

print('objp ', objp)

print('objp ', objp.shape[0])
