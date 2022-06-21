import streamlit as st

import pandas as pd
import plotly.express as px

st.markdown('#### Motherboard')
st.markdown('Chipset')
st.markdown('Since old system Motherboard is UNKOWN')
st.markdown('We compare the difference on the Z590 vs Z690')

st.image('https://www.xtremegaminerd.com/wp-content/uploads/2021/09/Z590-vs-Z690-diagram.jpg')

st.markdown('')
# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["Z590", 16, 320, 10], ["Z690", 32, 480, 100]],
    columns=["Product", "Data Bandwidth GT/s", "Ram Speed", "Network Speed"]
)

fig = px.bar(df, x="Product", y=["Data Bandwidth GT/s", "Ram Speed", "Network Speed"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)

st.markdown('#### Factory to consider')
st.markdown('- Thermal and Size')
st.markdown('#### Winner')
st.markdown('Gigabyte Z690-AERO-D-rev-1x')
st.markdown(
    'AERO Series motherboards are a fresh approach to creators that evolve with optimized features for content creation. To deliver reliable computing performance, impressive connectivity, expandable graphics, and ultra-fast storage for creators to deal with heavy design workloads like 3D rendering and feature-length video production.')
st.markdown('#### Thermal Technology ')
st.markdown(
    'An effective cooling solution can prevent the risk of design work being interrupted by an unexpected system crash. GIGABYTE’s advanced thermal solutions provide a perfect balance of aesthetics and performance. A large heat sink design and Direct-Touch Heatpipe II ensure stability during creative sessions.')
st.markdown('Note: It comes with NVME SSD Heatsink to ensure the SSD dont get too hot')
