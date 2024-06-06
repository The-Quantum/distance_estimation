import pickle
import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

def resetSessionVariables():
    # Delete a single key-value pair

    if "showMarks" in st.session_state:
        del st.session_state.showMarks

    if "imgPoints" in st.session_state:
        del st.session_state.imgPoints

    #transform into array format
    st.session_state.image  = np.array(st.session_state["imgStream"])
    

showMarks = False

st.write('### Now indicate the corresponding points in the image to save the coordinates in pixels by clicking on the image')
st.write('Note: The number of pixel coordinates need to match the number of real world coordinates ')

studyImg = st.session_state.image

if "showMarks"  in st.session_state:

    #Show points in image to verify
    imgPts = np.array(st.session_state.imgPoints)

    for i in range (imgPts.shape[0]):
        coord = tuple(int(x) for x in imgPts[i])
        studyImg = cv.circle(studyImg, coord , 2,(0, 0, 255), -1)

    st.image(studyImg)

    value = False
else:   
    value = streamlit_image_coordinates(studyImg)


if value:
    buff1, col, buff2 = st.columns([2,3,1])
    buff3, col4, buff4 = st.columns([1,5,1])

    with col:
        st.write(value)

        if st.button("Add Coordinate"):

            if "imgPoints" not in st.session_state:
                    st.session_state["imgPoints"] = [[value["x"],value["y"]]]
                    st.write(st.session_state["imgPoints"])

            else:
                if len(st.session_state.imgPoints) < st.session_state.nbPoints:

                    temp = st.session_state.imgPoints
                    temp.append([value["x"],value["y"]])
                    st.session_state.imgPoints =  temp
                    st.write(st.session_state.imgPoints)
                else:
                    with col4:
                        st.write('Maximum number of points reached, if there is an error press reset')

col2, col3 = st.columns([5,1])

if "showMarks"  in st.session_state:
    with col3:
        if st.button("Continue"):
            st.switch_page("Pages/2_Comparation.py")
        
        showMarks = True
        


if "imgPoints"  in st.session_state and not showMarks:
    if len(st.session_state.imgPoints) == st.session_state.nbPoints:
        st.write("")

        with col3:
            if st.button("Verify"):
                st.session_state.showMarks = True
                st.rerun()


with col2:
    if st.button("Reset"):
        resetSessionVariables()
        st.rerun()

    if st.button("Return"):
        resetSessionVariables()
        st.switch_page("MainPage.py")