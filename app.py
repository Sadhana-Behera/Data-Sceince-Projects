import streamlit as st
import pickle
import numpy as np
rf = pickle.load(open('rf_model_car_price_09nov.pkl','rb'))

st.title('CAR Selling Price prediction Web App')
st.subheader('Fill the below Details to predict Insurance Charges')
col1,col2=st.columns(2)
year = col1.slider('Year of Purchase',1992,2023)
km_driven = col1.slider('Kilometer Driven',1,900000)
owner = col1.selectbox('Owner',['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])
transmission = col2.selectbox('Transmission',['Manual','Automatic'])
seller_type = col2.selectbox('Seller Type',['Individual','Dealer','Trustmark Dealer'])
fuel = col2.selectbox('Fuel',['Diesel','Petrol','CNG','LPG','Electric'])

if st.button('Predict Selling Price'):
    if owner=='First Owner':
        owner = 0
    elif owner=='Second Owner':
        owner = 2
    elif owner=='Third Owner':
        owner = 4
    elif owner=='Fourth & Above Owner':
        owner = 1
    else:
        owner = 3
    if transmission=='Manual':
        transmission = 1
    else:
        transmission = 0
    if seller_type=='Individual':
        seller_type = 1
    elif seller_type=='Dealer':
        seller_type = 0
    else:
        seller_type = 2
    if fuel=='Diesel':
        fuel = 1
    elif fuel=='Petrol':
        fuel = 4
    elif fuel=='CNG':
        fuel = 0
    elif fuel=='LPG':
        fuel = 3
    else:
        fuel = 2

    test = np.array([year,km_driven,owner,transmission,seller_type,fuel])
    test = test.reshape(1,6)
    st.success(rf.predict(test)[0])

# To run Streamlit Web App
# streamlit run app.py

