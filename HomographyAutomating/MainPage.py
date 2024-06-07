# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:15:09 2024

@author: jpila
"""
import pickle
import cv2 as cv
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates


def resetSessionVariables():
    # Delete all key-value pair
    for key in st.session_state.keys():
        del st.session_state[key]



values = []
i=0


###########Header
st.write('# Welcome!')
st.write('### This is an app to apply a homography trasformation to and image')
st.write('##### Steps:')
st.write('###### 1- Upload Image to transform')
st.write('###### 2- Input real world coordinates of Reference points')
st.write('###### 3- Input image coordinates of Reference points')
st.write('###### 4- Transform & Analyse')


#####File UpLoader
file = st.file_uploader("Upload image you would desire to  trasform",type=['png','jpg'],accept_multiple_files=False)

if file:
    
    #read Image form stream
    image = Image.open(file)
    st.session_state["imgStream"] = image

    #transform into array format
    img  = np.array(image)
    
    st.image(img)

    st.session_state["image"] = img

    st.write("\n")
    st.write('##### Now input the set of coordinates of real world reference points')
    st.write('Note: Need atleast 4 points')

    
    x = st.number_input(label="X coordinate",step=1.,format="%.2f", min_value=0.0)
    y = st.number_input(label="y coordinate",step=1.,format="%.2f", min_value=0.0)

    coordinate = [x,y]

    buff1, col, buff2 = st.columns([2,3,1])
    buff4, col4, buff4 = st.columns([2,3,1])
    col2, col3 = st.columns([5,1])

    with col:
        if st.button('Add Coordinate'):
            if len(coordinate) < 2:
                st.write("Need to input 2 values, try again")
            else:

                if "nbPoints" not in st.session_state:
                    st.session_state["nbPoints"] = 1
                else:
                    st.session_state.nbPoints += 1


                if "objPoints" not in st.session_state:
                    st.session_state["objPoints"] = [coordinate]
                    st.write(st.session_state["objPoints"])
                else:
                    temp = st.session_state.objPoints
                    temp.append(coordinate)
                    st.session_state.objPoints =  temp
                    st.write(st.session_state.objPoints)
                
                print("ObjPoints ", st.session_state.objPoints)
                print("nb of Points = ", st.session_state.nbPoints )

            


    if "nbPoints" in st.session_state:
        if st.session_state.nbPoints >= 4:
            with col4:
                st.write("Able to apply Homography")
            with col3:
                if st.button("Next"):
                    st.switch_page("Pages/1_PixelsInput.py")


    with col2:
        if st.button("Reset"):
                
                st.write('Session State Variables Has been reset')
                resetSessionVariables()


    