import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

ORDERED = ["request_name", "descr", "review_status"]
UI_ORDERED = ["Request Type", "Description", "Review Status"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# add a side bar
SideBarLinks()

# set the header of the page
st.header("Academic Advisor Requests")

# retrieve and display requests data
request_data = requests.get("http://api:4000/admin/advrequests").json()
request_df = pd.DataFrame(request_data)
request_df = request_df[[col for col in ORDERED]].rename(columns=COL_MAPPER)
st.dataframe(request_df)