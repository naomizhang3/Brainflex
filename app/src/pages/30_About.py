import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About BrainFlex")

st.markdown (
    """
    BrainFlex is a Northeastern tutoring app that leverages a data-driven
    matching system to connect learners with tutors based on personality traits 
    and learning styles. 
    
    By tailoring connections to individual needs, 
    BrainFlex uses data to help students access the necessary academic support 
    to enhance their education. Through the collection, storage, and analysis 
    of data, BrainFlex differentiates itself from existing tutor apps by 
    offering greater personalization for users and greater efficiency and 
    accessibility for system administrators and decision-makers. 

    By blending personalization with interactivity, BrainFlex transforms 
    tutoring into an intuitive and enjoyable experience.
    """
        )
