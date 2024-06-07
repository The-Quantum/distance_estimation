import pickle
import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

# to make your app take up all the available space in the browser window
# (not just a single column)
st.set_page_config(layout='wide')



st.write('### Homography Trasformation')

#### Init variables
imgP = np.array(st.session_state.imgPoints)
objP = np.array(st.session_state.objPoints)
scale = st.number_input(label="Manage Image View:",placeholder= 1,min_value= 1)

objP = objP * scale

img = st.session_state.image



#####Find Homography
H, _ = cv.findHomography(imgP, objP)

st.session_state["H"] = H

#####Applyu Homography
tImg = cv.warpPerspective(img , H, (img.shape[1],img.shape[0]))

st.session_state.tImage = tImg


st.image([img, tImg], caption=['Original Image', 'Homography trasformation'])
#st.image(tImg, caption='Homography trasformation')

col1, col2 = st.columns([5,1])

with col1:
    if st.button("Return"):
        st.switch_page("Pages/1_PixelsInput.py")

    if st.button("Restart All Process"):
        for key in st.session_state.keys():
            del st.session_state[key]

        st.switch_page("MainPage.py")

with col2:
    if st.button("Continue"):
        st.switch_page("Pages/3_DistanceStimation.py")

