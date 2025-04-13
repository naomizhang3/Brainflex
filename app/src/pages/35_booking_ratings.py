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
st.header("View Booking Ratings")

# add spacing for visual clarity
st.text("")

# displays average rating for each tutor in a table
ratings_df = requests.get("http://api:4000/a/bookings").json()
ratings_df = pd.DataFrame(ratings_df)
ratings_df.columns = ["Average Rating", "Tutor First Name", "Tutor Last Name", "Tutor ID"]
st.dataframe(ratings_df)