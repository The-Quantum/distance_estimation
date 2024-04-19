# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:51:03 2024

Main for tests.

@author: jpila
"""
import CameraCalibration as CC

import numpy as np

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*2,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:2].T.reshape(-1,2)

#objp[2][2] = 4



corners = np.float32([[371,182],[97,229],[615,308],[234,392],[283,201],[407,219],[264,234],[361,243],[422,266],[339,279],[533,268],[479,297]])



cali1 = CC.CameraCalibration(objp , corners)

print(cali1.homography())



