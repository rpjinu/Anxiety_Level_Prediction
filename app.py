import streamlit as st
import joblib
import numpy as np

# Load your trained model (ensure the model is in the same directory or provide the correct path)
model = joblib.load(r'C:\Users\Ranjan kumar pradhan\.vscode\model.pkl')  # Load the saved model

# Title of the app
st.title('Anxiety Severity Predictor')

# Collecting user input
age = st.number_input('Age', min_value=18, max_value=100, value=25)
gender = st.selectbox('Gender', options=['Female', 'Male', 'Other'], index=1)
occupation = st.selectbox('Occupation', options=['Other', 'Teacher', 'Doctor', 'Student', 'Unemployed', 'Engineer'])
sleep_hours = st.slider('Sleep Hours', min_value=0.0, max_value=12.0, step=0.1, value=7.0)
physical_activity = st.slider('Physical Activity (hrs/week)', min_value=0.0, max_value=20.0, step=0.1, value=5.0)
caffeine_intake = st.slider('Caffeine Intake (mg/day)', min_value=0, max_value=1000, step=1, value=100)
alcohol_consumption = st.slider('Alcohol Consumption (drinks/week)', min_value=0, max_value=50, step=1, value=2)
smoking = st.selectbox('Smoking', options=['No', 'Yes'])
stress_level = st.slider('Stress Level (1-10)', min_value=1, max_value=10, step=1, value=5)
breathing_rate = st.slider('Breathing Rate (breaths/min)', min_value=10, max_value=40, step=1, value=20)
sweating_level = st.slider('Sweating Level (1-5)', min_value=1, max_value=5, step=1, value=3)
dizziness = st.selectbox('Dizziness', options=['No', 'Yes'])
therapy_sessions = st.slider('Therapy Sessions (per month)', min_value=0, max_value=20, step=1, value=2)
recent_major_life_event = st.selectbox('Recent Major Life Event', options=['No', 'Yes'])
diet_quality = st.slider('Diet Quality (1-10)', min_value=1, max_value=10, step=1, value=7)

# Mapping categorical inputs to numerical values for model input
gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
occupation_map = {'Other': 0, 'Teacher': 1, 'Doctor': 2, 'Student': 3, 'Unemployed': 4, 'Engineer': 5}
smoking_map = {'No': 0, 'Yes': 1}
dizziness_map = {'No': 0, 'Yes': 1}
recent_major_life_event_map = {'No': 0, 'Yes': 1}

# Convert inputs to numerical format
gender_num = gender_map[gender]
occupation_num = occupation_map[occupation]
smoking_num = smoking_map[smoking]
dizziness_num = dizziness_map[dizziness]
recent_major_life_event_num = recent_major_life_event_map[recent_major_life_event]

# Prepare the input data in the correct format (model expects a 2D array)
input_data = np.array([[age, gender_num, occupation_num, sleep_hours, physical_activity,
                        caffeine_intake, alcohol_consumption, smoking_num, stress_level,
                        breathing_rate, sweating_level, dizziness_num, therapy_sessions,
                        recent_major_life_event_num, diet_quality]])

# Display the collected inputs
st.subheader('Input Summary:')
st.write({
    'Age': age,
    'Gender': gender_num,
    'Occupation': occupation_num,
    'Sleep Hours': sleep_hours,
    'Physical Activity': physical_activity,
    'Caffeine Intake': caffeine_intake,
    'Alcohol Consumption': alcohol_consumption,
    'Smoking': smoking_num,
    'Stress Level': stress_level,
    'Breathing Rate': breathing_rate,
    'Sweating Level': sweating_level,
    'Dizziness': dizziness_num,
    'Therapy Sessions': therapy_sessions,
    'Recent Major Life Event': recent_major_life_event_num,
    'Diet Quality': diet_quality
})

# Predicting the target value (Severity of Anxiety Attack)
if st.button('Predict Severity of Anxiety Attack'):
    prediction = model.predict(input_data)  # Make prediction
    st.subheader('Predicted Severity of Anxiety Attack:')
    st.write(f"The predicted severity of anxiety attack is: {int(prediction[0])}")

