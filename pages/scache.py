import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title("Cache")

# Using cache

start = time()

st.subheader("Using st.cache")


@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
end = time()

st.info(end-start)


# Not using cache
start_no_cache = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
end_no_cache = time()
st.info(end_no_cache-start_no_cache)