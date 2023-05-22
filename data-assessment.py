import numpy as np
import plotly.express as px
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import time

st.title("Animation Time Trial")
mode = st.selectbox("Select Plotting Library",('Plotly','Altair','Matplotlib'))
FPS = st.slider('Attempted FPS',0,120,30)
numPoints = st.slider('Number of Plot Points',1,5000,5)
animTime = st.slider('Time to Animate',1,10,1)

#Data
X = np.random.rand(numPoints)
Y = np.random.rand(numPoints)
data = pd.DataFrame({"x":X,"y":Y})

extraTime = 0

if st.button("Animate"):

    if mode == "Plotly":
     
      df = pd.DataFrame(dict(
             r=[1, 5, 2, 2, 3],
        theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.show()  

    if mode == "Altair":
        fig1 = alt.Chart(data).mark_point().encode(x="x",y="y")
        drawn_fig1 = st.altair_chart(fig1,use_container_width = True)
        for i in range(FPS*animTime):
            frameStartTime = time.time()
            X = X +1.0/FPS
            Y = Y +1.0/FPS
            data = pd.DataFrame({"x":X,"y":Y})
            frameDrawTime = time.time()
            fig1 = alt.Chart(data).mark_point().encode(x="x",y="y")
            drawn_fig1.altair_chart(fig1,use_container_width = True)
            frameEndTime = time.time()
            try:
                time.sleep(1/FPS-(frameEndTime-frameStartTime))
            except:
                time.sleep(1/FPS)

    if mode == "Matplotlib":
        st.set_option('deprecation.showPyplotGlobalUse', False)
        fig1 = plt.scatter(X,Y)
        drawn_fig1 = st.pyplot()
        for i in range(FPS*animTime):
            frameStartTime = time.time()
            X = X +1.0/FPS
            Y = Y +1.0/FPS
            data = pd.DataFrame({"x":X,"y":Y})
            frameDrawTime = time.time()
            fig1 = plt.scatter(X,Y)
            drawn_fig1.pyplot()
            frameEndTime = time.time()
            try:
                time.sleep(1/FPS-(frameEndTime-frameStartTime))
            except:
                time.sleep(1/FPS)
