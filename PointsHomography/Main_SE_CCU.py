# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:36:06 2024

@author: jpila
"""
import SizeEstimations as SE
import cv2 as cv
import pickle

###################################### Estimations 5 Objects
##################################Camera Calibration Undistorions
####Create Object
szEstim = SE.SizeEstimations()

####Get serialize matrix, distortion Coefficient, Scale factor
# Open the file in binary mode 
with open('ObjsCCOutPut.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

ccTmtx = MtxDcoefSclF[0]
ccDcoef = MtxDcoefSclF[1]
ccScaleF = MtxDcoefSclF[2]
print('Scale Factor = ', ccScaleF)


############################Object 1
print('Case Study 1 = A3 Paper')
print('')

caseStudy = cv.imread('5objTest1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj1.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([178,183],[361,158])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([178,183],[183,286])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real A3paper Height Estimation = ',realHValue)
print('Real A3paper width Estimation = ',realWValue)
print('')

############################Object 2
print('Case Study 2 = Assiete')
print('')

caseStudy = cv.imread('5objTest2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj2.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceR = szEstim.estimateDistance2Pixels([297,224],[247,224])

#Estimate real Distance
realRValue = szEstim.estimateRealMeasure(objUnknownPDistanceR, ccScaleF)

print('Real Assiete Radius Estimation = ',realRValue)
print('')

############################Object 3
print('Case Study 3 = Calendrier')
print('')

caseStudy = cv.imread('5objTest3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj3.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([191,130],[164,363])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([191,130],[370,123])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Calendrier Height Estimation = ',realHValue)
print('Real Calendrier width Estimation = ',realWValue)
print('')

############################Object 4
print('Case Study 4 = Telephone')
print('')

caseStudy = cv.imread('5objTest4.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj4.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([278,181],[246,232])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([278,181],[309,190])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Telephone Height Estimation = ',realHValue)
print('Real Telephone width Estimation = ',realWValue)
print('')

############################Object 5
print('Case Study 5 = Stylo')
print('')

caseStudy = cv.imread('5objTest5.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj5.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([255,228],[324,222])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([291,221],[291,226])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Stylo Height Estimation = ',realHValue)
print('Real Stylo width Estimation = ',realWValue)
print('')

############################Object 6
print('Case Study 6 = Sac')
print('')

caseStudy = cv.imread('5objTest6.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj6.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([183,184],[374,145])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([183,184],[200,300])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Sac Height Estimation = ',realHValue)
print('Real Sac width Estimation = ',realWValue)
print('')


############################Object 7
print('Case Study 7 = 3 post its')
print('')

caseStudy = cv.imread('5objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj7.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH1 = szEstim.estimateDistance2Pixels([118,94],[147,90])
objUnknownPDistanceW1 = szEstim.estimateDistance2Pixels([118,94],[119,102])

objUnknownPDistanceH2 = szEstim.estimateDistance2Pixels([215,193],[246,202])
objUnknownPDistanceW2 = szEstim.estimateDistance2Pixels([215,193],[206,204])

objUnknownPDistanceH3 = szEstim.estimateDistance2Pixels([407,277],[422,307])
objUnknownPDistanceW3 = szEstim.estimateDistance2Pixels([407,277],[389,280])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH1, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW1, ccScaleF)
print('Real Post it #23  Height Estimation = ',realHValue)
print('Real Post it #23 Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH2, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW2, ccScaleF)
print('Real Post it #20 Height Estimation = ',realHValue)
print('Real Post it #20 width Estimation = ',realWValue)
print('')

realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH3, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW3, ccScaleF)
print('Real Post it #8 Height Estimation = ',realHValue)
print('Real Post it #8 width Estimation = ',realWValue)
print('')




# Open the file in binary mode 
with open('ObjsCCOutPut2.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

ccTmtx = MtxDcoefSclF[0]
ccDcoef = MtxDcoefSclF[1]
ccScaleF = MtxDcoefSclF[2]
print('Scale Factor = ', ccScaleF)

############################Object 8
print('Case Study 8 = Cable')
print('')

caseStudy = cv.imread('9objTest0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj8.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([314,38],[183,329])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([259,142],[263,142])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Cable Height Estimation = ',realHValue)
print('Real Cable width Estimation = ',realWValue)
print('')

############################Object 9
print('Case Study 9 = Keyboard')
print('')

caseStudy = cv.imread('9objTest2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj9.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([194,131],[383,119])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([194,131],[196,172])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Keyboard Height Estimation = ',realHValue)
print('Real Keyboard width Estimation = ',realWValue)
print('')

############################Object 10
print('Case Study 10 = Case')
print('')

caseStudy = cv.imread('9objTest3.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj10.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([352,245],[323,155])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([350,243],[463,234])


#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Cable Height Estimation = ',realHValue)
print('Real Cable width Estimation = ',realWValue)
print('')

################ New test (penscil )

# Open the file in binary mode 
with open('ObjsCCOutPut3.pkl', 'rb') as file: 
      
    # Call load method to deserialze 
    MtxDcoefSclF = pickle.load(file) 

ccTmtx = MtxDcoefSclF[0]
ccDcoef = MtxDcoefSclF[1]
ccScaleF = MtxDcoefSclF[2]
print('Scale Factor = ', ccScaleF)

############################Objects 11
print('Case Study 11 = new pencil Blue White, Case, A3Paper, Keyboard ')
print('')

caseStudy = cv.imread('4sameTime1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj11.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([290,285],[369,293])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([330,287],[330,292])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real new pencil BW  (down) Height Estimation = ',realHValue)
print('Real new pencil BW (down) width Estimation = ',realWValue)
print('')


#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([320,268],[420,190])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([320,268],[244,209])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Case Height Estimation = ',realHValue)
print('Real Case width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([225,53],[242,135])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([222,53],[326,44])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real A3Paper Height Estimation = ',realHValue)
print('Real A3Paper width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([232,126],[257,271])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([233,126],[175,131])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real Keyboard Height Estimation = ',realHValue)
print('Real Keyboard width Estimation = ',realWValue)
print('')


################More Test
print('Case Study 12 = pencil Blue white, pencil black' )
print('')

caseStudy = cv.imread('2sameTime0.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj12.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([252,72],[304,62])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([278,66],[279,68])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real pencil BW (up) Height Estimation = ',realHValue)
print('Real pencil BW  (up) width Estimation = ',realWValue)
print('')

caseStudy = cv.imread('2sameTime1.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj13.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([192,118],[193,157])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([191,147],[195,137])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real pencil (left) BW Height Estimation = ',realHValue)
print('Real pencil (left) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([336,239],[273,250])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([303,241],[303,247])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real pencil (down) Bl Height Estimation = ',realHValue)
print('Real pencil (down) Bl width Estimation = ',realWValue)
print('')


caseStudy = cv.imread('2sameTime2.jpg')
tCstudy = szEstim.undistortTransform(caseStudy, ccTmtx, ccDcoef)

cv.imshow('Undistorted',tCstudy)
cv.waitKey(0)
cv.imwrite('getPixelsObj14.jpg',tCstudy)
cv.destroyAllWindows()

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([417,162],[376,129])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([398,144],[393,147])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real pencil (right) BW Height Estimation = ',realHValue)
print('Real pencil (right) BW width Estimation = ',realWValue)
print('')

#Estimate  Pixel Distance of object of unknown dimensions
objUnknownPDistanceH = szEstim.estimateDistance2Pixels([321,58],[276,61])
objUnknownPDistanceW = szEstim.estimateDistance2Pixels([301,57],[301,60])

#Estimate real Distance
realHValue = szEstim.estimateRealMeasure(objUnknownPDistanceH, ccScaleF)
realWValue = szEstim.estimateRealMeasure(objUnknownPDistanceW, ccScaleF)
print('Real pencil (up) Bl Height Estimation = ',realHValue)
print('Real pencil (up) Bl width Estimation = ',realWValue)
print('')



