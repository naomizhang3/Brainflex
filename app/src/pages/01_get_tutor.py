import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

ORDERED = ["user_id", "first_name", "last_name", "bio"]
UI_ORDERED = ["Tutor ID", "First Name", "Last Name", "Bio"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Tutor Search')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")


col1, col2 = st.columns(2)

# add one number input for variable 1 into column 1
with col1:
  var_01 = st.text_input('Department ID:')

# add another number input for variable 2 into column 2
with col2:
  var_02 = st.text_input('Course Number:')

logger.info(f'var_01 = {var_01}')
logger.info(f'var_02 = {var_02}')


if st.button('Find Tutors',
             type='primary',
             use_container_width=True):
  results = requests.get(f'http://api:4000/s/tutors/{var_01}/{var_02}').json()
  results_df = pd.DataFrame(results)
  tutors_df = results_df[[col for col in ORDERED]].rename(columns=COL_MAPPER)
  st.dataframe(tutors_df)