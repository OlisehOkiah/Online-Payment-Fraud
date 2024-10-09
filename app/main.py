import streamlit as st
from streamlit_option_menu import option_menu
import random

st.set_page_config(page_title="Online Payment Fraud Detection", layout="centered")
from home import home_page
from prediction import pred_page

# Initialize session state for selected page
if 'selected' not in st.session_state:
    st.session_state.selected = "Home"

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction"],
        icons=["house", "graph-up-arrow"],
        menu_icon="cast",
        default_index=0
    )

    # Update session state when an option is selected from the sidebar
    st.session_state.selected = selected

# Render the selected page
if st.session_state.selected == "Home":
    home_page()
elif st.session_state.selected == "Prediction":
    pred_page()