
# **Weather Type Prediction**

## **Project Description**

This project aims to develop a machine learning model that can accurately predict the type of weather based on historical weather data and deploy a web application using Streamlit.

## **Objective**

To create a robust machine learning model capable of predicting weather types using historical weather data, providing valuable insights into weather patterns.

## **Dataset**

The dataset includes the following weather features:

- **Temperature** (Temperature in Celsius)
- **Humidity** (Humidity in percentage)
- **Wind Speed** (Wind Speed in kilometers per hour)
- **Precipitation (%)** (Precipitation in percentage)
- **Cloud Cover** (Partly cloudy, Clear , Overcast ,Cloudy)
- **Atmospheric Pressure** (Pressure in hpascals)
- **UV Index** (UV Index in the range 0-13)
- **Season** (Summer, Spring, Autumn, Winter)
- **Visibility (km)** (Visibility in kilometer)
- **Location** (Inland, Coastal, Mountain)
- **Weather type** (Categorical weather type)

## **Approach**

### **1. Data Preprocessing**
- Handle missing values and outliers.
- Normalize numerical features to ensure consistent scaling.

### **2. Feature Engineering**
- Encoding categorical features to enhance model performance, such as:
  - Cloud Cover
  - Location
  - Season

### **3. Model Selection**
- Experiment with various machine learning algorithms suitable for multi-class classification, including:
  - Logistic Regression
  - Decision Trees
  - Random Forests
  - Support Vector Machines (SVM)

### **4. Model Evaluation**
- Evaluate the performance of different models using metrics such as:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrices

### **5. Model Deployment**
- Deploy the best-performing model for real-time weather predictions.

## **Expected Outcomes**

- A robust machine learning model capable of accurately predicting weather types based on the provided features.
- Insights into the factors influencing weather patterns and their relative importance.
- Potential applications in fields such as agriculture, transportation, and tourism.
