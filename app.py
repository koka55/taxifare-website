import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown("WELCOME , RIDE SERVICE IS AVAILABLE ...")

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

# Input fields for user parameters
st.header("Fill Your ride details:")

# Date and time input
ride_datetime = st.date_input("Date", value=None)
ride_time = st.time_input("Time", value=None)

# Pickup and Dropoff Locations
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")

# Passenger count input
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



# 2. Let's build a dictionary containing the parameters for our API...
# Button to make prediction
if st.button("Get Prediction"):
    # Prepare the parameters for the API call
    params = {
        "pickup_datetime": f"{ride_datetime} {ride_time}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }


    # 3. Let's call our API using the `requests` package...
    url = 'https://taxifare-1055024044844.europe-west1.run.app/predict'
    response = requests.get(url, params=params)


    # 4. Let's retrieve the prediction from the **JSON** returned by the API...

    if response.status_code == 200:
        # Retrieve the prediction from the JSON response
        prediction = response.json().get('prediction')

        if prediction is not None:
            st.success(f"The predicted fare is: ${prediction:.2f}")
        else:
            st.error("No prediction received. Please check your parameters.")
    else:
        st.error("Error retrieving prediction. Please check your parameters.")

## Finally, we can display the prediction to the user
