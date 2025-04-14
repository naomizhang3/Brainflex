import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.header(f"View {st.session_state['first_name']}'s bookings")

results = requests.get(f"http://api:4000/t/bookings/{st.session_state['user_id']}").json()
st.dataframe(results)

