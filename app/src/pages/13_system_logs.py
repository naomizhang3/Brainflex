import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add side bar
SideBarLinks()

# set the header of the page
st.header("System Logs")

# get relevant data
log_data = requests.get("http://api:4000/admin/systemlogs").json()
log_lines = []
for row in log_data:
    creation_date = row["creation_date"]
    log_name = row["type_name"]
    log_lines.append(f"{creation_date} {log_name}")

# format data to look like system logs
st.code("\n".join(log_lines), language="text")