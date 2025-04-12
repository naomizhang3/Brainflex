import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("Add Bio")

backup_data = requests.get("http://api:4000/t/backupschedule").json()
st.dataframe(backup_data)