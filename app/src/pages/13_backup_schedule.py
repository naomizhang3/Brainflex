import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add a sidebar
SideBarLinks()

# set the header of the page
st.header("Backup Schedule")

# get relevant data
backup_data = requests.get("http://api:4000/admin/backupschedule").json()
backup_lines = []
for row in backup_data:
    date = row["backup_date"]
    status = row["backup_status"]
    first, last = row["first_name"], row["last_name"]
    line = f"{date} Status: {status} \n{date} Assigned Admin: {first} {last}"
    backup_lines.append(line)

# format data to look like system logs
st.code("\n".join(backup_lines), language="text")