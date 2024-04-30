# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:51:53 2024

@author: jpila
"""

import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv
import pickle 
import numpy as np


########        Homography  Test

# objp = np.float32([[0,0],[73.6,0],[0,117.4],[73.6,117.4],[26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5]])
# imgPts = np.float32([[952,29],[281,118],[1217,704],[134,856],[717,79],[939,201],[596,199],[781,277],[858,406],[637,423],[1112,467],[905,574]])


objPts = np.float32([[0,0],[73.6,0],[0,117.4],[73.6,117.4],
                    [26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5],[7,14.4],[10.4,21.6], #1- 9
                    [1,54.4],[7.6,57.4],[27,21.4],[29.4,28.2],[27.2,36],[34.2,39],[24,81.2],[26.4,87.6],[42.6,14],[45.8,20.6], #10 - 14
                    [35.4,45.4],[41,50.2],[34.6,96.2],[37.6,89.6],[52,0],[59,3.8],[50.2,44.2],[52.6,51.2],[46.4,71.2],[54,69.6], # 16 - 20 
                    [48.2,87],[55,90],[44.4,112.8],[47,106],[66,22.2],[72.4,26],[66.6,41],[70,47.8],[66,63.2],[72.4,65.6], # 21 - 25
                    [66.8,84.4],[68.2,92],[61.2,103.2],[64.2,110]]) #26 -27

imgPts = np.float32([[402,51],[159,78],[578,364],[160,443],#Table points
                     [320,68],[417,124],[288,116],[367,156],[411,218],[328,224],[513,251],[451,304],[394,75],[389,87],#1- 9
                     [462,154],[437,164],[331,92],[326,108],[341,123],[315,133],[404,243],[399,268],[269,86],[260,99], #10 - 14
                     [316,147],[295,162],[370,309],[345,285],[233,68],[208,76],[255,152],[246,172],[287,225],[251,226], #16 - 20 
                     [290,284],[256,300],[338,394],[313,363],[187,113],[162,125],[188,154],[174,174],[194,213],[164,226], # 21 - 25
                     [195,287],[187,317],[228,362],[215,397]]) #26 -27




#Transformation matrix to change repere
tMtx = np.float32([[-1,0,-1,73.6],[0,1,0,0],[0,0,-1,0],[0,0,0,0]])

def transformCoordSyst(objP,tMtx):
    
    #create new dimentions
    add3D = np.zeros(shape=(objP.shape[0], 1))
    add4D = np.ones(shape=(objP.shape[0], 1))

    to_add = np.concatenate((add3D, add4D), axis=1)

    #add new dimensions
    objP = np.concatenate((objP, to_add), axis=1)


    for i in range (objP.shape[0]):
        objP[i] = np.dot(tMtx, objP[i])
        
    print(objPts)
    print('')
    
    Results = objP[:,:2] 
    
    return Results


test = transformCoordSyst(objPts,tMtx)


test = test * 4  #better view 

#Create Objects
cali1 = CC.CameraCalibration(test)
szEstim = SE.SizeEstimations()

H = cali1.homography(imgPts)

#Test
img1 = cv.imread('CaseStd0W3.jpg')
tImg = szEstim.homographyTransform(img1,H)

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('ReWarpTest.jpg', tImg)


