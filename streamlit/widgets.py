import streamlit as st 
import pandas as pd


## Create Title
st.title("Treamlit Text Input")

name = st.text_input("Enter your Name: ")
st.write(f'Hello, {name}')

## creating slider
age  = st.slider("Select Your Age: ", 0, 100, 25)
st.write(f'Your age is: {age}.')

## creating slectbox/dropdown box
options = ['python', 'java', '.Net', 'c++', 'Kotlin']
choice = st.selectbox('Select Your Programming Language: ', options)
st.write(f"You Selected, {choice}")

## Creating and Displaying a Dataframe
data = {
    'Name': ['Ali', 'Aurrad', 'Imdad', 'Fazal'],
    'Age':['18', '20', '23', '55'],
    'City': ['Lahore', 'Mian Channu', 'Islamabad', 'Multan']
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv')
st.write(df)

## adding upload button to upload a file 
uploaded_file = st.file_uploader('Please enter the csv file: ', type = 'csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)



