import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data_path = 'data/liga.csv' 
    data = pd.read_csv(data_path)
    return data

def mostrar_estadisticas_equipo(data, equipo):
    # Filtrar datos para el equipo seleccionado
    datos_equipo = data[(data['HomeTeam'] == equipo) | (data['AwayTeam'] == equipo)]

    # Partidos jugados
    partidos_jugados = len(datos_equipo)
    st.write(f"Total de Partidos Jugados: {partidos_jugados}")

    # Victorias, empates y derrotas
    victorias = len(datos_equipo[(datos_equipo['FTR'] == 'H') & (datos_equipo['HomeTeam'] == equipo)] + 
                  datos_equipo[(datos_equipo['FTR'] == 'A') & (datos_equipo['AwayTeam'] == equipo)])
    empates = len(datos_equipo[datos_equipo['FTR'] == 'D'])
    derrotas = partidos_jugados - victorias - empates

    st.write(f"Victorias: {victorias}, Empates: {empates}, Derrotas: {derrotas}")

    # Goles marcados y recibidos
    goles_marcados = datos_equipo[datos_equipo['HomeTeam'] == equipo]['FTHG'].sum() + datos_equipo[datos_equipo['AwayTeam'] == equipo]['FTAG'].sum()
    goles_recibidos = datos_equipo[datos_equipo['HomeTeam'] == equipo]['FTAG'].sum() + datos_equipo[datos_equipo['AwayTeam'] == equipo]['FTHG'].sum()

    st.write(f"Goles Marcados: {goles_marcados}, Goles Recibidos: {goles_recibidos}")


def show_analisis_por_equipo():
    st.title("Análisis por Equipos")

    data = load_data()
    equipo_seleccionado = st.selectbox("Selecciona un Equipo", options=data['HomeTeam'].unique())
    mostrar_estadisticas_equipo(data, equipo_seleccionado)
