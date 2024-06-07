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
        """
        Input :
        -------
         - imgCaseStudy : Image to transform or warp
         - tMtx : Transform matrix
        """
        
        #Trasform the image
        imgTransform = cv.warpPerspective(imgCaseStudy,
                                          tMtx,
                                          (imgCaseStudy.shape[1], imgCaseStudy.shape[0]))
        return imgTransform
    
    
    def undistortTransform(self,imgCaseStudy, tMtx, dCoef):
        
        #Correct distortion
        imgTransform = cv.undistort(imgCaseStudy, tMtx, dCoef, None)
        
        return imgTransform
    
    
    def transformCoordSyst(self,objP,tMtx):
        """ Transform the coordinate system
        """
        
        #create new dimentions
        add3D = np.zeros(shape=(objP.shape[0], 1))
        add4D = np.ones(shape=(objP.shape[0], 1))

        to_add = np.concatenate((add3D, add4D), axis=1)

        #add new dimensions
        objP = np.concatenate((objP, to_add), axis=1)


        #for every point, change coordinates with transformation matrix
        for i in range (objP.shape[0]):
            objP[i] = np.dot(tMtx, objP[i])
            
        
        Results = objP[:,:2] 
        
        return Results

    
    def estimateDistance2Pixels(self,Pixel1,Pixel2):
    
        toTest = np.float32([])
        
        if(type(toTest) != type(Pixel1)):
            Pixel1 = np.array(Pixel1)
            
        if(type(toTest) != type(Pixel2)):
            Pixel2 = np.array(Pixel2)
        
        
        #If right format calculate euclidean distance
        distance = np.linalg.norm(Pixel1 - Pixel2)
    
        
        return distance
        

    def estimateScaleFactor(self,pDistKnowObj,realDist):
        
        scaleFactor = pDistKnowObj / realDist    
        
        return scaleFactor
    
    
    def estimateRealMeasure(self,pxlDistUnknowObj,scaleFactor):
        
        realValue = pxlDistUnknowObj / scaleFactor
       
        
        return realValue
    
            
        
