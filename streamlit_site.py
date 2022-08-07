# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 12:25:14 2022

@author: joebr
"""

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "Joe Briddle", page_icon= ":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Load assets
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ndqyrqfd.json")
img_headshot = Image.open("headshot.jpg")
img_toteboard = Image.open("toteboard.jpg")
lottie_github= load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_cwqf5i6h.json")

#Header Section
with st.container():
    header_image, header_text = st.columns(2)
    with header_image:
        st.image(img_headshot)
    with header_text:
        st.subheader("Hi, I'm Joe :wave:")
        st.title("A Financial Analyst in Denver")
        st.write("I am builing my knowledge in coding primarily through Python.")
        st.write("[Check out my LinkedIn >](https://www.linkedin.com/in/joe-briddle)")

#What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Financial Analyst at Dish Wireless and I am aiming to:
            - build on the coding base I learned while studying Business Analytics at the University of Iowa
            - find ways to automate processes to make my personal and work life easier
            - look for new ways to improve the lives of the people in my community
            
            Feel free to send me a message on LinkedIn!
            """
            )
    with right_column:
        st_lottie(lottie_coding, height=400, key = "coding")

#Experience
with st.container():
    st.write("---")
    st.header("My Experience")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_toteboard, caption = 'Total funds raised by UIDM28')
    with text_column:
        st.subheader("Finance Director, University of Iowa Dance Marathon")
        st.write(
            """
            As Finance Director, I was able to work with so many great people, including my incredible Finance Committee, consisting of 17 other students, as well as 14 other members of the Executive Council.
            
            [Here](https://magazine.foriowa.org/story.php?ed=true&storyid=2166) is an article by the UI Center for Advancement about my involvement in Dance Marathon!
            """
            )
        
#Continued Learning
with st.container():
    st.write("---")
    continued_left, continued_right = st.columns(2)
    with continued_left:
        st.header("Continuing to Learn")
        st.write("##")
        st.write(
            """
            I am always on the search for new ways to learn, including:
            - deepening my understanding of Python
            - building my knowledge of other coding languagesm, such as SQL and R
            - getting involved in non-profit efforts in my community
            
            Check out my [Github](https://github.com/joe-briddle) to see the projects I'm working on!'
            """
            )
    with continued_right:
        st_lottie(lottie_github, height=400, key = "github")
