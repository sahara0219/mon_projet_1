import streamlit as st
import pandas as pd
import plotly.express as px









from datetime import datetime

 

start_time = st.slider(

    "When do you start?",

    value=datetime(2020, 1, 1, 9, 30),

    format="MM/DD/YY - hh:mm",

)

st.write("Start time:", start_time)


vehiculos = pd.read_csv("vehicles_us (1).csv") #lectura del archivo csv


 

hist_button = st.button('Construir histograma')
fig = px.histogram(vehiculos, x="model_year", nbins=20, title="Distribución de Años de los Vehiculos ")

st.plotly_chart(fig)

hist_button = st.button('Construir histograma')
fig_t = px.histogram(vehiculos, x="transmission", nbins=20, title="Distribución de Transmisiones ")

st.plotly_chart(fig_t)
 
hist_button = st.button('Construir histograma') 
fig_p = px.histogram(vehiculos, x="price", nbins=20, title="Distribución de Precios")

st.plotly_chart(fig_p)
 
vehiculos = vehiculos.dropna() #eliminacion de los valores nulos 
vehiculos.colums = vehiculos.columns.str.lower().str.replace(" ", "_") #cambio de nombre de las columnas

st.title("Analisis de Vehiculos en Estados Unidos (2019-2020)") #titulo de la aplicacion

st.sidebar.header("Opciones de visualizacion") #opcines de visualizacion
st.write("Eeste es un analisis de los vehiculos en Estados Unidos durante los años 2019 y 2020, donde se analiza el tipo de combustible, el tipo de vehiculo, la marca y el modelo de los vehiculos.") # descripcion de la aplicascion 

st.subheader("Datos de los vehiculos") #subtitulos de la aplicacion

st.dataframe(vehiculos) #visualizacion de los datos en un dataframe 
st.write("Tolal de vehiculos:", len(vehiculos)) #total de vehiculos 
st.write("Total de marcas:", vehiculos['model'].nunique()) # total de marcas 
st.write("Total de modelos:", vehiculos['model_year'].nunique()) #total de modelos 
st.write("Total de tipos de combustible:", vehiculos['fuel'].nunique()) #total de tipos de combustible
st.write("tipos de trasmision:", vehiculos['transmission'].nunique()) #total de tipos de trasmision