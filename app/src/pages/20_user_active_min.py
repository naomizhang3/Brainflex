import logging
logger = logging.getLogger(__name__)
import streamlit as st
import plotly.express as px
from modules.nav import SideBarLinks
import requests

API_LINK = "http://api:4000/a/useractivity"
LABELS = {"value": "Active Minutes", "count": "Count"}

# add side bar
SideBarLinks()

# set the header of the page
st.header("View User Activity")

# add spacing for visual clarity
st.text("")

response = requests.get(API_LINK).json() 
student_data = response["students"]
tutor_data = response["tutors"]
student_active_min = [row["active_min"] for row in student_data]
tutor_active_min = [row["active_min"] for row in tutor_data]

# format columns
col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(student_active_min, nbins=10, labels=LABELS, 
                       title="Student Activity")
    fig.update_layout(yaxis_title="Count", showlegend=False)
    st.plotly_chart(fig)

with col2:
    fig = px.histogram(tutor_active_min, nbins=10, labels=LABELS, title="Tutor Activity")
    fig.update_layout(yaxis_title="Count", showlegend=False)
    st.plotly_chart(fig)
