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

if st.button('View Bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_view_tutor_bookings.py')

if st.button("Cancel Bookings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_delete_bookings.py')

if st.button("Add Bio",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_add_bio.py')

if st.button("View Earnings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_view_earnings.py')
  

if st.button("Add tutorable courses",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_add_courses.py')