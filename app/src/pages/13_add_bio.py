import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd


# for post/tutors add bio
# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()


# set the header of the page
st.header("Add Bio")


# add spacing for visual clarity
st.text("")

# adding new info to bio
st.write("Add information for bio")

with st.form("add_tutor_bio"):
    user_id = st.session_state['user_id']
    bio = st.text_input('Bio:')

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "user_id" : user_id,
            "bio" : bio
        }

        response = requests.put("http://api:4000/t/add_bio", json=data)
        if response.status_code == 200:
            st.success("Bio successfully added.")
        else:
            st.error("Failed to add bio.")


