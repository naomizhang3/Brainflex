# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Student Role ------------------------
def StudentPageNav():
    st.sidebar.page_link("pages/00_student_home.py", label="Student Home", icon="🧑‍🎓")
    st.sidebar.page_link("pages/01_get_tutor.py", label="↳ Find Tutors")
    st.sidebar.page_link("pages/02_view_bookings.py", label="↳ All Booked Sessions")
    st.sidebar.page_link("pages/03_create_bookings.py", label="↳ Book a Session")
    st.sidebar.page_link("pages/04_reschedule_booking.py", label="↳ Reschedule Bookings")
    st.sidebar.page_link("pages/05_cancel_bookings.py", label="↳ Cancel Bookings")

#### ------------------------ Tutor Role ------------------------
def TutorPageNav():
    st.sidebar.page_link("pages/06_tutor_home.py", label="Tutor Home", icon="🧑‍🏫")
    st.sidebar.page_link("pages/13_view_tutor_bookings.py", label="↳ All Booked Sessions")
    st.sidebar.page_link("pages/13_delete_bookings.py", label="↳ Cancel Bookings")
    st.sidebar.page_link("pages/13_add_bio.py", label="↳ Add Bio")
    st.sidebar.page_link("pages/04_reschedule_booking.py", label="↳ Reschedule Bookings")
    st.sidebar.page_link("pages/05_cancel_bookings.py", label="↳ Cancel Bookings")

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/11_admin_home.py", label="System Administrator Home", icon="🖥️")
    st.sidebar.page_link("pages/12_system_logs.py", label="↳ System Logs")
    st.sidebar.page_link("pages/13_backup_schedule.py", label="↳ Backup Schedule")
    st.sidebar.page_link("pages/14_requests_review.py", label="↳ Advisor Requests")
    st.sidebar.page_link("pages/15_edit_student_data.py", label="↳ Student Data")

#### ------------------------ Academic Advisor Role ------------------------
def AdvisorPageNav():
    st.sidebar.page_link("pages/31_advisor_home.py", label="Academic Advisor Home", icon="👨‍🏫")
    st.sidebar.page_link("pages/32_send_requests.py", label="↳ Send Requests")
    st.sidebar.page_link("pages/33_view_payments.py", label="↳ View Payments")
    st.sidebar.page_link("pages/34_user_active_min.py", label="↳ User Activity")
    st.sidebar.page_link("pages/35_booking_ratings.py", label="↳ Booking Ratings")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "student":
            StudentPageNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "advisor":
            AdvisorPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
