# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:55:36 2024

@author: jpila
"""
import SizeEstimations as SE
import cv2 as cv
import pickle


###################################### Measurements
##################### Camera Calibration Method
###############Exemple 1
print('Estimation with Camera Calibration matrix / Undistortion, Exemple 1:')
print('')
szEstim = SE.SizeEstimations()

# Open the file in binary mode 
with open('CCOutPut1.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

ccTmtx = MtxDcoefSclF[0]
ccDcoef = MtxDcoefSclF[1]
ccScaleF = MtxDcoefSclF[2]
print('Scale Factor = ', ccScaleF)

caseStudy = cv.imread('CaseStd01W3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixels0.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([449,240],[246,287])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([449,240],[528,359])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print('')

###############Exemple 2
print('Exemple 2:')
print('')
# Open the file in binary mode 
with open('CCOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

ccTmtx = MtxDcoefSclF[0]
ccDcoef = MtxDcoefSclF[1]
ccScaleF = MtxDcoefSclF[2]
print('Scale Factor = ', ccScaleF)

caseStudy = cv.imread('CaseStd11W3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixels1.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([148,187],[197,330])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([148,187],[270,151])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print(''); print('')

###################################### Measurements
##################### Homography Method
###############Exemple 1
print('Estimation with Homography matrix, Exemple 1:')
print('')

# Open the file in binary mode 
with open('HOutPut1.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxSclF = pickle.load(file) 

hTmtx = MtxSclF[0]
hScaleF = MtxSclF[1]
print('Scale Factor = ', hScaleF)

caseStudy = cv.imread('CaseStd01W3.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)


cv.imshow('Study',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixels2.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([58,330],[226,348])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([58,330],[48,445])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print('')

###############Exemple 2
print('Exemple 2:')
print('')

# Open the file in binary mode 
with open('HOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxSclF = pickle.load(file) 

hTmtx = MtxSclF[0]
hScaleF = MtxSclF[1]
print('Scale Factor = ', hScaleF)

caseStudy = cv.imread('CaseStd11W3.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)


cv.imshow('Study',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixels3.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([67,123],[240,122])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([67,123],[72,244])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print(''); print('')


###################################### Measurements
#####################  Undistortion + Homography Method

print('Estimation with  CC Undistortion then Homography matrix, Exemple1:')
print('')

#Mise en place pour trouver nouveau Scale Factor

# Open the file in binary mode 
with open('CCOutPut1.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoef = pickle.load(file) 

ccTmtx = MtxDcoef[0]
ccDcoef = MtxDcoef[1]

caseStudy = cv.imread('CaseStd01W3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.destroyAllWindows()

# Open the file in binary mode 
with open('HOutPut1.pkl', 'rb') as file: 

    # Call load method to deserialze 
    Mtx = pickle.load(file) 

hTmtx = Mtx[0]

tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsUH0.jpg',tCstudy)
cv.destroyAllWindows()



#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,0],[0,479])

#Estimate  scale factor
newScaleF = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)
print('New Scale factor =',newScaleF)

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([54,330],[226,347])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([54,330],[39,454])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print('')

###############Exemple 2
print('Exemple 2:')
print('')


caseStudy = cv.imread('CaseStd11W3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)


# Open the file in binary mode 
with open('HOutPut2.pkl', 'rb') as file: 

    # Call load method to deserialze 
    Mtx = pickle.load(file) 

hTmtx = Mtx[0]

tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsUH1.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,0],[12,469])

#Estimate  scale factor
newScaleF = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)
print('New Scale factor =',newScaleF)


#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([66,122],[240,121])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([66,122],[73,244])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real A3paper Height = ',realHValue)
print('Real A3paper width = ',realWValue)
print('')


