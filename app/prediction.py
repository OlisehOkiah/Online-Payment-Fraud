# Streamlit app
import streamlit as st
import numpy as np 
import pickle

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

def pred_page():
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

pred_page()
