import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Unicorn AI')
# st.write('Welcome to Unicorn AI :sunglasses:')
st.write('Welcome to Unicorn AI')

if st.button('Run Data Analysis'):
     st.write('Running Data Analysis')
else:
     st.write('Data Analysis')

# st.write(1234)

# Example 3

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })
#st.write(df)


# Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
