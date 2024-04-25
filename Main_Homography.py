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


imgPts2 = np.float32([[20,184],[46,446],[434,65],[601,231],#Table points
                      [51,250],[174,151],[166,257],[238,179],[323,140],[350,189],[342,88],[410,114],[72,182],[105,184],#1- 9
                      [218,120],[240,133],[113,226],[148,226],[178,207],[203,226],[354,141],[390,142],[93,291],[129,292], #10 - 14
                      [230,219],[265,230],[436,151],[418,167],[37,347],[57,372],[249,270],[290,268],[364,214],[376,244], #16 - 20 
                      [430,198],[462,127],[513,157],[498,172],[161,373],[192,399],[264,340],[309,342],[369,296],[406,319], # 21 - 25
                      [469,259],[505,254],[522,214],[555,215]]) #26 - 27


objPts = objPts * 4  #better view 

#Create Objects
cali1 = CC.CameraCalibration(objPts)
szEstim = SE.SizeEstimations()

H = cali1.homography(imgPts)



img1 = cv.imread('CaseStd0W3.jpg')
tImg = szEstim.homographyTransform(img1,H)

cv.imshow('Case Study', img1)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow('Transformation', tImg)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('toFindScale2.jpg', tImg)

toShow = np.concatenate((img1, tImg), axis=1) 
cv.imshow('Comparation', toShow)
cv.waitKey(0)
cv.destroyAllWindows()


###############Estimate Scale Factor

#Estimate  Pixel distance of  object of known dimensions 
objKnownPxDistance = szEstim.estimateDistance2Pixels([1,7],[7,465])
#Estimate  scale factor
sclFactor = szEstim.estimateScaleFactor(objKnownPxDistance, 117.4)

print('Scale factor =',sclFactor)

toSave = (H, sclFactor)

# Open a file and use dump() 
with open('HOutPut1.pkl', 'wb') as file: 
      
    # A new file will be created 
    pickle.dump(toSave, file) 