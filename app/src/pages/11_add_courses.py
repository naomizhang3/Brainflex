import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add a side bar
SideBarLinks()

# set the header of the page
st.header('Which course do you want to tutor for?')

# add spacing for visual clarity
st.text("")

# create a form to register for a new tutorable course
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