import streamlit as st

from datetime import datetime

 

start_time = st.slider(

    "When do you start?",

    value=datetime(2020, 1, 1, 9, 30),

    format="MM/DD/YY - hh:mm",

)

st.write("Start time:", start_time)

import pandas as pd
vehiculos = pd.read_csv("vehicles_us (1).csv") 
st.title("vehiculos en estados unidos")
st.dataframe(veiculos)
