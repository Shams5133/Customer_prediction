import streamlit as st
import pickle
import pandas as pd
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
job_list = {"blue-collar":1,"entrepreneur":2, "housemaid":3, "services":4,"technician":5, "self-employed":6,
                            "admin.": 7, "management": 8, "unemployed":9, "retired":10, "student":11}
education_list = {'primary':1,"secondary":2,"tertiary":3}
month_list = {"may":1,"jul":2,"jan":3,"nov":4,"jun":5,"aug":6,"feb":7,"apr":8,"oct":9,"sep":10,"dec":11,"mar":12}
st.write("Insurance customer converstion prediction")
age = st.sidebar.selectbox(options = range(1,100),label = "select age")
if age > 70:
    age = 70
job_option = st.sidebar.selectbox(options = job_list, label = "select job")
job = job_list[job_option]
education_option = st.sidebar.selectbox(options = education_list, label = "select educational qualification")
education_qual = education_list[education_option]
day = st.sidebar.selectbox(options = range(1,32),label = "select day")
month_option = st.sidebar.selectbox(options = month_list, label = "select month")
month = month_list[month_option]
dur = st.sidebar.number_input(min_value = 1, label = "enter duration of call")
if dur > 640:
  dur = 640
dur = dur//30
num_calls = st.sidebar.number_input(min_value = 1, label = "enter number of calls")
if num_calls > 6:
  num_calls = 6
marital_option = st.sidebar.selectbox(options = ['single','married','divorced'], label = "select marital status")
if marital_option == 'single':
  marital_single = 1
  marital_divorced = 0
  marital_married = 0
elif marital_option == 'married':
  marital_single = 0
  marital_divorced = 0
  marital_married = 1
elif marital_option == 'divorced':
  marital_single = 0
  marital_divorced = 1
  marital_married = 0
call_type_option = st.sidebar.selectbox(options = ['cellular','telephone','unknown'], label = "select call type")
if call_type_option == 'cellular':
  call_type_cellular = 1
  call_type_telephone = 0
  call_type_unknown = 0
elif call_type_option == 'unknown':
  call_type_cellular = 0
  call_type_telephone = 0
  call_type_unknown = 1
elif call_type_option == 'telephone':
  call_type_cellular = 0
  call_type_telephone = 1
  call_type_unknown = 0
prev_outcome_option = st.sidebar.selectbox(options = ['success','failure','unknown','other'], label = "select previous call outcome")
if prev_outcome_option == 'success':
  prev_outcome_success = 1
  prev_outcome_unknown = 0
  prev_outcome_other = 0
  prev_outcome_failure = 0
elif prev_outcome_option == 'failure':
  prev_outcome_success = 0
  prev_outcome_unknown = 0
  prev_outcome_other = 0
  prev_outcome_failure = 1
elif prev_outcome_option == 'other':
  prev_outcome_success = 0
  prev_outcome_unknown = 0
  prev_outcome_other = 1
  prev_outcome_failure = 0
elif prev_outcome_option == 'unknown':
  prev_outcome_success = 0
  prev_outcome_unknown = 1
  prev_outcome_other = 0
  prev_outcome_failure = 0

X_input = [age,job,education_qual, day, month, dur, num_calls , marital_divorced, marital_married, marital_single, call_type_cellular,  call_type_telephone,  call_type_unknown,
          prev_outcome_failure, prev_outcome_other, prev_outcome_success, prev_outcome_unknown ]
X_df = pd.DataFrame( columns =['age','job','education_qual', 'day', 'mon', 'dur', 'num_calls' , 'marital_divorced', 'marital_married', 'marital_single', 'call_type_cellular',  'call_type_telephone',  'call_type_unknown',
          'prev_outcome_failure', 'prev_outcome_other', 'prev_outcome_success', 'prev_outcome_unknown'] )
if st.sidebar.button('predict'):
  X_df.loc[0] = X_input
  X_scaled = scaler.transform(X_df)
  y = model.predict(X_scaled)
  if y == 1:
    st.write("Customer is predicted to buy the insurance")
  elif y ==0:
    st.write("Customer is predicted to not buy the insurance")

