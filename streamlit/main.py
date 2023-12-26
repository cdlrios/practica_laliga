import streamlit as st
from PIL import Image
# Importar módulos de las páginas
from pages import historico as analisis_historico
from pages import equipos as analisis_por_equipo

def main():
    st.sidebar.title("Navegación")

    # Menú para la navegación
    choice = st.sidebar.radio("Ir a", 
                              ["Portada", "Análisis Histórico", "Análisis por Equipo"])

    # Renderizar la página seleccionada
    if choice == "Portada":
        show_portada()
    elif choice == "Análisis Histórico":
        analisis_historico.show_analisis_historico()
    elif choice == "Análisis por Equipo":
        analisis_por_equipo.show_analisis_por_equipo()

def show_portada():
    # Mostrar el logo
    logo_path = 'data/logo.png'  # Ajusta la ruta según sea necesario
    logo = Image.open(logo_path)
    st.image(logo, width=500)

    # Contenido de la página de portada
    st.title("Campeonato Nacional de Liga - Primera División")
    st.write("Bienvenido al Dashboard de Análisis de la Liga de Fútbol. Selecciona una opción del menú para explorar los análisis históricos y por equipo.")

if __name__ == "__main__":
    main()
