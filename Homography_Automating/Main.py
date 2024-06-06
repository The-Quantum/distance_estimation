# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:43:36 2024

@author: jpila
"""
import pickle
import cv2 as cv
import numpy as np



def stimateHomography(objPts, imgPts, fName):
    # Input a file name , Real world coordinates and image coordinates of reference points
    # Estimates Homography matrix with the sets of coordinates
    # No Output but creation and save of a file (with the name passed as parameter) that contains the Homography matrix
    
    if('.pkl' not in fName):
        raise Exception('File name not valid or forgot .pkl at the end')
        return False
    
    if(len(fName) <= 4):
        #'.pkl' is not valid
        raise Exception('File name not valid')
        return False
    
    
    H, _ = cv.findHomography(imgPts,objPts)
    
    
    ###############Serialize Matrix
    # Open a file and use dump() 
    with open(fName, 'wb') as file: 
          
        # A new file will be created 
        pickle.dump(H, file) 


def applyHomography(fName, image):
    # Input an image and a name of a file of type .pkl that contains a homography matrix you want to apply on the image
    # Output the trasformed image 
    
    if('.pkl' not in fName):
        raise Exception('Filte type not valid or forgot .pkl at the end')
        return False
    else:
        if(len(fName) <= 4):
            raise Exception('File name not valid')
            return False
    
    ####Get serialize H matrix  
    # Open the file in binary mode 
    with open(fName, 'rb') as file: 
          
        # Call load method to deserialze 
        H = pickle.load(file) 
    
    # Apply Homography matrix to the image
    tImg = cv.warpPerspective(image, H, (image.shape[1],image.shape[0]))
    return tImg

def Video():
    #No input no Output
    #function to film and see homography trasformation live
    
    #Get camera 
    cap = cv.VideoCapture(0)
    show = False
    i = 0;    
        
    while True:
        #Infinite loop where you get each frame
        ret, frame = cap.read()
    
        if not ret:
            print("========================= Video not read =========================")
            break
            
        
        tFrame = applyHomography('Test.pkl', frame)
        
        
        toShow = np.concatenate((frame, tFrame), axis=1) 
        cv.imshow('Comparation', toShow)    
             
    
        if cv.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv.destroyAllWindows()
            break

########### Set Points
objL = np.float32([[0,0,0],[73.6,0,0],[0,117.4,0],[73.6,117.4,0]]) #1- 9
objL = objL*4 

imgL = np.float32([[349,26,0],[112,78,0],[576,310,0],[190,443,0]])#1- 9
###########


stimateHomography(objL,imgL,'Test.pkl')

img = cv.imread('NewTest.jpg')
tImg = applyHomography('Test.pkl',img)

Video()



