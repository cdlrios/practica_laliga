import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import time
import requests

response = requests.get("http://fastapi:8000//retrieve_data/")
data = response.json()
partidos = pd.DataFrame(data)

#Creo un método para obtener las columnas con datos vacios de los dataframes.
def compruebavacios(dataframe):
  valores_vacios = []
  for column_name in dataframe.columns:
    if dataframe[column_name].isna().any():
      valores_vacios.append(column_name)
    else:
      continue
  if len(valores_vacios)==0:
    print("No hay valores vacios en este dataframe")
  else:
    print("Las columnas con valores vacios son: ")
    for i in valores_vacios:
      print(i)

#creo un método para borrar aquellas columnas que todos sus valores estén vacios
def quitavacios(dataframe):
  for column_name in dataframe.columns:
    if dataframe[column_name].isna().all():
      dataframe.drop(column_name, axis=1, inplace=True)
    else:
      continue


#printeo los nombres de los equipos en el dataframe
print(partidos["HomeTeam"].unique())
print(len(partidos))


#Para una mejor comprensión de los datos, sustituimos los nombres de los equipos por sus abreviaturas
#equipos_1617 = {"Nombre": equipos, "Abreviatura": ["ALA", "ATH", "ATM", "FCB", "BET", "CEL", "EIB", "ESP", "GRA", "DEP", "LPA", "LEG", "MAL", "OSA", "RMA", "SEV", "RSO", "SPO", "VAL", "VILL"]}
#df_temporada_1617 = pd.DataFrame(equipos_1617)

#Sustituyo los nombres de los equipos por sus abreviaturas en el dataframe original
#partidos["HomeTeam"] = partidos["HomeTeam"].map(df_temporada_1617.set_index("Nombre")["Abreviatura"])
#partidos["AwayTeam"] = partidos["AwayTeam"].map(df_temporada_1617.set_index("Nombre")["Abreviatura"])

#print(partidos)

# Datos de ejemplo para la temporada 16/17 con nombres y abreviaturas
#datos_temporada_1617 = {"Nombre": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Villarreal", "Real Sociedad", "Athletic Bilbao", "Eibar", "Espanyol", "Alavés", "Málaga", "Valencia", "Celta de Vigo", "Las Palmas", "Real Betis", "La Coruna", "Leganés", "Sporting Gijón", "Osasuna", "Granada"], "Abreviatura": ["RMA", "BAR", "ATM", "SEV", "VIL", "RSO", "ATH", "EIB", "ESP", "ALA", "MAL", "VAL", "CEL", "LPA", "RBB", "DEP", "LEG", "SPO", "OSA", "GRA"]}


#df.fillna(0, inplace=True)  # Reemplaza los valores faltantes con 0 (u otro valor)
#df = df[df['columna'] > 0]  # Mantiene solo las filas donde 'columna' es mayor a 0
#df.rename(columns={'viejo_nombre': 'nuevo_nombre'}, inplace=True)
#df.drop(['columna_a_eliminar'], axis=1, inplace=True)
#df = df[(df['columna'] > limite_inferior) & (df['columna'] < limite_superior)]
#df['columna'] = (df['columna'] - df['columna'].mean()) / df['columna'].std()
#df.to_csv('tu_archivo_limpio.csv', index=False)

#Creo un método para obtener las columnas con datos vacios de los dataframes.
def compruebavacios(dataframe):
  valores_vacios = []
  for column_name in dataframe.columns:
    if dataframe[column_name].isna().any():
      valores_vacios.append(column_name)
    else:
      continue
  if len(valores_vacios)==0:
    print("No hay valores vacios en este dataframe")
  else:
    print("Las columnas con valores vacios son: ")
    for i in valores_vacios:
      print(i)

compruebavacios(partidos)
quitavacios(partidos)
st.title('Campeonato Nacional de Liga de Primera División')

equipo_seleccionado = st.selectbox('Selecciona un equipo:', partidos['HomeTeam'].unique())

partidos_filtrados = partidos[partidos['HomeTeam'] == equipo_seleccionado]

st.dataframe(partidos_filtrados)





