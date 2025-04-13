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

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("View your earnings")

# add spacing for visual clarity
st.text("")

payments_df = requests.get("http://api:4000/t/transactions").json()
payments_df = pd.DataFrame(payments_df)
ordered_cols = ["amount", "earned_date", "payment_date", "transaction_status"]
payments_df = payments_df[ordered_cols]
st.dataframe(payments_df)