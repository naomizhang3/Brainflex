import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
from datetime import datetime

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Which course do you want to tutor for?')

# Add spacing for visual clarity
st.text("")

with st.form("register_courses"):
    course_id = st.text_input("Course Id")
    course_num = st.text_input("Course Number")
    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "course_id": course_id,
            "course_num": course_num,
        }

        response = requests.post(f"http://api:4000/t/register-couses/{st.session_state['user_id']}", json=data)
        if response.status_code == 200:
            st.success(f"You are now able to tutor for {course_id} {course_num}.")
        else:
            st.error(f"Failed to add course.")