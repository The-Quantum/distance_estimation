# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:13:45 2024

@author: jpila
"""

import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv

import numpy as np


objPts = np.float32([[0,0,0],[73.6,0,0],[0,117.4,0],[73.6,117.4,0],
                   [26.6,6,0],[8,40,0],[40,29.6,0],[23.8,51,0],[19.5,74.2,0],[37.6,72,0],[1.2,88,0],[19,98.5,0],[7,14.4,0],[10.4,21.6,0], #1- 9
                   [1,54.4,0],[7.6,57.4,0],[27,21.4,0],[29.4,28.2,0],[27.2,36,0],[34.2,39,0],[24,81.2,0],[26.4,87.6,0],[42.6,14,0],[45.8,20.6,0], #10 - 14
                   [35.4,45.4,0],[41,50.2,0],[34.6,96.2,0],[37.6,89.6,0],[52,0,0],[59,3.8,0],[50.2,44.2,0],[52.6,51.2,0],[46.4,71.2,0],[54,69.6,0], # 16 - 20 
                   [48.2,87,0],[55,90,0],[44.4,112.8,0],[47,106,0],[66,22.2,0],[72.4,26,0],[66.6,41,0],[70,47.8,0],[66,63.2,0],[72.4,65.6,0], # 21 - 25
                   [66.8,84.4,0],[68.2,92,0],[61.2,103.2,0],[64.2,110,0], #26 - 27
                   [3,64,0],[3.6,106.2,0],[35.8, 81,0],[61.2,74,0],[13.6,117.4,0],[22,106,0]
                   ]) #34 - 41
#32 is weird

#29?? BAD mesurement

#28,29,30,31,32,33,34,35,36,37,38,39,40,41                    
#[3,64,0],[3.6,106.2,0],[34.9,6.8,0],[35.8, 81,0],[37,117.4,0],[54.2,106,0],[58.2,115,0],[61.2,74,0],[68,6,0],[64.4,15,0],[69.2,51,0],[73,77,0],[67.2,106.5,0],[70.8,111,0]

imgPts = np.float32([[405,52],[159,78],[578,364],[160,443],#Table points
                     [320,68],[417,124],[288,116],[367,156],[411,218],[328,224],[513,251],[451,304],[394,75],[389,87],#1- 9
                     [462,154],[437,164],[331,92],[326,108],[341,123],[315,133],[404,243],[399,268],[269,86],[260,99], #10 - 14
                     [316,147],[295,162],[370,309],[345,285],[233,68],[208,76],[255,152],[246,172],[287,225],[251,226], #16 - 20 
                     [290,284],[256,300],[338,394],[313,363],[187,113],[162,125],[188,154],[174,174],[194,213],[164,226], # 21 - 25
                     [195,287],[187,317],[228,362],[215,397], #26 - 27
                     [466,179],[538,320],[345,252],[217,244],[515,381],[449,336]
                     ]) #34 - 41

# [466,179],[538,320],[294,71],[345,252],[374,413],[269,371],[253,416],[217,244],[180,85],[192,99],[179,181],[165,264],[198,382],[177,400]

#42 43 
# [13.6,117.4,0],[22,106,0]
#[515,381],[449,336]

img1 = cv.imread('newPtns0.jpg')
tImg0 = cv.imread ('GoodResult1.jpg')
print(imgPts.shape[0])


image = img1
for i in range (imgPts.shape[0]):
    coord = tuple(int(x) for x in imgPts[i])
    image = cv.circle(image,coord, 2,(0, 0, 255), -1)
    

# Arrays to store object points and image points from all the images.
objP = [] # 3d point in real world space
imgP = [] # 2d points in image plane.

objP.append(objPts)
imgP.append(imgPts)
    
    

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# cali3 = CC.CameraCalibration(objP)
szEstim = SE.SizeEstimations()

ret, tMtx, dCoef, rvecs, tvecs = cv.calibrateCamera(objP, imgP, gray.shape , None,None)

h, w = image.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(tMtx, dCoef, (w,h), 1)

# tImg1 = szEstim.zhangsTransform(image, tMtx, dCoef)

tImg1 = cv.undistort(image, tMtx, dCoef)



cv.imshow('Distorted',image)
cv.waitKey(0)

# cv.imshow('Undistorted',tImg0)
# cv.waitKey(0)

cv.imshow('new Undistortion',tImg1)
cv.imwrite('MorePoints.jpg',tImg1)
cv.waitKey(0)

cv.destroyAllWindows()