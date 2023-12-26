import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages import clasificacion

def load_data():
    data_path = 'data/liga.csv'
    partidos = pd.read_csv(data_path)
    return partidos

def show_analisis_historico():
    st.title("Análisis Histórico")
    # Cargar los datos
    partidos = load_data()
    temporada_seleccionada = st.selectbox("Selecciona una Temporada", options=partidos['Temporada'].unique())
    tabla = clasificacion.generar_clasificacion(partidos, temporada_seleccionada)
    # Muestro el head de tabla
    st.table(tabla.head())