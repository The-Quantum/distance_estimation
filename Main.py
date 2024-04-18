# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:32:23 2024

@aauthor: jpila
"""


import Chess_CalibUndist as Zhang
import ip_camera as TakePhotos
import Scale_stimation_Homography as Homography
import Estimates as Est
import numpy as np
import cv2 as cv


#TakePhotos.takePhotos()

#Parameters for Zhang method
dirPath = 'C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\Screenshots'
squareSize = 1.5 #in cm
nbSquareX  = 11
nbSquareY = 11

'''

#Calibration
ret, TransformMtx, distCoef, rVecs, tVecs = Zhang.calibration_Chess(
     dirPath, squareSize, nbSquareX, nbSquareY
     )


#Matrix inversion
InvMtx = np.linalg.inv(TransformMtx)


# #test Undistort
# imgTest = cv.imread('Screenshot6.jpg')
# #imgTest = cv.resize(imgTest)
      
# undst = Zhang.UndistortImage(imgTest, TransformMtx, distCoef)

# scale_percent = 50 # percent of original size
# newWidth = int(imgTest.shape[1] * scale_percent / 100)
# newHeight = int(imgTest.shape[0] * scale_percent / 100)

# toShow = cv.resize(imgTest, (newWidth,newHeight))

# cv.imshow('Comparation', toShow)
# cv.waitKey(0)
# cv.destroyAllWindows()

TakePhotos.ImagesCompare(TransformMtx, distCoef) 

'''

########Scale Factor With Distorted Image
    #The studied Object is going to be notebook
print("Scale factor with Distorted Image")

pixDistY = Est.estimateDistance2Pixels(np.array([422, 433]) , np.array([851, 438]))
pixDistX = Est.estimateDistance2Pixels(np.array([422, 433]) , np.array([400, 715]))

###Calculate Scale Factor

#Width  (real world width 13.3 cm) height (real world height 21cm)
scaleFactorX, scaleFactorY = Est.estimateScaleFactor(pixDistX, pixDistY, 13.3 , 21)
print('Scale Factor height = ', scaleFactorY)
print('Scale Factor width = ', scaleFactorX)
print('')


########Scale Factor With Undistorted Image
    #The studied Object is going to be notebook
print('')
print("Scale factor with UnDistorted Image")

pixDistY = Est.estimateDistance2Pixels(np.array([418, 422]) , np.array([849, 435]))
pixDistX = Est.estimateDistance2Pixels(np.array([418, 422]) , np.array([395, 709]))
print('Pixel height distance = ' , pixDistY)
print('Pixel Width distance =', pixDistX)

#Calculate Scale Factor
#Width  (real world width 13.3 cm) height (real world height 21cm)
scaleFactorX, scaleFactorY = Est.estimateScaleFactor(pixDistX, pixDistY, 13.3 , 21)
print('Scale Factor height = ', scaleFactorY)
print('Scale Factor width = ', scaleFactorX)
print(''); print('')


#####Calculate dimension of unknown object
    #The studied Object is going to the Chess board
print('Calculate dimension of unknown object (Case being a Chess board)')

pixDistY = Est.estimateDistance2Pixels(np.array([470, 299]) , np.array([1057, 283]))
pixDistX = Est.estimateDistance2Pixels(np.array([470, 299]) , np.array([457, 767]))
print('Pixel height distance = ' , pixDistY)
print('Pixel Width distance =', pixDistX)

realW, realH = Est.estimateRealMeasures(pixDistX, pixDistY, scaleFactorX, scaleFactorY)

print('')
print('Real world height ~= ' , realH,'cm')
print('Real world Width ~=', realW,'cm')
print('');print('')



#Use of homography for same purpose

Homography.calibration_Homography(dirPath, squareSize, nbSquareX, nbSquareY)


#####Calculate dimension of unknown object with IRL Homography exemple
    #The studied Object is going to be a pen
print('Calculate dimension of unknown object (Case being a pen)')

#table coordinates
pixDistY = Est.estimateDistance2Pixels(np.array([73, 0]) , np.array([73, 118]))
pixDistX = Est.estimateDistance2Pixels(np.array([73, 0]) , np.array([0, 1]))

print('Table Pixel height distance = ' , pixDistY)
print('Table Pixel Width distance =', pixDistX)

scaleFactorX, scaleFactorY = Est.estimateScaleFactor(pixDistX, pixDistY, 73.6, 117.4)
print('Scale Factor height = ', scaleFactorY)
print('Scale Factor width = ', scaleFactorX)
print(''); print('')

#pen coordinates

pixDistY = Est.estimateDistance2Pixels(np.array([64, 98]) , np.array([55, 108]))
pixDistX = Est.estimateDistance2Pixels(np.array([59, 101]) , np.array([61, 104]))

realW, realH = Est.estimateRealMeasures(pixDistX, pixDistY, scaleFactorX, scaleFactorY)

print('')
print('Real world  pen height ~= ' , realH,'cm')
print('Real world  pen Width ~=', realW,'cm')
print('');print('')





