import streamlit as st
import pandas as pd
import requests

@st.cache
def load_data(url: str):
    r = requests.get(url)
    mijson = r.json()
    listado = mijson['partidos']
    partidos = pd.DataFrame.from_records(listado)
    return partidos

# URL del archivo CSV, ajusta según sea necesario
url_csv = 'http://localhost:8000/retrieve_data/'
partidos = load_data(url_csv)

# Métodos para comprobar y quitar valores vacíos, según sea necesario
def compruebavacios(dataframe):
    valores_vacios = [column_name for column_name in dataframe.columns if dataframe[column_name].isna().any()]
    if not valores_vacios:
        print("No hay valores vacíos en este DataFrame")
    else:
        print("Las columnas con valores vacíos son:")
        for i in valores_vacios:
            print(i)

def quitavacios(dataframe):
    dataframe.dropna(axis=1, how='all', inplace=True)

# Comprueba y quita valores vacíos
compruebavacios(partidos)
quitavacios(partidos)

# Título de la aplicación Streamlit
st.title('Campeonato Nacional de Liga de Primera División')

# Selector de equipo
equipo_seleccionado = st.selectbox('Selecciona un equipo:', partidos['HomeTeam'].unique())

# Filtra los partidos según el equipo seleccionado
partidos_filtrados = partidos[partidos['HomeTeam'] == equipo_seleccionado]

# Muestra el DataFrame filtrado
st.dataframe(partidos_filtrados)