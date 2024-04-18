# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:42:12 2024

@author: jpila
"""

import numpy as np
import cv2 as cv
import math


def estimateDistance2Pixels(Pixel1,Pixel2):
    
    X = pow((Pixel1[0]-Pixel2[0]),2)
    Y = pow((Pixel1[1]-Pixel2[1]),2)
    
    #distance = math.sqrt(Pixel1-Pixel2)
    distance = np.linalg.norm(Pixel1 - Pixel2)
    
    return distance
    

def estimateScaleFactor(pxlDistX,pxlDistY,realDistX,realDistY):
    
    scaleFactorX = pxlDistX/realDistX    
    scaleFactorY = pxlDistY/realDistY
    
    return (scaleFactorX,scaleFactorY)


def estimateRealMeasures(pxlDistX,pxlDistY,scaleFactorX,scaleFactorY):
    
    realW = pxlDistX / scaleFactorX
    realH = pxlDistY / scaleFactorY
    
    return (realW,realH)

    

