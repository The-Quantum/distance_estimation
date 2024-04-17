# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:32:23 2024

@aauthor: jpila
"""


import Chess_CalibUndist as Zhang
import ip_camera as TakePhotos
import Distance
import numpy as np
import cv2 as cv


##TakePhotos.takePhotos()

#Parameters for Zhang method
dirPath = 'C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\Screenshots'
squareSize = 1.5 #in cm
chBoardWidth  = 11
chBoardHeight = 11

#Calibration
ret, TransformMtx, distCoef, rVecs, tVecs = Zhang.calibration_Chess(
     dirPath, squareSize, chBoardWidth, chBoardHeight
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

########Scale Factor With Distorted Image
print("Scale factor with Distorted Image")

pixDistH = Distance.getDistance2Pixels(np.array([422, 433]) , np.array([851, 438]))
pixDistW = Distance.getDistance2Pixels(np.array([422, 433]) , np.array([400, 715]))
#Calculate Scale Factor

    #height (real world height 21cm)
scaleFactorH = pixDistH/21
    #Width  (real world width 13.3 cm)
scaleFactorW = pixDistW/13.3

print('Scale Factor height = ', scaleFactorH)
print('Scale Factor width = ', scaleFactorW)
print('')



########Scale Factor With Undistorted Image
print('')
print("Scale factor with UnDistorted Image")


pixDistH = Distance.getDistance2Pixels(np.array([418, 422]) , np.array([849, 435]))
pixDistW = Distance.getDistance2Pixels(np.array([418, 422]) , np.array([395, 709]))

#Calculate Scale Factor

    #height (real world height 21cm)
scaleFactorH = pixDistH/21
    #Width  (real world width 13.3 cm)
scaleFactorW = pixDistW/13.3
print('Pixel height distance = ' , pixDistH)
print('Pixel Width distance =', pixDistW)
print('Scale Factor height = ', scaleFactorH)
print('Scale Factor width = ', scaleFactorW)
print(''); print('')


#Calculate dimension of unknown object
print('Calculate dimension of unknown object')
pixDistH = Distance.getDistance2Pixels(np.array([470, 299]) , np.array([1057, 283]))
pixDistW = Distance.getDistance2Pixels(np.array([470, 299]) , np.array([457, 767]))

realH = pixDistH / scaleFactorH
realW = pixDistW / scaleFactorW

print('Pixel height distance = ' , pixDistH)
print('Pixel Width distance =', pixDistW)
print('')
print('Real world height = ' , realH)
print('Real world Width =', realW)





