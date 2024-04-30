import cv2
from os import path

import json
import numpy as np
import config
import os

# def caption_cv(config_file):

#     with open(path.join(config_file), "r+") as f:
#         cam_access_info = json.load(f)

#     cap = cv2.VideoCapture(
#         "rtsp://"+cam_access_info['login']+":"\
#         +cam_access_info["pasword"]+"@"+cam_access_info['ip']
#         )
#     return cap
        
config_file = config.CAMERA_LOGIN_FILE_PATH
#cap = caption_cv(config_file)

with open(path.join(config_file), "r+") as f:
    cam_access_info = json.load(f)



def takePhotos():
    
    
    # cap = cv2.VideoCapture(
    #     "rtsp://"+cam_access_info['login']+":"\
    #         +cam_access_info["pasword"]+"@"+cam_access_info['ip']
    #         )
      
    cap = cv2.VideoCapture(0)
    show = False
    i = 0;    
        
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("========================= Video not read =========================")
            break
        
        if show:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (7,7), None)
            
            cv2.drawChessboardCorners(frame, (7,7), corners, ret)
            
            
        cv2.imshow("frame", frame)
    
        if cv2.waitKey(1) == ord('p'):
            #take multiple photos for calibration
            name = '2sameTime'+str(i)+'.jpg'
            cv2.imwrite(name,frame)
           
            print('Image taken')
            i += 1
            print('Number of images =',i)
            
             
        if cv2.waitKey(1) == ord('a'):
            #take a singlePhoto
            print('show true')
            show = True
            
        if cv2.waitKey(1) == ord('d'):
            #take a singlePhoto
            print('show false')
            show = False
             
             
    
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break
 
        
