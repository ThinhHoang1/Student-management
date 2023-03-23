import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
path_to_file = 'house-prices.csv'

@st.cache_data()
def load_data():
    df = pd.read_csv(path_to_file)
    df.replace({'Yes': 1, 'No': 0}, inplace=True)
    df.replace({'East': 2, 'North': 1, 'West': 0}, inplace=True)
    return df

df = load_data()

# Create the Streamlit app
def main():
    st.title('House Prices Prediction')
    st.write('Welcome to the House Prices Prediction app!')
    st.write('Please select the type of model you want to use:')

    # Create radio buttons for user to select model
    model_type = st.radio('', ['Simple Linear Regression', 'Multiple Linear Regression'])

    # Split the data into train and test sets
    y = df['Price']
    if model_type == 'Simple Linear Regression':
        X = df[['SqFt']]
    else:
        X = df[['SqFt', 'Bedrooms', 'Bathrooms', 'Offers', 'Brick', 'Neighborhood']]
    SEED = 42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

    # Train the model
    if model_type == 'Simple Linear Regression':
        regressor = linear_model.LinearRegression()
        regressor.fit(X_train, y_train)
    else:
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        regressor = linear_model.LinearRegression()
        regressor.fit(X_train_scaled, y_train)

    # Create input widgets for user input
    sqft = st.slider('Square footage', 500, 5000, 1000)
    if model_type == 'Multiple Linear Regression':
        bedrooms = st.selectbox('Number of bedrooms', [1, 2, 3, 4, 5])
        bathrooms = st.selectbox('Number of bathrooms', [1, 2, 3, 4])
        offers = st.slider('Number of offers', 1, 10, 1)
        brick = st.selectbox('Is the house made of brick?', ['Yes', 'No'])
        neighborhood = st.selectbox('Neighborhood', ['East', 'North', 'West'])

        # Convert categorical variables to numerical
        if brick == 'Yes':
            brick = 1
        else:
            brick = 0

        if neighborhood == 'East':
            neighborhood = 2
        elif neighborhood == 'North':
            neighborhood = 1
        else:
            neighborhood = 0

    # Make a prediction and display the result
    if st.button('Predict'):
        if model_type == 'Simple Linear Regression':
            X = np.array(sqft).reshape(1, -1)
        else:
            X = np.array([sqft, bedrooms, bathrooms, offers, brick, neighborhood]).reshape(1, -1)
            X = scaler.transform(X)
        prediction = regressor.predict(X)
        st.write('The predicted house price is: $', round(prediction[0], 2))

    if st.checkbox('View the dataset'):
        st.write(df)
if __name__ == '__main__':
    main()
   
