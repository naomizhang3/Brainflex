import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

# add a side bar
SideBarLinks()

# set the header of the page
st.header("Academic Advisor Requests")

# retrieve and display requests data
request_data = requests.get("http://api:4000/admin/advrequests").json()
ordered_cols = ["request_name", "descr", "review_status"]
request_df = pd.DataFrame(request_data)
request_df = request_df[[col for col in ordered_cols]]
st.dataframe(request_df)