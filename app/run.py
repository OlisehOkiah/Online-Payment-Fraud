import streamlit as st
import numpy as np
import pickle
import os
from streamlit_option_menu import option_menu

# Initialize session state for selected page
if 'selected' not in st.session_state:
    st.session_state.selected = "Home"

# Load the model function
@st.cache_resource
def load_model():
    model_path = os.path.join(os.getcwd(), 'model.pkl')
    try:
        with open(model_path, "rb") as file:  # Use relative path
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please ensure model.pkl is in the correct directory.")
        return None  # Return None or handle appropriately if the model isn't found

# Home page function
def home_page():
    st.title("Welcome to the Online Payment Fraud Detection App! 🎉")
    st.markdown(
        """This app helps to detect potential fraudulent transactions in online payment systems using a machine learning model."""
    )
    # Additional content can be added here

# Prediction page function
def pred_page(model):
    st.title("Fraud Detection: Input Transaction Details")
    
    # Input values for prediction
    step = st.number_input("Step", min_value=1, max_value=743, value=1)
    amount = st.number_input("Amount", min_value=0.0, max_value=1e6, value=1000.0)
    oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0, max_value=1e6, value=1000.0)
    newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0, max_value=1e6, value=500.0)
    balance_diff_org = oldbalanceOrg - newbalanceOrig

    oldbalanceDest = st.slider("Old Balance (Destination)", min_value=0.0, max_value=1e6, value=0.0)
    newbalanceDest = st.slider("New Balance (Destination)", min_value=0.0, max_value=1e6, value=0.0)
    balance_diff_dest = oldbalanceDest - newbalanceDest

    # Predict button
    if st.button('Predict Fraud'):
        # Prepare input data
        input_data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig, balance_diff_org, balance_diff_dest]])
        
        # Predict using the trained model
        prediction = model.predict(input_data)
        
        # Output the prediction result
        if prediction[0] == 1:
            st.write("⚠️ This transaction is predicted to be fraudulent!")
        else:
            st.write("✅ This transaction is predicted to be non-fraudulent.")

# Main function to run the Streamlit app
def main():
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

    # Load the model once at the start
    model = load_model()

    # Render the selected page
    if st.session_state.selected == "Home":
        home_page()
    elif st.session_state.selected == "Prediction" and model is not None:
        pred_page(model)

# Run the app using the __main__ block
if __name__ == "__main__":
    main()
