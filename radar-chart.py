import streamlit as st
import random
import plotly.express as px
import pandas as pd

def radar_chart(val):  
    df = pd.DataFrame(dict(
    r=[random.randint(0,val),
       random.randint(0,val),
       random.randint(0,val),
       random.randint(0,val),
       random.randint(0,val)],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.write(fig)

if __name__ == '__main__':
    val = st.slider('Select value',0,10,1)
    radar_chart(val)
