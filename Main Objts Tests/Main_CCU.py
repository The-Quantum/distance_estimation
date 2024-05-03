# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:51:03 2024

Main for tests.

@author: jpila
"""
import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv

import numpy as np


######## Calibrate Camera test with Post its   

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)

objPts = np.float32([[0,0,0],[73.6,0,0],[0,117.4,0],[73.6,117.4,0],
                   [26.6,6,0],[8,40,0],[40,29.6,0],[23.8,51,0],[19.5,74.2,0],[37.6,72,0],[1.2,88,0],[19,98.5,0],[7,14.4,0],[10.4,21.6,0], #1- 9
                   [1,54.4,0],[7.6,57.4,0],[27,21.4,0],[29.4,28.2,0],[27.2,36,0],[34.2,39,0],[24,81.2,0],[26.4,87.6,0],[42.6,14,0],[45.8,20.6,0], #10 - 14
                   [35.4,45.4,0],[41,50.2,0],[34.6,96.2,0],[37.6,89.6,0],[52,0,0],[59,3.8,0],[50.2,44.2,0],[52.6,51.2,0],[46.4,71.2,0],[54,69.6,0], # 16 - 20 
                   [48.2,87,0],[55,90,0],[44.4,112.8,0],[47,106,0],[66,22.2,0],[72.4,26,0],[66.6,41,0],[70,47.8,0],[66,63.2,0],[72.4,65.6,0], # 21 - 25
                   [66.8,84.4,0],[68.2,92,0],[61.2,103.2,0],[64.2,110,0]]) #26 - 27


imgPts = np.float32([[405,52],[159,78],[578,364],[160,443],#Table points
                     [320,68],[417,124],[288,116],[367,156],[411,218],[328,224],[513,251],[451,304],[394,75],[389,87],#1- 9
                     [462,154],[437,164],[331,92],[326,108],[341,123],[315,133],[404,243],[399,268],[269,86],[260,99], #10 - 14
                     [316,147],[295,162],[370,309],[345,285],[233,68],[208,76],[255,152],[246,172],[287,225],[251,226], #16 - 20 
                     [290,284],[256,300],[338,394],[313,363],[187,113],[162,125],[188,154],[174,174],[194,213],[164,226], # 21 - 25
                     [195,287],[187,317],[228,362],[215,397]]) #26 - 27


#Read Image
img1 = cv.imread('newPtns0.jpg')
image = img1

#Show points in image to verify
for i in range (imgPts.shape[0]):
    coord = tuple(int(x) for x in imgPts[i])
    image = cv.circle(image,coord, 2,(0, 0, 255), -1)
    
h, w = image.shape[:2]

cv.imshow('Distorted',image)
cv.waitKey(0)

# Arrays to store object points and image points from all the images.
objP = [] # 3d point in real world space
imgP = [] # 2d points in image plane.
objP.append(objPts)
imgP.append(imgPts)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#Create Objects
cali = CC.CameraCalibration(objP)
szEstim = SE.SizeEstimations()

ret, tMtx, dCoef, rvecs, tvecs = cali.calbration(objP, imgP, gray.shape[::-1])

###########Basic Undistortion
newTMtx, roi = cv.getOptimalNewCameraMatrix(tMtx, dCoef, (w,h), 1, (w,h))

tImg0 = szEstim.undistortTransform(image, tMtx, dCoef)

###########Undistort with Remapping
mapx, mapy = cv.initUndistortRectifyMap(tMtx, dCoef , None, newTMtx, (w,h), 5)
tImg3 = cv.remap(image, mapx, mapy, cv.INTER_LINEAR)
 
# crop the image
x, y, w, h = roi
tImg3 = tImg3[y:y+h, x:x+w]


############Results 
cv.imshow('Undistorted',tImg0)
cv.waitKey(0)


cv.imshow('Remap Optimal Undistortion',tImg3)

cv.waitKey(0)

cv.destroyAllWindows()

toShow = np.concatenate((image,tImg0), axis = 1)
cv.imshow('Analyse',toShow)
cv.waitKey(0)
cv.destroyAllWindows()

