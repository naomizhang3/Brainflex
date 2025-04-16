import logging
logger = logging.getLogger(__name__)
import streamlit as st
import plotly.express as px
from modules.nav import SideBarLinks
import requests
import pandas as pd

# add a sidebar
SideBarLinks()

# set the header of the page
st.header("View Tutor Availability")

# add spacing for visual clarity
st.text("")

# retrieve the data
avail_data = requests.get("http://api:4000/a/tutorsupplies").json()
avail_df = pd.DataFrame(avail_data)
avail_df["Course Name"] = avail_df["dept_id"] + " " + avail_df["course_num"].astype(str)
fig = px.bar(avail_df, x="Course Name", y="Number of Available Tutors", 
             title="Top 5 Courses with the Highest Tutor Availability", 
             color="Course Name")
fig.update_layout(showlegend=False)
st.plotly_chart(fig)