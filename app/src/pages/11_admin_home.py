import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome System Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button("Check all system logs", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_system_logs.py')

if st.button("View backup schedule", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

if st.button("Review requests from academic advisors", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_API_Test.py')

if st.button("Add students to the system",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')

if st.button("Remove students from the system",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')