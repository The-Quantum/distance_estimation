# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:54:07 2024

@author: jpila
"""

import SizeEstimations as SE
import cv2 as cv
import pickle


###################################### Estimations 5 Objects
################################## Undistorions + Homography

#####Mise en place pour trouver nouveau Scale Factor

####Create Object
szEstim = SE.SizeEstimations()

####Get serialize matrix, distortion Coefficient, Scale factor
# Open the file in binary mode 
with open('ObjsCCOutPut.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoef = pickle.load(file) 

ccTmtx = MtxDcoef[0]
ccDcoef = MtxDcoef[1]

caseStudy = cv.imread('5objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.destroyAllWindows()

# Open the file in binary mode 
with open('ObjsHOutPut.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    Mtx = pickle.load(file) 

hTmtx = Mtx[0]

tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObjUH0.jpg',tCstudy)
cv.destroyAllWindows()


#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,0],[0,470])

#Estimate  scale factor
newScaleF = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)
print('New Scale factor =', newScaleF)


############################Object 1
print('Case Study 1 = A3 Paper')
print('')

caseStudy = cv.imread('5objTest1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj111.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([54,246],[224,250])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([54,246],[51,366])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real A3paper Height Estimation = ',realHValue)
print('Real A3paper width Estimation = ',realWValue)
print('')

############################Object 2
print('Case Study 2 = Assiete')
print('')

caseStudy = cv.imread('5objTest2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj222.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceR = szEstim.estimateDistance2Pixels([150,318],[109,318])

#Estimate real Distance
realRValue = szEstim.estimateRealMeasure(objUnknownPDistanceR, newScaleF)

print('Real Assiete Radius Estimation = ',realRValue)
print('')

############################Object 3
print('Case Study 3 = Calendrier')
print('')

caseStudy = cv.imread('5objTest3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj333.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([71,167],[34,433])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([71,167],[245,198])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Calendrier Height Estimation = ',realHValue)
print('Real Calendrier width Estimation = ',realWValue)
print('')

############################Object 4
print('Case Study 4 = Telephone')
print('')

caseStudy = cv.imread('5objTest4.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj444.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([143,264],[104,319])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([143,264],[167,282])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Telephone Height Estimation = ',realHValue)
print('Real Telephone width Estimation = ',realWValue)
print('')

############################Object 5
print('Case Study 5 = Stylo')
print('')

caseStudy = cv.imread('5objTest5.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj555.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([114,318],[171,324])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([145,317],[144,324])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Stylo Height Estimation = ',realHValue)
print('Real Stylo width Estimation = ',realWValue)
print('')

############################Object 6
print('Case Study 6 = Sac')
print('')

caseStudy = cv.imread('5objTest6.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj666.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([61,389],[244,380])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([61,389],[59,246])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Sac Height Estimation = ',realHValue)
print('Real Sac width Estimation = ',realWValue)
print('')

############################Object 7
print('Case Study 7 = 3 post its')
print('')

caseStudy = cv.imread('5objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj777.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH1 = szEstim.estimateDistance2Pixels([0,81],[27,79])
objUnknownPDistanceW1 = szEstim.estimateDistance2Pixels([0,81],[0,96])

objUnknownPDistanceH2 = szEstim.estimateDistance2Pixels([86,266],[112,285])
objUnknownPDistanceW2 = szEstim.estimateDistance2Pixels([86,266],[76,279])

objUnknownPDistanceH3 = szEstim.estimateDistance2Pixels([220,396],[222,426])
objUnknownPDistanceW3 = szEstim.estimateDistance2Pixels([220,396],[205,397])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH1, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW1, newScaleF)
print('Real Post it #23  Height Estimation = ',realHValue)
print('Real Post it #23 Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH2, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW2, newScaleF)
print('Real Post it #20 Height Estimation = ',realHValue)
print('Real Post it #20 width Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH3, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW3, newScaleF)
print('Real Post it #8 Height Estimation = ',realHValue)
print('Real Post it #8 width Estimation = ',realWValue)
print('')

################### Ajout de Objets

# Open the file in binary mode 
with open('ObjsCCOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoef = pickle.load(file) 

ccTmtx = MtxDcoef[0]
ccDcoef = MtxDcoef[1]

caseStudy = cv.imread('9objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.destroyAllWindows()

# Open the file in binary mode 
with open('ObjsHOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    Mtx = pickle.load(file) 

hTmtx = Mtx[0]

tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObjUH1.jpg',tCstudy)
cv.destroyAllWindows()


#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,0],[0,471])

#Estimate  scale factor
newScaleF = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)
print('New Scale factor =', newScaleF)


############################Object 8
print('Case Study 8 = cable')
print('')

caseStudy = cv.imread('9objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj888.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([192,25],[39,425])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([111,214],[115,214])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real cable Height Estimation = ',realHValue)
print('Real cable width Estimation = ',realWValue)
print('')

############################Object 9
print('Case Study 9 = keyboard')
print('')

caseStudy = cv.imread('9objTest2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj999.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([236,195],[48,193])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([236,195],[231,262])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real keyboard Height Estimation = ',realHValue)
print('Real keyboard width Estimation = ',realWValue)
print('')

############################Object 10
print('Case Study 10 = Case')
print('')

caseStudy = cv.imread('9objTest3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj101010.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([171,363],[167,234])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([171,363],[266,362])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real case Height Estimation = ',realHValue)
print('Real csae width Estimation = ',realWValue)
print('')

################### New Tests

# Open the file in binary mode 
with open('ObjsCCOutPut3.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoef = pickle.load(file) 

ccTmtx = MtxDcoef[0]
ccDcoef = MtxDcoef[1]

caseStudy = cv.imread('4sameTime0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.destroyAllWindows()

# Open the file in binary mode 
with open('ObjsHOutPut3.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    Mtx = pickle.load(file) 

hTmtx = Mtx[0]

tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObjUH99.jpg',tCstudy)
cv.destroyAllWindows()


#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([0,0],[0,471])

#Estimate  scale factor
newScaleF = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)
print('New Scale factor =', newScaleF)

###########################Objects 11
print('Case Study 11 = new pencil Blue White, Case, A3Paper, Keyboard ')
print('')

caseStudy = cv.imread('4sameTime1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)


cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj111111.jpg',tCstudy)
cv.destroyAllWindows()


#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([124,370],[229,302])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([122,371],[72,295])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Case Height Estimation = ',realHValue)
print('Real Case width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([82,8],[83,185])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([82,8],[206,15])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real A3Paper Height Estimation = ',realHValue)
print('Real A3Paper width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([75,169],[73,361])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([75,169],[21,167])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real Keyboard Height Estimation = ',realHValue)
print('Real Keyboard width Estimation = ',realWValue)
print('')


################More Test
print('Case Study 12 = pencil Blue white, pencil black' )
print('')

caseStudy = cv.imread('2sameTime0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj121212.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([108,71],[171,61])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([141,60],[142,69])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real pencil BW (up) Height Estimation = ',realHValue)
print('Real pencil BW  (up) width Estimation = ',realWValue)
print('')

caseStudy = cv.imread('2sameTime1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj131313.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([36,148],[34,212])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([33,185],[37,184])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real pencil (left) BW Height Estimation = ',realHValue)
print('Real pencil (left) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([141,344],[90,346])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([118,342],[117,348])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real pencil (down) Bl Height Estimation = ',realHValue)
print('Real pencil (down) Bl width Estimation = ',realWValue)
print('')


caseStudy = cv.imread('2sameTime2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)
tCstudy = szEstim.homographyTransform(tCstudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj141414.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([239,263],[215,205])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([224,233],[229,232])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real pencil (right) BW Height Estimation = ',realHValue)
print('Real pencil (right) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([191,56],[139,50])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([168,51],[168,56])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, newScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, newScaleF)
print('Real pencil (up) Bl Height Estimation = ',realHValue)
print('Real pencil (up) Bl width Estimation = ',realWValue)
print('')



