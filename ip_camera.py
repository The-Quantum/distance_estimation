import cv2
from os import path
import Chess_CalibUndist as Zhang
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
    
    
    cap = cv2.VideoCapture(
        "rtsp://"+cam_access_info['login']+":"\
            +cam_access_info["pasword"]+"@"+cam_access_info['ip']
            )
    i = 0;    
        
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("========================= Video not read =========================")
            break
        
        scale_percent = 50 # percent of original size
        newWidth = int(frame.shape[1] * scale_percent / 100)
        newHeight = int(frame.shape[0] * scale_percent / 100)
        frame = cv2.resize(frame, (newWidth,newHeight))
        
        cv2.imshow("frame", frame)
    
        if cv2.waitKey(1) == ord('s'):
            #take multiple photos for calibration
            name = 'screenshot'+str(i)+'.jpg'
            cv2.imwrite(name,frame)
           
            print('Image taken')
            i += 1
            print('Number of images =',i)
            
            if i > 13 :
                cap.release()
                cv2.destroyAllWindows()
                break
             
        if cv2.waitKey(1) == ord('a'):
            #take a singlePhoto
            name = 'UndistTest.jpg'
            cv2.imwrite(name,frame)
           
            cap.release()
            cv2.destroyAllWindows()
            break
             
             
             
    
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break
        

def ImagesCompare(TransformMtx, distCoef):
    cap = cv2.VideoCapture(
        "rtsp://"+cam_access_info['login']+":"\
            +cam_access_info["pasword"]+"@"+cam_access_info['ip']
            )
   
    i = 0;    
        
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("========================= Video not read =========================")
            break
        
        normalWidth = int(frame.shape[1])
        normalHeight = int(frame.shape[0])
        
        #resize
        scale_percent = 50 # percent of original size
        newWidth = int(frame.shape[1] * scale_percent / 100)
        newHeight = int(frame.shape[0] * scale_percent / 100)
        frame = cv2.resize(frame, (newWidth,newHeight))
        
        #undistort
        frame_Undst = Zhang.UndistortImage(frame, TransformMtx, distCoef)
        frame_Undst = cv2.putText(
            frame_Undst, 'Calibration with Zhangs Method', (50,450),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2
            )
        
        toShow = np.concatenate((frame, frame_Undst), axis=1) 
        
        cv2.imshow("frame", toShow)
        
        if cv2.waitKey(1) == ord('a'):
            frame = cv2.resize(frame, (normalWidth,normalHeight))
            frame_Undst = cv2.resize(frame_Undst, (normalWidth,normalHeight))
            #take a singlePhoto
            os.chdir('C:\\Users\\jpila\\OneDrive\\Documents\\GitHub\\distance_estimation\\ToAnalyse')

            cv2.imwrite('Save_distorted2.jpg', frame)
            cv2.imwrite('Save_undistorted2.jpg',frame_Undst)
            cv2.imwrite('Comparation2.jpg',toShow)
           
            cap.release()
            cv2.destroyAllWindows()
            break
             
             
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break
        
