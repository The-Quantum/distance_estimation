# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:04:28 2024

@author: jpila
"""

import Chess_CalibUndist as Zhang
import Estimates as Est
import numpy as np
import cv2 as cv


#Parameters for Zhang method
dirPath = 'C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\Real Test ZhangChBoard\\FirstTestChess\\Temp'
squareSize = 1 #in cm
nbSquareX  = 11
nbSquareY = 11



#Calibration
ret, TransformMtx, distCoef, rVecs, tVecs = Zhang.calibration_Chess(
      dirPath, squareSize, nbSquareX, nbSquareY
      )


#test Undistort
imgTest = cv.imread('Screenshot6.jpg')
#imgTest = cv.resize(imgTest)
      
undst = Zhang.UndistortImage(imgTest, TransformMtx, distCoef)

scale_percent = 50 # percent of original size
newWidth = int(imgTest.shape[1] * scale_percent / 100)
newHeight = int(imgTest.shape[0] * scale_percent / 100)
toShow = cv.resize(imgTest, (newWidth,newHeight))

cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()
