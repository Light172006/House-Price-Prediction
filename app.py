import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(page_title= 'House Price Prediction',page_icon='🏠')

st.title('House Price Predictor')

if 'bedroom' not in st.session_state:
    st.session_state.bedroom = 0
if 'bathroom' not in st.session_state:
    st.session_state.bathroom = 0
if 'balcony' not in st.session_state:
    st.session_state.balcony = 0  
if 'car_parking' not in st.session_state:
    st.session_state.car_parking = 0  
if 'location' not in st.session_state:
    st.session_state.loaction = ''
if 'furnishing' not in st.session_state:
    st.session_state.furnishing = ''
if 'area' not in st.session_state:
    st.session_state.area = 0
if 'C_Lv' not in st.session_state:
    st.session_state.C_Lv = 0
if 'T_Lv' not in st.session_state:
    st.session_state.T_Lv = 0

st.write('### LOCATION:')
st.selectbox('Enter Your Loaction',['thane', 'navi-mumbai', 'nagpur', 'mumbai', 'ahmedabad',
       'bangalore', 'chennai', 'gurgaon', 'hyderabad', 'indore', 'jaipur',
       'kolkata', 'lucknow', 'new-delhi', 'noida', 'pune', 'agra', 'allahabad', 'aurangabad', 'badlapur', 'bhiwadi',
       'bhiwandi', 'bhubaneswar', 'chandigarh', 'coimbatore', 'dehradun',
       'durgapur', 'ernakulam', 'faridabad', 'ghaziabad', 'goa',
       'greater-noida', 'guntur', 'guwahati', 'gwalior', 'haridwar',
       'jabalpur', 'jamshedpur', 'kalyan', 'kanpur', 'kochi', 'mangalore',
       'mohali', 'mysore', 'nashik', 'palghar', 'panchkula', 'patna',
       'raipur', 'rajahmundry', 'ranchi', 'siliguri', 'sonipat', 'surat',
       'thrissur', 'tirupati', 'trichy', 'trivandrum', 'vadodara', 'vapi',
       'varanasi', 'vijayawada', 'visakhapatnam', 'zirakpur',
       'Others'],key='location')

st.write('### BEDROOM:')
st.slider('Enter the number of bedroom',0,10,key='bedroom')

st.write('### BATHROOM:')
st.slider('Enter the number of bathroom',0,10,key='bathroom')

st.write('### BALCONY:')
st.slider('Enter the number of balcony',0,10,key='balcony')

st.write('### CAR PARKING:')
st.slider('Enter the number of car parking',0,10,key='car_parking')

st.write('### TOTAL FLOOR:')
st.slider('Enter the total number floor',1,50,key='T_Lv')

st.write('### FLOOR:')
st.slider('Enter the floor number',0,st.session_state.T_Lv,key='C_Lv')

st.write('### FURNISHING:')
st.selectbox('Enter the furnishing condition',['Furnished','Semi-Furnished','Unfurnished'],key='furnishing')

st.write('### AREA:')
st.number_input('Enter the area in sqft',key='area')

model = joblib.load(r"D:\\ML Projects\\House Price Prediction\\House_Price_Prediction.pkl")
feature_name = joblib.load(r"D:\\ML Projects\\House Price Prediction\\Feature_Name.json")

Data = dict()
for i in feature_name:
    Data[i] = 0

Data = pd.DataFrame(Data,index=['0'])

Data['Bathroom'] = st.session_state.bathroom
Data['Balcony'] = st.session_state.balcony
Data['Car Parking'] = st.session_state.car_parking
Data['BHK'] = st.session_state.bedroom
Data['Area'] = st.session_state.area
Data[st.session_state.furnishing] = 1
Data[st.session_state.location] = 1
Data['Floor'] = st.session_state.C_Lv / st.session_state.T_Lv

if 'estimate' not in st.session_state:
    st.session_state.estimate = 0

def predict():
    st.session_state.estimate =  model.predict(Data)

if st.button('ESTIMATE',icon='💸',on_click=predict()):
    st.write(f'Estimated Price : ₹{round(float(st.session_state.estimate),2)} Lakh')