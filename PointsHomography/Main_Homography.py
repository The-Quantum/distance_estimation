# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:17:55 2024

@author: jpila
"""

import CameraCalibration as CC
import SizeEstimations as SE
import cv2 as cv
import pickle 
import numpy as np


########        Homography  Test

#Objet Creation
szEstim = SE.SizeEstimations()

#First test
# objp = np.float32([[0,0],[73.6,0],[0,117.4],[73.6,117.4],[26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5]])
# imgPts = np.float32([[952,29],[281,118],[1217,704],[134,856],[717,79],[939,201],[596,199],[781,277],[858,406],[637,423],[1112,467],[905,574]])

# Real world postich coordinates on the table
objPts = np.float32([[0,0],[73.6,0],[0,117.4],[73.6,117.4],
                     [26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5],[7,14.4],[10.4,21.6], #1- 9
                     [1,54.4],[7.6,57.4],[27,21.4],[29.4,28.2],[27.2,36],[34.2,39],[24,81.2],[26.4,87.6],[42.6,14],[45.8,20.6], #10 - 14
                     [35.4,45.4],[41,50.2],[34.6,96.2],[37.6,89.6],[52,0],[59,3.8],[50.2,44.2],[52.6,51.2],[46.4,71.2],[54,69.6], # 16 - 20                     
                     [48.2,87],[55,90],[44.4,112.8],[47,106],[66,22.2],[72.4,26],[66.6,41],[70,47.8],[66,63.2],[72.4,65.6], # 21 - 25                    
                     [66.8,84.4],[68.2,92],[61.2,103.2],[64.2,110]]) #26 -27


# Pixels coordinate of the postich coordinate on the table
imgPts = np.float32([[366,29],[123,61],[533,337],[116,416],#Table points
                      [281,47],[377,101],[248,94],[325,123],[367,193],[284,200],[468,225],[405,277],[355,53],[349,66],#1- 9
                      [421,127],[396,139],[290,71],[285,87],[300,100],[271,111],[359,216],[351,245],[230,66],[219,80], #10 - 14
                      [275,124],[254,141],[322,283],[298,256],[195,50],[170,59],[214,130],[206,151],[244,203],[207,204], #16 - 20 
                      [246,257],[211,275],[287,366],[264,335],[149,94],[125,106],[150,134],[135,155],[155,192],[123,206], # 21 - 25
                      [154,262],[146,293],[184,336],[169,370]]) #26 - 27

# Pixels coordinate of the postich coordinates at ( fist camera position change) 
# imgPts = np.float32([[395,26],[150,41],[542,338],[129,389],#Table points
#                      [310,38],[403,97],[276,82],[349,124],[386,187],[305,187],[486,225],[421,270],[385,48],[376,61],#1- 9
#                      [444,127],[418,138],[318,62],[312,77],[327,90],[299,101],[379,209],[369,236],[259,54],[248,66], #10 - 14
#                      [300,113],[277,128],[341,271],[319,237],[223,34],[198,41],[239,115],[229,134],[267,188],[228,186], #16 - 20 
#                      [266,239],[228,257],[303,351],[278,317],[177,76],[149,85],[174,115],[159,132],[177,170],[144,183], # 21 - 25
#                      [172,238],[165,270],[199,314],[181,348]]) #26 - 27


## Pixels coordinate of the postich coordinates at (second camera position change)
# imgPts = np.float32([[394,30],[154,56],[570,328],[168,408],#Table points
#                       [312,46],[411,99],[283,91],[361,129],[406,191],[324,194],[506,221],[448,270],[386,52],[381,65],#1- 9
#                       [454,127],[431,138],[323,69],[318,84],[334,97],[308,109],[400,212],[394,239],[262,63],[253,77], #10 - 14
#                       [312,121],[290,136],[370,277],[343,251],[226,46],[200,54],[251,125],[243,146],[287,197],[249,198], #16 - 20 
#                       [290,250],[256,268],[341,357],[314,326],[182,89],[156,101],[185,129],[171,147],[193,185],[162,197], # 21 - 25
#                       [197,255],[190,286],[232,326],[220,362]]) #26 - 27

#Transformation matrix to change coordinate system
mtx = np.float32([[-1,0,-1,73.6],[0,1,0,0],[0,0,-1,0],[0,0,0,0]])
objPts = szEstim.transformCoordSyst(objPts,mtx)


# better view 
objPts = objPts * 4 

#Create Objects
cali1 = CC.CameraCalibration(objPts)

# Compute the homography matrix 
H = cali1.homography(imgPts)

######Results
img1 = cv.imread('images/5objTest0.jpg') 
tImg = szEstim.homographyTransform(img1, H)

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('objFindScale3.jpg', tImg)

toShow = np.concatenate((img1, tImg), axis=1) 
cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()


###############Estimate Scale Factor

#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,9],[2,467])
#Estimate  scale factor
sclFactor = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)

print('Scale factor =',sclFactor)

###############Serialize Matrix  and Scale Factor
# toSave = (H, sclFactor) 

# # Open a file and use dump() 
# with open('ObjsHOutPut3.pkl', 'wb') as file: 
      
#     # A new file will be created 
#     pickle.dump(toSave, file) 