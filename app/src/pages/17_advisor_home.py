import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# add a sidebar
SideBarLinks()

# welcome the advisor
st.title(f"Welcome Academic Advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# links to advisor pages
if st.button("Send requests to admin", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/18_send_requests.py')

if st.button("View payments", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/19_view_payments.py')

if st.button("View active user time", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/20_user_active_min.py')

if st.button("View booking ratings",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_booking_ratings.py')
  
if st.button("View tutor availability per course",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_tutor_supply.py')