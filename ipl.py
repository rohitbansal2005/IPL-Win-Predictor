import streamlit as st
import pickle
import pandas as pd

# Load model
try:
    pipe = pickle.load(open('pipe.pkl', 'rb'))
except FileNotFoundError:
    st.error("The model file 'pipe.pkl' is missing. Please upload it to proceed.")
    st.stop()

# Title
st.title('IPL Win Predictor')

# Input options
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

col1, col2 = st.columns(2)  # Use st.columns instead of st.beta_columns

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select host city', sorted(cities))
target = st.number_input('Target', min_value=1, step=1)

col3, col4, col5 = st.columns(3)  # Use st.columns instead of st.beta_columns

with col3:
    score = st.number_input('Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)

# Prediction button
if st.button('Predict Probability'):
    if overs == 0:
        st.error("Overs cannot be zero. Please input a valid number.")
    elif overs * 6 > 120:
        st.error("Overs completed cannot exceed 20. Please input a valid value.")
    elif score > target:
        st.error("Score cannot exceed the target. Please adjust your input.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        remaining_wickets = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # Input DataFrame
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [remaining_wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Model Prediction
        result = pipe.predict_proba(input_df)
        loss_prob = result[0][0]
        win_prob = result[0][1]

        # Display Results
        st.header(f"{batting_team} - {round(win_prob * 100)}%")
        st.header(f"{bowling_team} - {round(loss_prob * 100)}%")
