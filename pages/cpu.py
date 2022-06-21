import streamlit as st

import pandas as pd
import plotly.express as px

st.markdown('#### CPU')
st.markdown('We compare Raw Performance on the i9-9900K vs i9-12900K')

st.image('image/img.png')

st.markdown('')
# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["i9-9900K", 1284, 12450, 8779, 5651], ["i9-12900K", 1997, 27472, 17595, 6946]],
    columns=["Product", "Cinebench R23", "Cinebench R23 (Multi-Core)", "Geekbench 5, 64bit (Multi-Core)",
             "Revit 2022.1.1"]
)

fig = px.bar(df, x="Product",
             y=["Cinebench R23", "Cinebench R23 (Multi-Core)", "Geekbench 5, 64bit (Multi-Core)", "Revit 2022.1.1"],
             barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)

st.markdown('#### Factory to consider')
st.markdown('- Pure Raw Speed')
st.markdown('#### Winner')
st.markdown('i9-12900K won 30% for Most Render')

st.markdown('#### Reference i9-12900K ')
st.markdown('''
RVT 2022 - Full_Standard set - 2022.06.01 @ 13.48.15 on DESKTOP-SIIA0ON.txt
RFO Benchmark v3.3 (build 09.05.2022)
RevitForum.org

All times are in seconds, lower is better.


Run on Revit 2022.1.1

__________________________________________________ _______________
Update
4.46 update previous version file

__________________________________________________ _______________
Model creation benchmark
3.64 opening and loading the custom template
8.09 creating the floors levels and grids
10.59 creating a group of walls and doors
16.02 modifying the group by adding a curtain wall
6.40 creating the exterior curtain wall
5.35 creating the sections
2.21 changing the curtain wall panel type
7.83 creating area plans
1.07 creating and applying view template
61.20 TOTAL

__________________________________________________ _______________
Export benchmark
34.67 export all views as PNGs at 300 dpi
29.35 export all views as DWFs
63.47 export all views as DWGs
29.53 print all views as vector *
54.43 print all views as raster *

Notes:
* Print Views tests require the 'Microsoft XPS Document Writer' printer be installed.

__________________________________________________ _______________
Render benchmark
69.46 render


TEST CONDITIONS:
__________________________________________________ _____
Mfr: ASUS
Model: System Product Name
OS: Microsoft Windows 10 Pro 64-bit (build 2009)

__________________________________________________ _____
CPU0: 12th Gen Intel(R) Core(TM) i9-12900K
Max Clock Speed: 3.2Ghz
Physical Processors: 16
Logical Processors: 24

Total Physical Memory: 64GB
BANK 0: 32GB @ 3200Mhz
BANK 0: 32GB @ 3200Mhz

__________________________________________________ _____
Graphics Card: NVIDIA GeForce RTX 3060
Graphics RAM: 3.9990234375GB
Driver version: 30.0.15.1259
Screen Resolution: 3840 x 2160 x bit @ 60Hz (max 120Hz)

DPI Scaling: 300%

__________________________________________________ _____
Drive Type: Local Disk (NTFS)
Drive Model: Seagate FireCuda 530 ZP1000GM30023

'''
            )

st.markdown('#### Reference 2- i9 - 9900k')
st.markdown('''

RVT 2022 - Full_Standard set - 2021.06.11 @ 07.40.13 on PRLXLT03.txt
RFO Benchmark v3.3 (build 09.05.2022)
RevitForum.org

All times are in seconds, lower is better.


Run on Revit 2022 FCS

__________________________________________________ _______________
Update
7.61 update previous version file

__________________________________________________ _______________
Model creation benchmark
5.15 opening and loading the custom template
14.78 creating the floors levels and grids
21.97 creating a group of walls and doors
34.75 modifying the group by adding a curtain wall
13.80 creating the exterior curtain wall
11.57 creating the sections
4.33 changing the curtain wall panel type
15.71 creating area plans
2.16 creating and applying view template
124.22 TOTAL

__________________________________________________ _______________
Export benchmark
56.33 export all views as PNGs at 300 dpi
54.18 export all views as DWFs
126.26 export all views as DWGs
64.51 print all views as vector *
88.60 print all views as raster *

Notes:
* Print Views tests require the 'Microsoft XPS Document Writer' printer be installed.

__________________________________________________ _______________
Render benchmark
56.51 render

__________________________________________________ _______________
Graphics - Standard View
5.82 activate View Styles view
0.49 change view to Wireframe
0.71 change view to Hidden
0.95 change view to Shaded
0.93 change view to Consistent Colors
4.87 change view to Realistic
0.91 refresh Wireframe Line view x10
3.15 refresh Hidden Line view x10
3.30 refresh Shaded view x10
3.17 refresh Consistent Colors view x10
2.67 refresh Realistic view x10''')
