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
    
    #Constructor
    def __init__(self,objectPts):
    
        self.objP = objectPts
   
    #Methods
    def homography(self,imgPoints):
        #Takes both list of Points get inverse transformation matrix H
        
        #Check if there is atleast 4 coordinates points
        if(self.__getNbPoints(self.objP) < 4):
            raise Exception('Not enought coordinate points. Need atleast 4, therefore cant use Homography')
            return False
        
        #check if there is same nb of points in both planes
        
        if(self.__getNbPoints(self.objP) != self.__getNbPoints(imgPoints)):
                raise Exception('Number of points in each plane differ, cant use Homography.')
                return False
        
      
        
        #Check if coordinates have a 3 third dimension
        if(self.objP.shape[1] >= 3):
            #check if the values of this 3 third dimension are == 0
            if(self.__isPlane(self.objP) == False):
                raise Exception('objp is not a plane, cant use Homography')
                return False
            
        
        
        #if no exception return Trasformation Matrix from img to 3D world
        H_inv ,_= cv.findHomography(imgPoints , self.objP )
        
        return H_inv
        
        
    def __getNbPoints(self,system):
        return system.shape[0]
        
        
    def __isPlane(self,ptnCoordinates):
        
        #check if the values of this 3 third dimension are == 0
        for i in range (ptnCoordinates.shape[0]):
            if(ptnCoordinates[i][2] != 0):
                return False
        
        return True
    
    
    def zhang(self,dirPath, nbCornersX, nbCornersY):
        #Calibration with chessboard
        
        #Check if there is atleast 4 coordinates points
        if(self.__getNbPoints(self.objP) < 4):
            raise Exception('Not enought coordinate points. Need atleast 4, therefore cant use Zhangs')
            return False
 
     
       
        #check if the values of this 3 third dimension are == 0
        if(self.__isPlane(self.objP) == False):
            raise Exception('objp is not a plane, cant zhang')
            return False
            
            
            
        #If no exception start calibration
        
        #Number to indicate how many images we have browsed
        i=0
        
        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        
        
        # Arrays to store object points and image points from all the images.
        objPtns = [] # 3d point in real world space
        imgPtns = [] # 2d points in image plane.

          
        imgsDir = pathlib.Path(dirPath).glob('*.jpg')


        for fname in imgsDir:
            img = cv.imread(str(fname))
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (nbCornersX,nbCornersY), None)
         
            # If found, add object points, image points (after refining them)
            if ret == True:
                objPtns.append(self.objP)
         
                corners2 = cv.cornerSubPix(gray,corners, (nbCornersX,nbCornersY), (-1,-1), criteria)
                imgPtns.append(corners2)
         
                # Draw and display the corners
                cv.drawChessboardCorners(img, (nbCornersX,nbCornersY), corners2, ret)
                
            print("image number = ",i)
            cv.imshow('img', img)
            cv.waitKey(0)
            i+=1
         
        cv.destroyAllWindows()
            
            
        # Return Trasformation Matrix from  3D world to Img, and distortion coefficient
        ret, tMtx, dist, rvecs, tvecs = cv.calibrateCamera(
            objPtns, imgPtns, gray.shape , None, None)
        
        
        return [ret,tMtx, dist ,rvecs, tvecs]

    
    
    def calibration(self,imgPoints, imgShape):
        toTest = np.float32([])
        
        #Check if points are in the right format , need an array of arrays.
        if(type(toTest) == type(self.objP)):
            objPoints = []
            objPoints.append(self.objP)
        
        # Return Trasformation Matrix from  3D world to Img, and distortion coefficient
        ret, tMtx, dist, rvecs, tvecs = cv.calibrateCamera(
            self.objP, imgPoints, imgShape , None, None)
        
        
        return [ret,tMtx, dist ,rvecs, tvecs]
        
        