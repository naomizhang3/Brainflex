import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
from datetime import datetime


st.set_page_config(layout = 'wide')

# add side bar
SideBarLinks()

# set a header
st.header('Reschedule a Booking')

# create a form to reschedule a booking
with st.form("reschedulebooking"):
  user_id = st.session_state['user_id']
  booking_id = st.text_input("Booking Id")
  selected_date = st.date_input("Pick a date: ")
  selected_time = st.time_input("Pick a time: ")
  combined_datetime = datetime.combine(selected_date, selected_time)
  

  submitted = st.form_submit_button("Submit")

  if submitted:
      data = {
          "time" : combined_datetime.isoformat(),
      }

      response = requests.put(f"http://api:4000/s/bookings/{user_id}/{booking_id}", json=data)
      if response.status_code == 200:
          st.success("Booking Sucessfully Rescheduled")
      else:
          st.error("Failed.")