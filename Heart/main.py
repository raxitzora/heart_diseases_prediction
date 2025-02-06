# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Load the trained model (Ensure this path is correct)
model = joblib.load('D:\\Heart\\eda\\heart_disease_model.pkl')

# Streamlit UI elements for input
st.title("Heart Disease Prediction")

st.write("""
This application predicts the likelihood of having heart disease based on your medical data.
Please fill in the following details:
""")

# Input fields for user to provide data
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
chest_pain_type = st.selectbox("Chest Pain Type", options=[1, 2, 3, 4], format_func=lambda x: f"Type {x}")
resting_bp_s = st.number_input("Resting Blood Pressure (s)", min_value=0)
cholesterol = st.number_input("Cholesterol", min_value=0)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
resting_ecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2], format_func=lambda x: f"Type {x}")
max_heart_rate = st.number_input("Maximum Heart Rate Achieved", min_value=0)
exercise_angina = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.number_input("Oldpeak", min_value=0.0, step=0.1)
st_slope = st.selectbox("ST Slope", options=[1, 2, 3], format_func=lambda x: f"Type {x}")

# Convert input data into a DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'chest pain type': [chest_pain_type],
    'resting bp s': [resting_bp_s],
    'cholesterol': [cholesterol],
    'fasting blood sugar': [fasting_blood_sugar],
    'resting ecg': [resting_ecg],
    'max heart rate': [max_heart_rate],
    'exercise angina': [exercise_angina],
    'oldpeak': [oldpeak],
    'ST slope': [st_slope]
})

# Prediction button with a loading spinner
if st.button("Predict Heart Disease"):
    with st.spinner('Making prediction...'):
        prediction = model.predict(input_data)
    
    if prediction == 0:
        st.write("No Heart Disease Detected!")
    else:
        st.write("Heart Disease Detected! Please consult a doctor.")
