# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:27:24 2024

@author: jpila
"""

import cv2 as cv
import numpy as np

#############Code to compare our DLT implementation for Homography Trasformation
#############And OpenCV findHomography function


objL = np.float32([[0,0,0],[280, 0,0],[0, 225,0],[280, 225,0], [0, 373,0],[280,373,0],[0,495,0],[280, 495,0]])
imgL = np.float32([[154, 420,0],[365, 419,0],[171,488,0], [501, 491,0], [194, 583,0], [675, 583,0], [254, 797,0], [1081, 797,0]])



# objL = np.float32([[0,0,0],[73.6,0,0],[0,117.4,0],[73.6,117.4,0]]) #1- 9

# objL = objL*4

# imgL = np.float32([[364,29,0],[123,61,0],[533,337,0],[116,416,0]])#1- 9

def getLPrime(T, Lines):
     
    Lprimes = []
    
    #Pour toute les lignes appliquer (produit matriciel avec ) la matrice T
    for i in range(0, Lines.shape[0]):
        Lprimes.append( T @ Lines[i, :].reshape((3,1)) )
    
    return np.array(Lprimes)


def getApoints(objL, imgL):
    # Get Known matrix A of our homography  Linear equation  calculus A.h = 0
    A_matrix = []
    for i in range (objL.shape[0]):
        Xd = objL[i][0][0] 
        Yd = objL[i][1][0] 
    
        Xs = imgL[i][0][0] 
        Ys = imgL[i][1][0] 
       
        A_matrix.append([Xs, Ys, 1, 0, 0, 0, -Xd*Xs, -Xd*Ys, -Xd])
        A_matrix.append([0, 0, 0, Xs, Ys, 1, -Yd*Xs, -Yd*Ys, -Yd])
        
    
   # print('A_Matrix = ', A_matrix)
    A_matrix = np.float32(A_matrix)
            
    return A_matrix

#SVD with points

#i make an artificial array just to put our arrays in the required format for the geApoints() Method
Tid = np.array([[1,0,0],
            [0,1,0],
            [0,0,1]
            ])
Tobjpp = getLPrime(Tid, objL) 
Timgpp = getLPrime(Tid, imgL) 

Ap = getApoints(Tobjpp, Timgpp)

Up,Sp,Vp = np.linalg.svd(Ap)
hp = Vp[-1]
HpPrime = hp.reshape((3,3))

cvH, _ = cv.findHomography(imgL,objL)

########Results
### Remark: Image savings are commented
#img1 = cv.imread('Test.jpg') "LinesHomography/image_hold3.jpg"

img1 = cv.imread('image_hold3.jpg')

cvtImg = cv.warpPerspective(img1, cvH, (img1.shape[1],img1.shape[0]))
tImg = cv.warpPerspective(img1, HpPrime, (img1.shape[1],img1.shape[0]))

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.imwrite('ForCanvaDLT.jpg', tImg)

cv.imshow('Transformation OpenCV', cvtImg)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.imwrite('ForCanvaH.jpg', tImg)

toShow = np.concatenate((tImg, cvtImg), axis=1) 
# toShow = np.concatenate((toShow, cvtImg), axis=1) 
cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()