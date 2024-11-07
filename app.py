import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from joblib import load

# Load the pre-trained model and encoders
best_model = load('best_weather_model.joblib') 
preprocessor=load('preprocessor.joblib')
label_encoder = load('label_encoder.joblib')

def test_model_prediction(model, input_data, preprocessor, label_encoder, feature_names):
    # Wrap input data in a DataFrame with feature names
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Transform the entire input data using the same preprocessor
    input_data_encoded = preprocessor.transform(input_df)
    
    # Predict and decode the weather type
    predicted_weather_encoded = model.predict(input_data_encoded)
    predicted_weather = label_encoder.inverse_transform(predicted_weather_encoded)

    return predicted_weather[0]

# Streamlit app definition
def main():
    st.title('Weather Type Prediction App')
    
    # Input fields
    st.header('Enter Weather Details')
    
    temperature = st.number_input('Temperature (°C)', min_value=-24.0, max_value=71.0, step=0.1)
    humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=110.0, step=0.1)
    wind_speed = st.number_input('Wind Speed (km/h)', min_value=0.0, max_value=30.0, step=0.1)
    precipitation = st.number_input('Precipitation(%)', min_value=0.0, max_value=110.0, step=0.1)
    cloud_cover = st.selectbox('Cloud Cover', ['partly cloudy', 'clear' ,'overcast' ,'cloudy'])
    pressure = st.number_input('Pressure (hPa)', min_value=900.0, max_value=1100.0, step=0.1)
    uv_index = st.number_input('UV Index', min_value = 0.0, max_value=13.0, step=0.1)
    season = st.selectbox('Season', ['Winter', 'Spring', 'Summer', 'Autumn'])
    visibility = st.number_input('Visibility (km)', min_value=0.0, max_value=15.0, step=0.1)
    location = st.selectbox('Location', ['inland', 'mountain' ,'coastal'])
    
    # Button to make prediction
    if st.button('Predict Weather Type'):

        # Prepare input data
        input_data = [
            temperature, humidity, wind_speed,precipitation, cloud_cover,
            pressure, uv_index, season, visibility, location
        ]

        feature_names = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Cloud Cover', 
                 'Atmospheric Pressure', 'UV Index', 'Season', 'Visibility (km)', 'Location']
        
        
        # Get prediction
        prediction = test_model_prediction(best_model, input_data,preprocessor,label_encoder,feature_names)
        
        # Display the prediction result
        st.write(f"Predicted Weather Type: {prediction}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
