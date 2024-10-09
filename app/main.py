import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Online Payment Fraud Detection", layout="centered")
from .home import home_page
from .prediction import pred_page

with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=["Home", "Prediction"],
        icons=["house", "graph-up-arrow"],
        menu_icon="cast",
        default_index=0
    )

if selected=="Home":
    home_page()

elif selected =="Prediction":
    pred_page()