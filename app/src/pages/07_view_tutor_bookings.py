import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
from modules.nav import SideBarLinks
import requests

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.header(f"Hi, {st.session_state['first_name']}! View your bookings.")

results = requests.get(f"http://api:4000/t/bookings/{st.session_state['user_id']}").json()
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
bookings = pd.DataFrame({"Booking ID": ids, "Student": names, "Scheduled Time": times})
bookings.index = range(1, len(bookings) + 1)
st.dataframe(bookings)

