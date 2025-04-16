import logging
logger = logging.getLogger(__name__)
import streamlit as st
import plotly.express as px
from modules.nav import SideBarLinks
import requests

LABELS = {"value": "Average Rating"}

# add a sidebar
SideBarLinks()

# set the header of the page
st.header("View Average Ratings")

# add spacing for visual clarity
st.text("")

# create a histogram to display the average ratings data
ratings_data = requests.get("http://api:4000/a/bookings").json()
ratings_lst = [row["Overall Average Rating"] for row in ratings_data]
fig = px.histogram(ratings_lst, nbins=5, labels=LABELS, 
                       title="Average Tutor Ratings")
fig.update_layout(yaxis_title="Count", showlegend=False)
st.plotly_chart(fig)