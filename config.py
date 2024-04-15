from os import path

PRESENT_DIR  = path.dirname(path.realpath(__file__))

CAMERA_LOGIN_FILE_PATH = path.join(
    PRESENT_DIR, "camera_login_parameters.json"
)