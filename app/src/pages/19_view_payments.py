import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

ORDERED = ["amount", "earned_date", "payment_date", "transaction_status", 
           "booking_id", "recipient_id"]
UI_ORDERED = ["Amount ($)", "Date Earned", "Payment Date", 
              "Transaction Status", "Booking ID", "Recipient ID"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("View outgoing payments")

# add spacing for visual clarity
st.text("")

payments_df = requests.get("http://api:4000/a/payments").json()
payments_df = pd.DataFrame(payments_df)
payments_df = payments_df[ORDERED].rename(columns=COL_MAPPER)
st.dataframe(payments_df)