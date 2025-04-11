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

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Getting tutors for courses')

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


if st.button('Calculate Prediction',
             type='primary',
             use_container_width=True):
  results = requests.get(f'http://api:4000/s/tutors/{var_01}/{var_02}').json()
#   results = requests.get(f'http://api:4000/c/prediction/{var_01}/{var_02}').json()
  st.dataframe(results)