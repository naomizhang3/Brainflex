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
from datetime import datetime

API_LINK = "http://api:4000/s/createbookings"

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Create Booking')

# Add spacing for visual clarity
st.text("")

student_id = st.session_state['user_id']
booking_data = requests.get(f"http://api:4000/s/bookings/{student_id}").json()
booking_data_df = pd.DataFrame(booking_data)
st.dataframe(booking_data_df)

st.write("Schedule a Booking")
with st.form("create_booking_form"):
    booking_id = st.text_input("Booking Id")
    selected_date = st.date_input("Pick a date: ")
    selected_time = st.time_input("Pick a time: ")
    combined_datetime = datetime.combine(selected_date, selected_time)
    tutor_id = st.text_input("Enter a Tutor's Id")

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "booking_id": booking_id,
            "completion_status": True,
            "creation_time": datetime.now().isoformat(),
            "scheduled_time": combined_datetime.isoformat(),
            "tutor_id": tutor_id,
            "student_id": st.session_state['user_id'],
        }

        response = requests.post(API_LINK, json=data)
        if response.status_code == 200:
            st.success("Booking successfully created.")
        else:
            st.error(f"Failed to schedule booking")