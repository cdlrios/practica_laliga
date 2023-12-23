import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import time

#Carga de datos
SP1_2024 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_23_24.csv")
SP1_2023 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_22_23.csv")
SP1_2022 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_21_22.csv")
SP1_2021 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_20_21.csv")
SP1_2020 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_19_20.csv")
SP1_2019 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_18_19.csv")
SP1_2018 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_17_18.csv")
SP1_2017 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_16_17.csv")
SP1_2016 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_15_16.csv")
SP1_2015 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_14_15.csv")
SP1_2014 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_13_14.csv")
SP1_2013 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_12_13.csv")
SP1_2012 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_11_12.csv")
SP1_2011 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_10_11.csv")
SP1_2010 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_09_10.csv")
SP1_2009 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_08_09.csv")
SP1_2008 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_07_08.csv")
SP1_2007 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_06_07.csv")
SP1_2006 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_05_06.csv")
#SP1_2005 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_04_05.csv")
SP1_2004 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_03_04.csv")
SP1_2003 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_02_03.csv")
SP1_2002 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_01_02.csv")
SP1_2001 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_00_01.csv")
SP1_2000 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_99_00.csv")
SP1_1999 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_98_99.csv")
SP1_1998 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_97_98.csv")
SP1_1997 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_96_97.csv")
SP1_1996 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_95_96.csv")
SP1_1995 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_94_95.csv")
SP1_1994 = pd.read_csv("/Users/carlosdelosriosmouvet/Documentos/Practica_progra/data/SP1_93_94.csv")

#Unimos todos los dataframes en uno solo
partidos = pd.concat([SP1_2024, SP1_2023, SP1_2022, SP1_2021, SP1_2020, SP1_2019, SP1_2018, SP1_2017, SP1_2016, SP1_2015, SP1_2014, SP1_2013, SP1_2012, SP1_2011, SP1_2010, SP1_2009, SP1_2008, SP1_2007, SP1_2006, SP1_2004, SP1_2003, SP1_2002, SP1_2001, SP1_2000, SP1_1999, SP1_1998, SP1_1997, SP1_1996, SP1_1995, SP1_1994], ignore_index=True)

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





