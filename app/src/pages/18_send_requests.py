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
st.header("Send Requests to Admin")

st.text("")

col1, = st.columns(1)

# sending requests to admin
with col1:
    st.write("Send a New Request to Admin")
    with st.form("send_request_form"):
        request_id = st.text_input("Request ID: ")
        description = st.text_input("Description: ")
        sent_by = st.text_input("Sent By: ")
        type_id = st.text_input("Type ID: ")

        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "request_id": request_id,
                "description": description,
                "sent_by": sent_by,
                "type_id": type_id
            }

            response = requests.post("http://api:4000/a/requests", json = data)
            #st.write("Status code:", response.status_code)
            #st.write("Response body:", response.text)
            if response.status_code == 200:
                st.success("Request successfully sent")
            else:
                st.error("Failed to send request")