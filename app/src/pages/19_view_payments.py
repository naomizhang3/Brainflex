import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks
import requests

ORDERED = ["amount", "earned_date", "payment_date", "transaction_status", 
           "booking_id", "recipient_id"]
UI_ORDERED = ["Amount ($)", "Date Earned", "Payment Date", 
              "Transaction Status", "Booking ID", "Recipient ID"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# add a side bar
SideBarLinks()

# set the header of the page
st.header("View Outgoing Payments")

# add spacing for visual clarity
st.text("")

# retrieve payments data and make it a df
payments_df = requests.get("http://api:4000/a/payments").json()
payments_df = pd.DataFrame(payments_df)

# rename the columns and re-index the df for a more intuitive user experience
payments_df = payments_df[ORDERED].rename(columns=COL_MAPPER)
payments_df.index = range(1, len(payments_df) + 1)

# display the df
st.dataframe(payments_df)