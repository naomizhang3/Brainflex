import logging
logger = logging.getLogger(__name__)
import streamlit as st
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# add a sidebar
SideBarLinks()

# set the header of the page
st.header("View tutor supply per course")

# add spacing for visual clarity
st.text("")

# create a histogram to display the average ratings data
tutor_data = requests.get("http://api:4000/a/tutorsupplies").json()

st.dataframe(tutor_data)