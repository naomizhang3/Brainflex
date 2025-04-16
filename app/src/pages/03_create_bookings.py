import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks
import requests
from datetime import datetime

API_LINK = "http://api:4000/s/createbookings"
COL_MAPPER = {"booking_id": "Booking ID", "first_name": "First Name", 
              "last_name": "Last Name", "scheduled_time": "Scheduled Time"}

# add side bar
SideBarLinks()

# set the header of the page
st.header('Book a Tutoring Session')

# add spacing for visual clarity
st.text("")

# retrieve relevant data
student_id = st.session_state['user_id']
booking_data = requests.get(f"http://api:4000/s/bookings/{student_id}").json()
booking_data_df = pd.DataFrame(booking_data).rename(columns=COL_MAPPER)
st.dataframe(booking_data_df)

# create a form to add a new booking
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