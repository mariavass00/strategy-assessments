# Libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 

import plotly.express as px
import pandas as pd

categories = ['Rolling Resistance','Comfort','Noise',
           'Wear', 'Traction','Handling']
fig = go.Figure()

#product 1
fig.add_trace(go.Scatterpolar(
      r=[105, 100, 100, 110, 95, 100],
      theta=categories,
      fill='toself',
      name='Product A'
))

#product 2
fig.add_trace(go.Scatterpolar(
      r=[95, 100, 100, 100, 105, 100],
      theta=categories,
      fill='toself',
      name='Product B'
))

#product 3
fig.add_trace(go.Scatterpolar(
      r=[100, 100, 95, 100, 100, 110],
      theta=categories,
      fill='toself',
      name='Product B'
))

#customization of chart
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[90, 115]
    )),
  showlegend=False
)


fig.show()

