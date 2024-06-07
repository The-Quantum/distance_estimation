# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:14:21 2024

@author: jpila
"""
import SizeEstimations as SE
import cv2 as cv
import pickle

###################################### Estimations 5 Objects
################################## Homography
####Create Object
szEstim = SE.SizeEstimations()

####Get serialize matrix  Scale factor
# Open the file in binary mode 
with open('ObjsHOutPut.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

hTmtx = MtxDcoefSclF[0]
hScaleF = MtxDcoefSclF[1]
print('Scale Factor = ', hScaleF)

############################Object 1
print('Case Study 1 = A3 Paper')
print('')

caseStudy = cv.imread('5objTest1.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj11.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([54,247],[224,249])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([54,247],[52,367])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real A3paper Height Estimation = ',realHValue)
print('Real A3paper width Estimation = ',realWValue)
print('')

############################Object 2
print('Case Study 2 = Assiete')
print('')

caseStudy = cv.imread('5objTest2.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj22.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceR = szEstim.estimateDistance2Pixels([150,318],[109,318])

#Estimate real Distance
realRValue = szEstim.estimateRealMeasure(objUnknownPDistanceR, hScaleF)

print('Real Assiete Radius Estimation = ',realRValue)
print('')

############################Object 3
print('Case Study 3 = Calendrier')
print('')

caseStudy = cv.imread('5objTest3.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj33.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([71,169],[36,433])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([71,169],[245,198])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Calendrier Height Estimation = ',realHValue)
print('Real Calendrier width Estimation = ',realWValue)
print('')

############################Object 4
print('Case Study 4 = Telephone')
print('')

caseStudy = cv.imread('5objTest4.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj44.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([144,264],[104,321])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([144,264],[168,281])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Telephone Height Estimation = ',realHValue)
print('Real Telephone width Estimation = ',realWValue)
print('')

############################Object 5
print('Case Study 5 = Stylo')
print('')

caseStudy = cv.imread('5objTest5.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj55.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([114,318],[171,323])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([145,317],[144,324])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Stylo Height Estimation = ',realHValue)
print('Real Stylo width Estimation = ',realWValue)
print('')

############################Object 6
print('Case Study 6 = Sac')
print('')

caseStudy = cv.imread('5objTest6.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj66.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([58,389],[242,384])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([58,389],[60,248])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Sac Height Estimation = ',realHValue)
print('Real Sac width Estimation = ',realWValue)
print('')

############################Object 7
print('Case Study 7 = 3 post its')
print('')

caseStudy = cv.imread('5objTest0.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj77.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH1 = szEstim.estimateDistance2Pixels([2,91],[30,88])
objUnknownPDistanceW1 = szEstim.estimateDistance2Pixels([2,91],[3,106])

objUnknownPDistanceH2 = szEstim.estimateDistance2Pixels([86,267],[110,284])
objUnknownPDistanceW2 = szEstim.estimateDistance2Pixels([86,280],[76,280])

objUnknownPDistanceH3 = szEstim.estimateDistance2Pixels([219,395],[221,424])
objUnknownPDistanceW3 = szEstim.estimateDistance2Pixels([219,395],[206,395])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH1, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW1, hScaleF)
print('Real Post it #23  Height Estimation = ',realHValue)
print('Real Post it #23 Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH2, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW2, hScaleF)
print('Real Post it #20 Height Estimation = ',realHValue)
print('Real Post it #20 width Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH3, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW3, hScaleF)
print('Real Post it #8 Height Estimation = ',realHValue)
print('Real Post it #8 width Estimation = ',realWValue)
print('')

################### Ajout de Objets

# Open the file in binary mode 
with open('ObjsHOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

hTmtx = MtxDcoefSclF[0]
hScaleF = MtxDcoefSclF[1]
print('Scale Factor = ', hScaleF)

############################Object 8
print('Case Study 8 = Cable')
print('')

caseStudy = cv.imread('9objTest0.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj88.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([192,29],[39,425])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([106,229],[110,229])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Cable Height Estimation = ',realHValue)
print('Real Cable width Estimation = ',realWValue)
print('')

############################Object 9
print('Case Study 9 = Keyboard')
print('')

caseStudy = cv.imread('9objTest2.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj99.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([49,195],[234,196])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([49,195],[52,258])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Keyboard Height Estimation = ',realHValue)
print('Real Keyboard width Estimation = ',realWValue)
print('')

############################Object 10
print('Case Study 10 = Case')
print('')

caseStudy = cv.imread('9objTest3.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1010.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([171,361],[168,236])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([171,362],[260,361])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Cable Height Estimation = ',realHValue)
print('Real Cable width Estimation = ',realWValue)
print('')


################ New test (penscil )

# Open the file in binary mode 
with open('ObjsHOutPut3.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

hTmtx = MtxDcoefSclF[0]
hScaleF = MtxDcoefSclF[1]
print('Scale Factor = ', hScaleF)

############################Objects 11
print('Case Study 11 = new pencil Blue White, Case, A3Paper, Keyboard ')
print('')

caseStudy = cv.imread('4sameTime1.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)


cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1111.jpg',tCstudy)
cv.destroyAllWindows()


#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([124,371],[228,302])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([121,370],[71,294])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Case Height Estimation = ',realHValue)
print('Real Case width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([83,20],[84,188])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([83,20],[204,25])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real A3Paper Height Estimation = ',realHValue)
print('Real A3Paper width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([75,173],[70,360])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([76,171],[23,170])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real Keyboard Height Estimation = ',realHValue)
print('Real Keyboard width Estimation = ',realWValue)
print('')


################More Test
print('Case Study 12 = pencil Blue white, pencil black' )
print('')

caseStudy = cv.imread('2sameTime0.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1212.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([109,78],[169,66])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([141,67],[142,75])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real pencil BW (up) Height Estimation = ',realHValue)
print('Real pencil BW  (up) width Estimation = ',realWValue)
print('')

caseStudy = cv.imread('2sameTime1.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1313.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([38,151],[35,214])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([35,189],[38,190])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real pencil (left) BW Height Estimation = ',realHValue)
print('Real pencil (left) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([90,345],[140,344])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([120,342],[119,347])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real pencil (down) Bl Height Estimation = ',realHValue)
print('Real pencil (down) Bl width Estimation = ',realWValue)
print('')


caseStudy = cv.imread('2sameTime2.jpg')
tCstudy = szEstim.homographyTransform(caseStudy, hTmtx)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1414.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([238,262],[214,207])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([227,228],[221,230])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real pencil (right) BW Height Estimation = ',realHValue)
print('Real pencil (right) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([189,62],[138,58])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([165,56],[164,65])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, hScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, hScaleF)
print('Real pencil (up) Bl Height Estimation = ',realHValue)
print('Real pencil (up) Bl width Estimation = ',realWValue)
print('')



