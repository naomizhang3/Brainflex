import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# add a sidebar
SideBarLinks()

# set the header of the page
st.header("Send Requests to Admin")

# add spacing for visual clarity
st.text("")

# sending requests to admin
st.write("Send a New Request to Admin")
with st.form("send_request_form"):
    request_id = st.text_input("Request ID: ")
    description = st.text_input("Description: ")
    sent_by =  st.session_state['user_id']
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