import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write("A simple app showing the various ways on how to use the st.write() command for displaying text, numbers, DataFrames and plots.")
# Example 1
st.header("st.write")

# Example 2
st.write("Hello, *WoRlD!* :sunglasses:")
# Example 3
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

# Example 4
st.write(df)
# Example 5
st.write('Below is a DataFrame: ', df, ' Above is a dataframe.')

df_random = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a','b','c']
    )

circle = alt.Chart(df_random).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(circle)