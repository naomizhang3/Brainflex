import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add a side bar
SideBarLinks()

# set the header of the page
st.header("Academic Advisor Requests")

request_data = requests.get("http://api:4000/admin/advrequests").json()
