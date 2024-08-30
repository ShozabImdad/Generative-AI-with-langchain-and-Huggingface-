import streamlit as st 
import pandas as pd
import numpy as np


## Title of the application
st.title("Hello Streamlit")

## Displaying a simple text
st.write("This is a simple text.")

## Creating a simp,e dataframe
df = pd.DataFrame ({
    'Firts Column' : [1, 2, 3, 4],
    'Second Column' : [10, 20, 30, 40]
    })

## Displaying a dataframe
st.write("Here is the dataframe.")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns= ['a', 'b', 'c']
)
st.line_chart(chart_data)