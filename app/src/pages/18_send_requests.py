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

rtypes_data = requests.get("http://api:4000/a/requesttypes").json()
rtype_options = {row["request_name"]: row["type_id"] for row in rtypes_data}

# sending requests to admin
st.write("Send a New Request to Admin")
with st.form("send_request_form"):
    description = st.text_input("Description: ")
    sent_by =  st.session_state['user_id']
    input_rtype = st.selectbox("Select Request Type", list(rtype_options.keys()))
    type_id = rtype_options[input_rtype]

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "description": description,
            "sent_by": sent_by,
            "type_id": type_id
        }

        response = requests.post("http://api:4000/a/requests", json = data)
        #st.write("Status code:", response.status_code)
        #st.write("Response body:", response.text)
        if response.status_code == 200:
            st.success("Request successfully sent.")
        else:
            st.error("Failed to send request.")