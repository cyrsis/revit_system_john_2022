import streamlit as st

import pandas as pd
import plotly.express as px

st.markdown('#### Graphic Card')
st.markdown('Nvidia Base')
st.markdown('NVIDIA Quadro RTX4000 vs RTX3080')

st.markdown('')
# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["RTX 4000", 52, 15, 94], ["RTX 3080", 91, 27, 235]],
    columns=["Product", "Overall Score", "PassMark", "CUDA"]
)

fig = px.bar(df, x="Product", y=["Overall Score", "PassMark", "CUDA"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)

st.markdown('#### Factory to consider')
st.markdown('- Price and Performance')
st.markdown('#### Winner')
st.markdown('Zotac RTX 3080 TI')
st.markdown(
    '3080 Series is almost double the speed compare to Quadro RTX 4000')

st.markdown('100% work with Revit 2019')
st.markdown('Driver can be Studio (Render) and Gaming')

st.image('https://static.userbenchmark.com/resources/static/gpu/Nvidia-RTX-3080.jpg')
