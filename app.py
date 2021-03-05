import streamlit as st
import datetime
import requests
import json

st.title("NY TAXI")

container = st.beta_container()
col1, col2, col3 = st.beta_columns(3)

with col1:
    d = st.date_input('Select a date: ', datetime.datetime.now())
    st.write('When ?', d)

    pass_cnt = st.number_input('Select passenger count', value=0)
    st.write('Passenger Count: ', pass_cnt)

with col2:
    pick_long = st.number_input('Select pickup longitude')
    st.write('Pickup Longitude: ', pick_long)

    pick_lat = st.number_input('Select pickup latitude')
    st.write('Pickup Latitude: ', pick_lat)

with col3:
    drop_long = st.number_input('Select dropoff longitude')
    st.write('Dropoff Longitude: ', drop_long)

    drop_lat = st.number_input('Select dropoff latitude')
    st.write('Dropoff Latitude: ', drop_lat)

url = 'https://docker-image-tst-hroqn6xmnq-ew.a.run.app/predict_fare/'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

if st.button('Predict'):
    # print is visible in server output, not in the page
    
    if pick_long == 0 or pick_lat == 0 or drop_long == 0 or drop_lat == 0 or pass_cnt == 0:
        st.error('Please fill all the fields !')
    else:
        date = f'{d} 00:00:00 UTC'
        params = {"key":date, "pickup_datetime":date, "pickup_latitude":pick_lat,\
                    "pickup_longitude":pick_long, "dropoff_latitude":drop_lat, \
                        "dropoff_longitude":drop_long, "passenger_count":pass_cnt }
    
        # params = {
        #                 "dropoff_latitude":40.74383544921875,
        #                 "dropoff_longitude":-73.98143005371094,
        #                 "key":"2015-01-27 13:08:24.0000002",
        #                 "passenger_count":1,
        #                 "pickup_datetime":"2015-01-27 13:08:24 UTC",
        #                 "pickup_latitude":40.7638053894043,
        #                 "pickup_longitude":-73.97332000732422}
        
        response = requests.get(url, params = params)
        status_code = response.status_code
        if status_code >= 400:
            st.error(f'An error occured ! {response.text}')
        else:
            resp = response.json()
            pred = resp['prediction']
            
            st.success(f'Prediction: {pred}')
