import streamlit as st

import pandas as pd
import plotly.express as px

st.markdown('#### Overall System')
st.markdown('The suggest model carry almost double in performance and fit the price constraint')
st.markdown('The System were design for couple years run in 24/7')

st.markdown('---')
st.markdown('##### Base Model')
st.markdown('''
| Item         |                       Specs                       |
|--------------|:-------------------------------------------------:|
| CPU          |              Intel® CoreTM i9 9900k               |
| Memory       |            32GB RAM DDR4 2666+ or more            |
| Display Card |          NVIDIA Quadro RTX4000 or faster          |
| Hard Drive   |      500+GB SSD & Min. 2TB 7200+RPM storage       |
| Network      | Gigabit Ethernet Adapter with internet connection |

''')
st.markdown('---')
st.markdown('##### Suggest System')

st.markdown('''
| Item         |                       Specs                       |
|--------------|:-------------------------------------------------:|
| CPU          |              Intel® CoreTM i9 12900k               |
| Memory       |            64GB RAM DDR5 5200            |
| Display Card |          NVIDIA RTX 3080TI          |
| Hard Drive   |      Samsung M.2 980 Pro 1 TB x 3       |
| Network      | 10 Gigabit Ethernet Adapter            |

''')

st.markdown('---')
st.markdown('### More')
st.markdown('#### Water Cooling -NZXT  Kraken X73')
st.image(
    'https://nzxt.com/assets/cms/34299/1615585055-kraken-x73frontbnwith-fanpurple.png?dpr=2&fit=crop&fm=webp&h=1000&w=1000')

st.markdown('#### Case - Fractal Define 7 XL with Top Water Cooler Mount & Cable Management')
st.image(
    'https://www.fractal-design.com/wp-content/uploads/2020/10/Define_7_Sheetmetal_Black_Vented_Top_wo_sidepanel_XL_Left_Front_Above-1080x1080.jpg')
