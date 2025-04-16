import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks
import requests

ORDERED = ["user_id", "first_name", "last_name", "bio"]
UI_ORDERED = ["Tutor ID", "First Name", "Last Name", "Bio"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# add side bar
SideBarLinks()

# set the header of the page
st.header('Tutor Search')
st.write(f"### Hi, {st.session_state['first_name']}.")

# create columns to get user input about the course
col1, col2 = st.columns(2)
with col1:
  var_01 = st.text_input('Department ID:')
with col2:
  var_02 = st.text_input('Course Number:')

logger.info(f'var_01 = {var_01}')
logger.info(f'var_02 = {var_02}')

# retrieve relevant data from the database
if st.button('Find Tutors',
             type='primary',
             use_container_width=True):
  results = requests.get(f'http://api:4000/s/tutors/{var_01}/{var_02}').json()
  results_df = pd.DataFrame(results)
  try:
    tutors_df = results_df[[col for col in ORDERED]].rename(columns=COL_MAPPER)
    st.dataframe(tutors_df)
  except:
    st.error("No available tutors for this course :(")