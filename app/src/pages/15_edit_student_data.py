import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

API_LINK = "http://api:4000/admin/studentdata"

# add side bar links
SideBarLinks()

# set the header of the page
st.header("Student Data")

# add a dataframe of student data
student_data = pd.DataFrame(requests.get(API_LINK).json())
ordered_cols = ["user_id", "nu_id", "first_name", "MI", "last_name", "status"]
student_data = [student_data[col] for col in ordered_cols]
with st.expander("View All Student Data"):
    st.dataframe(student_data)

# add spacing for visual clarity
st.text("")

# add columns for adding/removing student data
col1, col2 = st.columns(2)

# create a form to submit additional student data
with col1:
    st.write("Add New Student to System")
    with st.form("add_student_form"):
        user_id = st.text_input('User ID:')
        nu_id = st.text_input('NUID:')
        first_name = st.text_input('First Name:')
        last_name = st.text_input('Last Name:')
        
        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "user_id": user_id,
                "nu_id": nu_id,
                "fn": first_name,
                "ln": last_name
            }

            response = requests.post(API_LINK, 
                                     json=data)
            if response.status_code == 200:
                st.success("Student successfully added.")
            else:
                st.error(f"Failed to add student.")

# create a form to remove student data
with col2:
    st.write("Remove Student from System")
    with st.form("remove_student_form"):
        user_id = st.text_input('User ID:')
        confirm = st.checkbox("I understand that this action cannot be undone.")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not confirm:
                st.error("You must check the box to proceed.")
            else:
                data = {"user_id": user_id}

                response = requests.delete(API_LINK, json=data)
                if response.status_code == 200:
                    st.success("Student data successfully deleted.")
                else:
                    st.error(f"Failed to delete student data.")