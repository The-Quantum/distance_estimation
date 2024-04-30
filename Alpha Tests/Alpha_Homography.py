# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:53:08 2024

@author: jpila
"""

import numpy as np
import cv2 as cv
import glob
import pathlib
import os

def calibration_Homography(dirPath,caseStudyImg,squareSize, nbSquareW, nbSquareH):
    os.chdir('C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\ToAnalyse')
    
    img1 = cv.imread('Screenshot2_0.jpg')
    img2 = cv.imread(caseStudyImg)
    
    
    '''
    scale_percent = 50 # percent of original size
    newWidth = int(img1.shape[1] * scale_percent / 100)
    newHeight = int(img1.shape[0] * scale_percent / 100)
    
    img1 = cv.resize(img1, (newWidth,newHeight))
    
    
    newWidth = int(img2.shape[1] * scale_percent / 100)
    newHeight = int(img2.shape[0] * scale_percent / 100)
    
    img2 = cv.resize(img2, (newWidth,newHeight))
    
    '''
    
    # # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    # objp = np.zeros((nbSquareW*nbSquareH,3), np.float32)
    # objp[:,:2] = np.mgrid[0:nbSquareW,0:nbSquareH].T.reshape(-1,2)
    # objp = objp * 15;
    
    ###objp = np.float32([[26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5]])
    #addition of table coordinates
    ##objp = np.float32([[0,0],[73.6,0],[0,117.4],[73.6,117.4],[26.6,6],[8,40],[40,29.6],[23.8,51],[19.5,74.2],[37.6,72],[1.2,88],[19,98.5]])
   
    objp = np.float32([[0,0],[736,0],[0,1174],[736,1174],[266,60],[80,400],[400,296],[238,510],[195,742],[376,720],[12,880],[190,985]])

 
    gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    
    #ret1, corners = cv.findChessboardCorners(gray, (nbSquareW,nbSquareH))
    
    ###corners = np.float32([[283,201],[407,219],[264,234],[361,243],[422,266],[339,279],[533,268],[479,297]])
    corners = np.float32([[371,182],[97,229],[615,308],[234,392],[283,201],[407,219],[264,234],[361,243],[422,266],[339,279],[533,268],[479,297]])

    
    #print('shape object points =', objp.shape)
    #print('shape corners =', corners.shape)
    
    H ,_= cv.findHomography(corners , objp )
    
    #print('H matrix =', H)
    
    H_small, _ = cv.findHomography(corners , objp/10 )
    
    
    img1_warp = cv.warpPerspective(img1, H_small,(img1.shape[1], img1.shape[0]))
    img2_warp = cv.warpPerspective(img2, H_small,(img2.shape[1], img2.shape[0]))

    toShow = np.concatenate((img1, img1_warp), axis=1) 
    cv.imshow('Comparation0', toShow)
    cv.waitKey(0)
       
    #Image 1 alone after applying H matrix
    img1_warp = cv.warpPerspective(img1, H,(1500, 1500))    
    scale_percent = 50 # percent of original size
    newWidth = int(img1_warp.shape[1] * scale_percent / 100)
    newHeight = int(img1_warp.shape[0] * scale_percent / 100)
    
    img1_warp = cv.resize(img1_warp, (newWidth,newHeight))
    
    cv.imshow('img1_warp', img1_warp)
    cv.waitKey(0)
    
  
    
    toShow = np.concatenate((img2, img2_warp), axis=1) 
    cv.imshow('Comparation1', toShow)
    cv.waitKey(0)
    
    
    #Image Case Study alone after applying H matrix
    img2_warp = cv.warpPerspective(img2, H,(1500, 1500))    
    scale_percent = 50 # percent of original size
    newWidth = int(img2_warp.shape[1] * scale_percent / 100)
    newHeight = int(img2_warp.shape[0] * scale_percent / 100)
    
    img2_warp = cv.resize(img2_warp, (newWidth,newHeight))
    
    cv.imshow('img2_warp', img2_warp)
    cv.waitKey(0)
    
    
    cv.imwrite('CaseStudy.jpg',img2_warp)
    
    cv.destroyAllWindows()


 
