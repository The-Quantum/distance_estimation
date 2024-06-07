import pickle
import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

def resetSessionVariables():
       # Delete a single key-value pair
    if "knownP1" in st.session_state:
        del st.session_state.knownP1

    if "knownP2" in st.session_state:
        del st.session_state.knownP2
    
    if "sclFactor" in st.session_state:
        del st.session_state.sclFactor

    if "unknownP1" in st.session_state:
        del st.session_state.unknownP1

    if "unknownP2" in st.session_state:
        del st.session_state.unknownP2
    
    if "locked" in st.session_state:
        del st.session_state.locked
    

    
    
    

# to make your app take up all the available space in the browser window
# (not just a single column)
st.set_page_config(layout='centered')



st.write('### DistanceStimation')
st.write('##### Steps:')
st.write('###### 1- Input coordinates of known real world lenght')
st.write('###### 2- Calculate scale Factor')
st.write('###### 3- Input coordinates of desired lenght to stimate')

st.write('### Indicate the points by clicking on the image ')

studyImg = st.session_state.tImage

value = streamlit_image_coordinates(studyImg)

if value:
    buff1, col, buff2 = st.columns([2,3,1])
    buff3, col4, buff4 = st.columns([1,5,1])

    st.write('Pick 2 points and input known lenght')

    with col:
        st.write(value)


    if st.button("Select"):

            if "knownP1" not in st.session_state:
                    st.session_state["knownP1"] = [value["x"],value["y"]]
                    st.write(st.session_state["knownP1"])
            elif "knownP2" not in st.session_state:
                    st.session_state["knownP2"] = [value["x"],value["y"]]
                    st.write(st.session_state["knownP1"], st.session_state["knownP2"])
            else:
                    st.write('Maximum number of points reached, if there is an error press reset')


if "knownP1" in st.session_state and "knownP2" in st.session_state:

    Pixel1 = np.array(st.session_state.knownP1)
        
    Pixel2 = np.array(st.session_state.knownP2)
        
    #If right format calculate euclidean distance
    pxlDist = np.linalg.norm(Pixel1 - Pixel2)

    rDist = st.number_input(label="Known Distance betwen this 2 points in cm:",step=1.,format="%.2f", min_value=0.0)

    st.session_state["sclFactor"] = pxlDist / rDist   

    st.write('Scale factor =',st.session_state["sclFactor"]) 

if "sclFactor" in st.session_state:

    #####File UpLoader
    file = st.file_uploader("Upload image with object with unknow dimensions",type=['png','jpg'],accept_multiple_files=False)

    if file:
        #read Image form stream
        image = Image.open(file)

        #transform into array format
        img  = np.array(image)

        #####Apply Homography
        tImg = cv.warpPerspective(img , st.session_state["H"], (img.shape[1],img.shape[0]))


        st.write('#### Indicate the points by clicking on the image ')

        value2 = streamlit_image_coordinates(tImg)

        if "n" not in st.session_state:
            st.session_state["n"] = 0

        buff5, col5, buff6 = st.columns([2,3,1])

        if value2:
            
            with col5:
                st.write(value2)
            
            col6, col7 = st.columns([2,1])

            with col6:
                if  st.button('Point1'):
                    
                    st.session_state["unknownP1"] = [value2["x"],value2["y"]]
                    
            with col7:   
                if st.button('Point2'):
                    st.session_state["unknownP2"] = [value2["x"],value2["y"]]

            with col6:
                 if "unknownP1" in st.session_state:
                    st.write("Selected pixel 1 = ", st.session_state.unknownP1)
                 
            with col7:
                if "unknownP2" in st.session_state:
                    st.write("Selected pixel 2 = ", st.session_state.unknownP2)




        if st.button('Estimate distance') :
            Pixel1 = np.array(st.session_state.unknownP1)
            Pixel2 = np.array(st.session_state.unknownP2)
                
            #If right format calculate euclidean distance
            pxlDist = np.linalg.norm(Pixel1 - Pixel2)

            rValue  = pxlDist / st.session_state.sclFactor

            st.write('Distance Estimated in Cm =',rValue) 
             

        print("n = ",st.session_state.n)
            



col2, col3 = st.columns([5,1])

with col2:
    if st.button("Reset"):
        resetSessionVariables()
        st.rerun()

    if st.button("Return"):
        resetSessionVariables()
        st.switch_page("Pages/2_Comparation.py")

with col3:
     if st.button("Restart All Process"):
        for key in st.session_state.keys():
            del st.session_state[key]

        st.switch_page("MainPage.py")