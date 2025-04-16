import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# add side bar
SideBarLinks()

# welcome the student
st.title(f"Welcome, {st.session_state['first_name']}!.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# links to student pages
if st.button('Find tutors', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_get_tutor.py')

if st.button('View all bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_view_bookings.py')

if st.button('Book a session', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_create_bookings.py')

if st.button('Reschedule bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_reschedule_booking.py')
  
if st.button('Cancel bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_cancel_bookings.py')