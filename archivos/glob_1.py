import numpy as np
import pandas as pd
import glob # módulo que detecta nombres de ruta que siguen un patrón determinado
import os

ruta = "/Users/carlosdelosriosmouvet/Documentos/Practica_progra_ufv/fastapi/data"

listado_de_archivos = glob.glob(os.path.join(ruta,'SP1*.csv'))
def importa(archivo):
    tmp = pd.read_csv(archivo,  on_bad_lines='skip')
    return tmp


ligas = [importa(i) for i in listado_de_archivos]


#Debido a que se usan dos formatos de fecha diferentes se unifican todos en la misma
for i in ligas:
    try:
        i['Date'] = pd.to_datetime(i['Date'], format='%d/%m/%Y')
    except ValueError:
        i['Date'] = pd.to_datetime(i['Date'], format='%d/%m/%y')

#Indico a qué temporadas se corresponden
for i in ligas:
    i["Temporada"] =  max(i["Date"]).year

#Combinamos todas las temporadas
partidos = pd.concat([i for i in ligas], axis=0)

#creo un método para borrar aquellas columnas que todos sus valores estén vacios
def quitavacios(dataframe):
  for column_name in dataframe.columns:
    if dataframe[column_name].isna().all():
      dataframe.drop(column_name, axis=1, inplace=True)
    else:
      continue


# Creo un método para borrar aquellas filas que todos sus valores estén vacios
def quitavacios_filas(dataframe):
    dataframe.dropna(how='all', inplace=True)


quitavacios(partidos)
quitavacios_filas(partidos)


#partidos = partidos.sort_values(by='Date')

partidos.to_csv('/Users/carlosdelosriosmouvet/Documentos/dataliga.csv', index=False)