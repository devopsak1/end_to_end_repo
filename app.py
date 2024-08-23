import streamlit as st
import pandas as pd

data = {
    'Course Name': ['Devops', 'Azure', 'Snowflake', 'SQL', 'Hadoop'],
    'Course Duration': ['30 Day', '35 Day', '40 Day', '30 Day', '21 Day']
}

df = pd.DataFrame(data)
st.write('Course Details Table....')

st.dataframe(df)
