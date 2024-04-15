import cv2
from os import path
import json
import config

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

cap = cv2.VideoCapture(
    "rtsp://"+cam_access_info['login']+":"\
        +cam_access_info["pasword"]+"@"+cam_access_info['ip']
        )


while True:
    ret, frame = cap.read()

    if not ret:
        print("========================= Video not read =========================")
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break

