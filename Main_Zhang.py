# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:06:20 2024

@author: jpila
"""


import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv

import numpy as np



#########        Zhangs  Test

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)

# chBoardDir = 'C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\ZhangChBoard\\test4'
# squareSize = 3.4 # in  cm
# nbCornersX = 7
# nbCornersY = 7


# objp = np.zeros((nbCornersX*nbCornersY,3), np.float32)
# print(objp.shape)
# objp[:,:2] = np.mgrid[0:nbCornersX,0:nbCornersY].T.reshape(-1,2)
# objp = objp * squareSize;

# print(objp.shape)
# #print(objp)


# cali2 = CC.CameraCalibration(objp)
# szEstim = SE.SizeEstimations()

# ret, tMtx, dCoef, rvecs, tvecs = cali2.zhang(chBoardDir, nbCornersX, nbCornersY)

# img1 = cv.imread('ChTest4jpg')

# tImg = szEstim.zhangsTransform(img1,tMtx,dCoef)
# cv.imwrite('resultf.jpg', tImg)

# cv.imshow('Analyse',tImg)
# cv.waitKey(0)
# cv.destroyAllWindows()
