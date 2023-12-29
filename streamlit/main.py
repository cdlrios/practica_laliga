import streamlit as st
from PIL import Image
import requests
import pandas as pd


logo_path = './logo.png'
logo = Image.open(logo_path)

st.image(logo, width=500)
st.sidebar.success("Selecciona una sección")
st.title("Campeonato Nacional de Liga - Primera División")
st.write("Bienvenido al Dashboard de Análisis de la Liga de Fútbol. ")
st.title("Contenido")
st.write("En la sección Análisis por temporada encontrarás diferentes datos de los equipos que parcitiparon en esa temporada: Clasifiación general, Tiros, Faltas, Tarjetas, Efectividad al puntuar y Análisis de casas de apuestas. En la sección de Análisis por Equipo encontrarás los datos históricos de aquellos equipos que disputaron la Primera División entre las temporadas 2005-2006 y 2023-2024.")
st.title("Datos")
st.write("Este dashboard muestra las estadísticas todos los partidos de Primera División desde la temporada 2005-2006 hasta el 23 de diciembre de 2023. Fuente: https://www.football-data.co.uk/")

