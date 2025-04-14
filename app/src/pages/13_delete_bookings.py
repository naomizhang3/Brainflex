import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

# add side bar links
SideBarLinks()

# add the header
st.header("Delete Booking")

# add spacing for visual clarity
st.text("")

with st.form("delete_booking_form"):
    booking_id = st.text_input('Booking ID: ')
    confirm = st.checkbox("I understand that this action cannot be undone.")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not confirm:
        st.error("You must check the box to proceed.")
    else:
        data = {"booking_id": booking_id}

        response = requests.delete("http://api:4000/t/deletebookings", json=data)
        if response.status_code == 200:
            st.success("Boooking successfully deleted.")
        else:
            st.error("Failed to delete booking")
