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
    st.sidebar.page_link("pages/07_view_tutor_bookings.py", label="↳ All Booked Sessions")
    st.sidebar.page_link("pages/08_delete_tutor_bookings.py", label="↳ Cancel Bookings")
    st.sidebar.page_link("pages/09_add_bio.py", label="↳ Add Bio")
    st.sidebar.page_link("pages/10_view_earnings.py", label="↳ Earnings Dashboard")
    st.sidebar.page_link("pages/11_add_courses.py", label="↳ Add Tutorable Courses")

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/12_admin_home.py", label="System Administrator Home", icon="🖥️")
    st.sidebar.page_link("pages/13_system_logs.py", label="↳ System Logs")
    st.sidebar.page_link("pages/14_backup_schedule.py", label="↳ Backup Schedule")
    st.sidebar.page_link("pages/15_requests_review.py", label="↳ Advisor Requests")
    st.sidebar.page_link("pages/16_edit_student_data.py", label="↳ Student Data")

#### ------------------------ Academic Advisor Role ------------------------
def AdvisorPageNav():
    st.sidebar.page_link("pages/17_advisor_home.py", label="Academic Advisor Home", icon="👨‍🏫")
    st.sidebar.page_link("pages/18_send_requests.py", label="↳ Send Requests")
    st.sidebar.page_link("pages/19_view_payments.py", label="↳ View Payments")
    st.sidebar.page_link("pages/20_user_active_min.py", label="↳ User Activity")
    st.sidebar.page_link("pages/21_booking_ratings.py", label="↳ Average Ratings")
    st.sidebar.page_link("pages/22_tutor_supply.py", label="↳ Tutor Supply")

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

    # Show the other page navigators depending on the users'role.
    if st.session_state["authenticated"]:

        if st.session_state["role"] == "student":
            StudentPageNav()

        if st.session_state["role"] == "tutor":
            TutorPageNav()

        if st.session_state["role"] == "administrator":
            AdminPageNav()
        
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
