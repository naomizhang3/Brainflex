import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("Student Data")

student_data = requests.get("http://api:4000/admin/studentdata").json()
with st.expander("View All Student Data"):
    st.dataframe(student_data)

# add spacing for visual clarity
st.text("")

st.write("Add New Student")
with st.form("student_form"):
    system_id = st.text_input('System ID:')
    nu_id = st.text_input('NUID:')
    first_name = st.text_input('First Name:')
    last_name = st.text_input('Last Name:')
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "user_id": system_id,
            "nu_id": nu_id,
            "fn": first_name,
            "ln": last_name
        }

        requests.post("http://api:4000/admin/studentdata", json=data)

# if st.button('Calculate Prediction', type='primary', use_container_width=True):
#   st.write("Hi")