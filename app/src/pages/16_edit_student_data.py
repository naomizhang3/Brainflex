import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

API_LINK = "http://api:4000/admin/studentdata"
ORDERED = ["user_id", "nu_id", "first_name", "MI", "last_name", 
                "acct_status"]
UI_ORDERED = ["User ID", "NUID", "First Name", "MI", "Last Name", 
                "Account Status"]
COL_MAPPER = {ORDERED[i]: UI_ORDERED[i] for i in range(len(ORDERED))}

# add side bar links
SideBarLinks()

# add the header
st.header("Student Data")

# retrieve and display student data
student_data = requests.get(API_LINK).json()
student_df = pd.DataFrame(student_data)
student_df = student_df[[col for col in ORDERED]].rename(columns=COL_MAPPER)
with st.expander("View All Student Data"):
    st.dataframe(student_df)

# add spacing for visual clarity
st.text("")

# format columns
col1, col2 = st.columns(2)

# submit new student data
with col1:
    st.write("Add New Student to System")
    with st.form("add_student_form"):
        nu_id = st.text_input('NUID:')
        first_name = st.text_input('First Name:')
        last_name = st.text_input('Last Name:')
        
        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "nu_id": nu_id,
                "fn": first_name,
                "ln": last_name
            }

            response = requests.post(API_LINK, json=data)
            if response.status_code == 200:
                st.success("Student successfully added.")
            else:
                st.error(f"Failed to add student.")

# remove student data
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

                response = requests.delete("http://api:4000/admin/studentdata", 
                                            json=data)
                if response.status_code == 200:
                    st.success("Student data successfully deleted.")
                else:
                    st.error(f"Failed to delete student data.")