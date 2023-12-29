import streamlit as st
from PIL import Image
import historico as analisis_historico
import equipos as analisis_por_equipo
import requests
import pandas as pd

# Función para cargar datos
@st.cache_data
def load_data(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.DataFrame(response.json())
        return data
    else:
        st.error("Error al cargar los datos")
        return pd.DataFrame()

data_url = 'http://127.0.0.1:8000/retrieve_data/'
data = load_data(data_url)

def main():
    st.sidebar.title("Navegación")

    # Menú para la navegación
    choice = st.sidebar.radio("Ir a", 
                              ["Portada", "Análisis por Temporada", "Análisis por Equipo"])

    # Renderizar la página seleccionada
    if choice == "Portada":
        show_portada()
    elif choice == "Análisis por Temporada":
        analisis_historico.show_analisis_historico(partidos=data)
    elif choice == "Análisis por Equipo":
        analisis_por_equipo.show_analisis_por_equipo(data=data)

def show_portada():
    # Mostrar el logo
    logo_path = 'data/logo.png'
    logo = Image.open(logo_path)
    st.image(logo, width=500)

    # Contenido de la página de portada
    st.title("Campeonato Nacional de Liga - Primera División")
    st.write("Bienvenido al Dashboard de Análisis de la Liga de Fútbol. ")
    st.title("Contenido")
    st.write("En la sección Análisis por temporada encontrarás diferentes datos de los equipos que parcitiparon en esa temporada: Clasifiación general, Tiros, Faltas, Tarjetas, Efectividad al puntuar y Análisis de casas de apuestas. En la sección de Análisis por Equipo encontrarás los datos históricos de aquellos equipos que disputaron la Primera División entre las temporadas 2005-2006 y 2023-2024.")
    st.title("Datos")
    st.write("Este dashboard muestra las estadísticas todos los partidos de Primera División desde la temporada 2005-2006 hasta el 23 de diciembre de 2023. Fuente: https://www.football-data.co.uk/")
if __name__ == "__main__":
    main()
