import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add side bar links
SideBarLinks()

# add the header
st.header("Cancel a Booking")

# add spacing for visual clarity
st.text("")

# create a form to cancel bookings
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
            st.success("Booking successfully canceled.")
        else:
            st.error("Failed to cancel booking.")
