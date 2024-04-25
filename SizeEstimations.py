# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:23:50 2024

Class DistanceEstimations

@author: jpila
"""

import numpy as np
import cv2 as cv
import math

class SizeEstimations:
    
    #Constructor
        #Not necessary for our purpose
    # def __init__(self, tMatrix, distCoefficient):
    #     self.tMtx = tMatrix
    #     self.dCoef = distCoefficient
    
    def __init__(self):
        pass
        
    #Methods
    def homographyTransform(self,imgCaseStudy,tMtx):
        imgTransform = cv.warpPerspective(imgCaseStudy,
                                          tMtx,
                                          (imgCaseStudy.shape[1], imgCaseStudy.shape[0]))
        return imgTransform
    
    
    def undistortTransform(self,imgCaseStudy, tMtx, dCoef):
        
        imgTransform = cv.undistort(imgCaseStudy, tMtx, dCoef, None)
        
        return imgTransform
    
    def estimateDistance2Pixels(self,Pixel1,Pixel2):
    
        toTest = np.float32([])
        
        if(type(toTest) != type(Pixel1)):
            Pixel1 = np.array(Pixel1)
            
        if(type(toTest) != type(Pixel2)):
            Pixel2 = np.array(Pixel2)
        
        distance = np.linalg.norm(Pixel1 - Pixel2)
    
        
        return distance
        

    def estimateScaleFactor(self,pDistKnowObj,realDist):
        
        scaleFactor = pDistKnowObj / realDist    
        
        return scaleFactor
    
    
    def estimateRealMeasure(self,pxlDistUnknowObj,scaleFactor):
        
        realValue = pxlDistUnknowObj / scaleFactor
       
        
        return realValue
    
            
        
