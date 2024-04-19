# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:52:57 2024

Class CameraCalibration

@author: jpila
"""

import numpy as np
import cv2 as cv
import glob
import pathlib
import os

class CameraCalibration:
    #Attributes
    objP = []  #List of coordinates of the reference points in the real World
    imgPoints = [] #List of coordinates of the reference points in the image
    
    #Constructors
    def __init__(self,objectPts, imagePts):
        self.objP = objectPts
        self.imgPoints = imagePts
       
    #Methods
    def homography(self):
        
        #Check if coordinates have a 3 third dimension
        if(self.objP.shape[1] >= 3):
            #check if the values of this 3 third dimension are == 0
            if(self.__isPlane(self.objP) == False):
                raise Exception('objp is not a plane, cant use Homography')
                return False
            
        if(self.imgPoints.shape[1] >= 3):
           #check if the values of this 3 third dimension are == 0
            raise Exception('ImgPoints is not a plane, cant use Homography')
            return False
        
        #if no exception return Inverse matrix H^-1
        H_inv ,_= cv.findHomography(self.imgPoints , self.objP )
        
        return H_inv
        
        
    def __isPlane(self,ptnCoordinates):
        
        #check if the values of this 3 third dimension are == 0
        for i in range (ptnCoordinates.shape[0]):
            if(ptnCoordinates[i][2] != 0):
                return False
            
        return True
        