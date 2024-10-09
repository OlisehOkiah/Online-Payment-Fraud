import streamlit as st
import random
from PIL import Image
from prediction import pred_page

    

# home.py
def home_page():
    st.title("Welcome to the Online Payment Fraud Detection App! 🎉")

    st.markdown(
        """This app helps to detect potential fraudulent transactions in online payment systems using a machine learning model."""
    )

    # Add custom CSS for styling
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        body {
            background-size: cover;  
            background-repeat: no-repeat; 
            color: white;  
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        h2 {
            color: #2E7D32;
        }
        .fun-fact {
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display an animated GIF or image
    st.markdown(
        """
        <div style='text-align: center'>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXUxZWFlaDZzaW80MXJnMTVhMXEycHM1ZWRsM3doZTk4Z2RiaXJ6bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hgjNPEmAmpCMM/giphy.gif" alt="Fraud Detection GIF" width="500">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Fun Facts section with random tips
    fun_facts = [
        "Did you know? Fraud detection saves online businesses millions every year! 💸",
        "Stay safe online! Always verify suspicious emails before clicking. 🔐",
        "Machine learning models can detect fraud with over 90% accuracy! 🧠",
        "Fraudulent transactions often happen late at night or on holidays! 🌙",
    ]
    
    st.subheader("💡 Fun Fact of the Day")
    st.markdown(f"<div class='fun-fact'>{random.choice(fun_facts)}</div>", unsafe_allow_html=True)

    # Interactive quiz section
    st.subheader("🧠 Test Your Knowledge!")
    
    # First quiz question
    quiz_question1 = st.radio(
        "What percentage of fraudulent transactions involve small amounts of money?",
        ("10%", "30%", "50%", "70%")
    )
    
    if quiz_question1 == "50%":
        st.success("Correct! 🎉 Many fraudsters prefer smaller amounts to avoid detection.")
    elif quiz_question1:
        st.error("Try again! Fraudsters often fly under the radar with small amounts.")

    # Second quiz question
    quiz_question2 = st.radio(
        "What is the most common type of online fraud?",
        ("A) Identity theft", "B) Credit card fraud", "C) Phishing", "D) Account takeover"),
        key='second_quiz'  # Unique key for this widget
    )

    if quiz_question2 == "B) Credit card fraud":
        st.success("Correct! 🎉 Credit card fraud is one of the most prevalent types of online fraud.")
    elif quiz_question2:
        st.error("Try again! Credit card fraud is very common in online transactions.")

    # A button to switch to the prediction page
    if st.button("Go to Predictions"):
        st.session_state.selected = "Prediction"  # Update session state to go to Prediction

    # Footer message
    st.write("Enjoy your experience with fraud detection! 💻🔍")