# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:58:32 2024

@author: jpila
"""

import cv2 as cv
import numpy as np


def Onclick(event,x,y, flags, params):
       
    # checking for right mouse clicks      
    if event==cv.EVENT_LBUTTONDOWN:
        print('[',x,',',y,']')
        params.append([x,y])
    



img = cv.imread('NewTest.jpg')
cv.imshow('Test', img)      

# setting mouse handler for the image 
    # and calling the click_event() function 
    
imgPts = []
cv.setMouseCallback('Test', Onclick,imgPts) 

cv.waitKey(0)
cv.destroyAllWindows()

imgPts = np.array(imgPts)
print('imgPts = ', imgPts)
