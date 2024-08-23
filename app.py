import streamlit as st
import pandas as pd

data = {
    'Course Name': ['Devops', 'Azure', 'Snowflake', 'SQL'],
    'Course Duration': ['30 Day', '35 Day', '40 Day', '30 Day']
}

df = pd.DataFrame(data)

st.dataframe(df)
