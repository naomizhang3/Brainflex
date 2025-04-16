import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View bookings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/07_view_tutor_bookings.py')

if st.button("Cancel bookings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/08_delete_tutor_bookings.py')

if st.button("Add bio",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/09_add_bio.py')

if st.button("View earnings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_view_earnings.py')
  

if st.button("Add courses to tutor for",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_add_courses.py')