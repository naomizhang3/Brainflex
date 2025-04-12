import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Tutor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')  

if st.button('Find students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_find_students.py')

if st.button('View Bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

if st.button("Reschedule Bookings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_reschedule_bookings.py')

if st.button("Add Bio",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_view_payments.py')

if st.button("View Earnings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_view_payments.py')
  

  