import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['partidos']
    df = pd.DataFrame.from_records(listado)
    return df
    
data = load_data('http://fastapi:8000/retrieve_data/')
    
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

def calcular_estadisticas_equipo(partidos, equipo):
    # Filtrar partidos para el equipo seleccionado
    datos_equipo_local = partidos[(partidos['HomeTeam'] == equipo)]
    datos_equipo_visitante = partidos[(partidos['AwayTeam'] == equipo)]

    # Agrupar por temporada y calcular estadísticas
    goles_marcados_local = datos_equipo_local.groupby('Temporada')['FTHG'].sum()
    goles_marcados_visitante = datos_equipo_visitante.groupby('Temporada')['FTAG'].sum()
    goles_marcados = goles_marcados_local + goles_marcados_visitante
    goles_recibidos_local = datos_equipo_local.groupby('Temporada')['FTAG'].sum()
    goles_recibidos_visitante = datos_equipo_visitante.groupby('Temporada')['FTHG'].sum()
    goles_recibidos = goles_recibidos_local + goles_recibidos_visitante

    return goles_marcados, goles_recibidos

def calcular_puntos_por_temporada(partidos, equipo):
    # Filtrar partidos para el equipo seleccionado
    datos_equipo = partidos[(partidos['HomeTeam'] == equipo) | (partidos['AwayTeam'] == equipo)]

    # Calcular puntos por temporada
    datos_equipo['Puntos'] = datos_equipo.apply(lambda row: 3 if (row['HomeTeam'] == equipo and row['FTR'] == 'H') or 
                                                (row['AwayTeam'] == equipo and row['FTR'] == 'A') else
                                                (1 if row['FTR'] == 'D' else 0), axis=1)
    puntos_por_temporada = datos_equipo.groupby('Temporada')['Puntos'].sum()

    return puntos_por_temporada

def show_analisis_por_equipo(data, equipo_seleccionado):
    st.title("Análisis por Equipos")
    mostrar_estadisticas_equipo(data, equipo_seleccionado)

    # Obtener estadísticas para el equipo seleccionado
    goles_marcados, goles_recibidos = calcular_estadisticas_equipo(data, equipo_seleccionado)

    # Preparar datos para el gráfico de barras
    df_estadisticas = pd.DataFrame({'Goles Marcados': goles_marcados, 'Goles Recibidos': goles_recibidos})

    # Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    df_estadisticas.plot(kind='bar')
    plt.title(f"Rendimiento de {equipo_seleccionado} a lo largo de las Temporadas")
    plt.xlabel("Temporada")
    plt.ylabel("Goles")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Calcular puntos por temporada para el equipo seleccionado
    puntos_por_temporada = calcular_puntos_por_temporada(data, equipo_seleccionado)

    # Crear un gráfico de barras para visualizar los puntos por temporada
    plt.figure(figsize=(10, 6))
    puntos_por_temporada.plot(kind='bar')
    plt.title(f"Puntos Obtenidos por Temporada - {equipo_seleccionado}")
    plt.xlabel("Temporada")
    plt.ylabel("Puntos")
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Crear una interfaz de usuario con Streamlit
equipos = data['HomeTeam'].unique()
equipo_seleccionado = st.selectbox("Selecciona un Equipo", options=equipos)
show_analisis_por_equipo(data=data, equipo_seleccionado=equipo_seleccionado)
