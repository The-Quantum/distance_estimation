# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:09:50 

code for calibrating camera with Zhang's methode
    own chess images

@author: jpila
"""

import numpy as np
import cv2 as cv
import glob
import pathlib
import os

def calibration_Chess(dirPath, squareSize, width, height):
    #Number to indicate how many images we have browsed
    i=0
    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((width*height,3), np.float32)
    objp[:,:2] = np.mgrid[0:width,0:height].T.reshape(-1,2)
    objp = objp * squareSize;
    

    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

      
    images = pathlib.Path(dirPath).glob('*.jpg')

    nameOfFile = 'marks0'
    index=0
    

    for fname in images:
        img = cv.imread(str(fname))
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    

     
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (width,height), None)
     
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
     
            corners2 = cv.cornerSubPix(gray,corners, (width,height), (-1,-1), criteria)
            imgpoints.append(corners2)
     
            # Draw and display the corners
            cv.drawChessboardCorners(img, (width,height), corners2, ret)
        print("image number = ",i)
        
        
        # name = nameOfFile + '.jpg'
        # cv.imwrite(name,img)
            
        index += 1
        nameOfFile = nameOfFile.replace(nameOfFile[5],str(index))
        
        
        cv.imshow('img', img)
        cv.waitKey(0)
        i+=1
     
    cv.destroyAllWindows()


        
    #Camera calibration
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
        objpoints, imgpoints, gray.shape, None, None)
    
    return[ret, mtx, dist, rvecs, tvecs]
    
    
    
def UndistortChessImage(imgToUndist,calibMtx,distCoef):
 
    #undistortion
    
    undst = cv.undistort(imgToUndist, calibMtx, distCoef, None)
    
     
    return undst
 

def UndistorAllImages(dirPath,calibMtx,distCoef):
    os.chdir('C:\\Users\\jpila\\OneDrive\\Escritorio\\Jean Pierre\\Documentos\\Trabajos\\Stage BESTTIC\\Images to undistort again')
    nameOfFile = 'Undistorted0'
    index=0
    
    images = pathlib.Path(dirPath).glob('*.jpg')

    for fname in images:
        img = cv.imread(str(fname))
        
        imgUndist = UndistortChessImage(img,calibMtx,distCoef)
        
        name = nameOfFile + '.jpg'
        cv.imwrite(name,imgUndist)
            
        index += 1
        nameOfFile = nameOfFile.replace(nameOfFile[11],str(index))

        toShow = np.concatenate((img, imgUndist), axis=1) 
        cv.imshow('Comparation', toShow)
        cv.waitKey(0)
        
    cv.destroyAllWindows()
    
    
    


