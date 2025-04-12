import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

API_LINK = "http://api:4000/a/useractivity"

# set the header of the page
st.header("View User Activity")

# add spacing for visual clarity
st.text("")

# format columns
col1, col2 = st.columns(2)

response = requests.get(API_LINK).json()
    
 # get student activity data and display
student_data = response.get("students")
student_df = pd.DataFrame(student_data)
ordered_cols = ["user_id", "active_min"]
student_df = student_df[ordered_cols]

# get tutor activity data and display
tutor_data = response.get("tutors")
tutor_df = pd.DataFrame(tutor_data)
tutor_df = tutor_df[ordered_cols]

student_df_display = student_df.reset_index(drop=True)
tutor_df_display = tutor_df.reset_index(drop=True)

# display student and tutor activity data
with col1:
    st.subheader("Student Activity")
    st.table(student_df_display)

with col2:
    st.subheader("Tutor Activity")
    st.table(tutor_df_display)
