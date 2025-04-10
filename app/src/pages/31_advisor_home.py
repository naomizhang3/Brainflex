import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Academic Advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button("Send a request to an admin", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_send_requests.py')

if st.button("View payments", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_view_payments.py')

if st.button("View active user time", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/34_user_active_min.py')

if st.button("View booking ratings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/35_booking_ratings.py')