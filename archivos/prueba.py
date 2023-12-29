import pandas as pd


todosmisdatos = pd.read_csv('./fastapi/data/liga.csv',sep=',')
todosmisdatos.fillna(0, inplace=True)
partidos_list = todosmisdatos.to_dict(orient='records')

equipos = [d['HomeTeam'] for d in partidos_list if 'HomeTeam' in d]

print(equipos)