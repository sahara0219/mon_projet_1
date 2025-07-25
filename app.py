import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 
import streamlit as st 

car_data = pd.read_csv('vehicles_us (1).csv',sep=',') # Se lee el archivo CSV con los datos de los vehiculos

st.title("Analisis de Vehiculos en Estados Unidos (2019-2020)") #titulo de la aplicacion

st.sidebar.header("Opciones de visualizacion") #opcines de visualizacion
st.write("Eeste es un analisis de los vehiculos en Estados Unidos durante los años 2019 y 2020, donde se analiza el tipo de combustible, el tipo de vehiculo, la marca y el modelo de los vehiculos.") # descripcion de la aplicascion 

st.subheader("Datos de los vehiculos") #subtitulos de la aplicacion

st.dataframe(car_data) #visualizacion de los datos en un dataframe 
st.write("Tolal de vehiculos:", len(car_data)) #total de vehiculos 
st.write("Total de marcas:", car_data['model'].nunique()) # total de marcas 
st.write("Total de modelos:", car_data['model_year'].nunique()) #total de modelos 
st.write("Total de tipos de combustible:", car_data['fuel'].nunique()) #total de tipos de combustible
st.write("tipos de trasmision:", car_data['transmission'].nunique()) #total de tipos de trasmision


if st.button('Construir histograma',key ='histograma'):
   st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
   fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])]) # Crear un histograma utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de histograma
   fig.update_layout(title_text='Distribución del Odómetro') # Opcional: Puedes añadir un título al gráfico si lo deseas

   st.plotly_chart(fig, use_container_width=True, key="histograma")()# Mostrar el gráfico Plotly

build_dis = st.checkbox('Construir grafico de dispersion', value=False)# checkbox para controlar la construccion del grafico de dispersion

if build_dis:
   st.write('creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de cohces')
   st.write('Este grafico muestra la relacion entre el odometro y el precio de los vehiculos')

   fig_2= go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')]) # Crear un scatter plot utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de scatter
   fig_2.update_layout(title_text='Relación entre Odómetro y Precio') # Opcional: Puedes añadir un título al gráfico si lo deseas
   st.plotly_chart(fig_2, use_container_width=True, key="grafico_dispersion")# Mostrar el gráfico Plotly
