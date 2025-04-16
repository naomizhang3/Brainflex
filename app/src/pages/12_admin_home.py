import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# add a side bar
SideBarLinks()

# welcome the user
st.title(f"Welcome System Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# add system admin tasks
if st.button("Check all system logs", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_system_logs.py')

if st.button("View backup schedule", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_backup_schedule.py')

if st.button("Review requests from academic advisors", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_requests_review.py')

if st.button("Modify student data",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_edit_student_data.py')