import streamlit as st
import pickle
import pandas as pd

teams = ['Rajasthan Royals', 'Royal Challengers Bangalore',
       'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
       'Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders',
       'Punjab Kings', 'Mumbai Indians']

City = ['Delhi', 'Bengaluru', 'Indore', 'Bangalore', 'Jaipur', 'Durban',
       'Chandigarh', 'Ahmedabad', 'Hyderabad', 'Mumbai', 'Pune',
       'Chennai', 'Kolkata', 'Dubai', 'Abu Dhabi', 'Navi Mumbai',
       'Port Elizabeth', 'Cape Town', 'Dharamsala', 'Sharjah',
       'East London', 'Johannesburg', 'Cuttack', 'Visakhapatnam',
       'Raipur', 'Centurion', 'Bloemfontein', 'Ranchi', 'Kimberley']
pipe = pickle.load(open("pipe.pkl","rb"))
st.title("Win Predictor")

col1,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("select batting team",teams)
with col2:
    bowling_team = st.selectbox("select bowling team",teams )
select_city = st.selectbox("select city",City)
target = st.number_input("target")

col1,col2,col3 = st.columns(3)
with col1:
    score = st.number_input("score")
with col2:
    overs = st.number_input("overs finished")
with col3:
    wickets = st.number_input("wickets fallen")
if st.button("predict"):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({'BattingTeam':[batting_team],'BowlingTeam':[bowling_team],'City':[select_city],'runs_needed':[runs_left],'balls_left':[balls_left],'wick_in_hand':[wickets],'total_run':[target],'crr':[crr],'rr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")

