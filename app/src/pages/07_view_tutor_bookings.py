import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

# add a side bar
SideBarLinks()

# set up the header
st.header(f"Hi, {st.session_state['first_name']}! View your bookings.")

# retrieve information about bookings from the database
results = requests.get(f"http://api:4000/t/bookings/{st.session_state['user_id']}").json()

# format the retrieved data
ids = []
names = []
times = []
for row in results:
    id = row["booking_id"]
    name = f"{row['first_name']} {row['last_name']}"
    time = row["scheduled_time"]
    ids.append(id)
    names.append(name)
    times.append(time)

# rename the columns and re-index the df for a more intuitive user experience
bookings = pd.DataFrame({"Booking ID": ids, "Student": names, "Scheduled Time": times})
bookings.index = range(1, len(bookings) + 1)

# display the df
st.dataframe(bookings)

