import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks
import requests

ORDERED = ["amount", "payment_date", "transaction_status"]
UI_ORDERED = ["Amount ($)", "Date Received", "Transaction Status"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("View Your Earnings")

# add spacing for visual clarity
st.text("")

payments_df = requests.get("http://api:4000/t/transactions").json()
payments_df = pd.DataFrame(payments_df)
payments_df = payments_df[ORDERED].rename(columns=COL_MAPPER)
st.dataframe(payments_df)