import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    data_path = 'data/liga.csv'
    partidos = pd.read_csv(data_path)
    return partidos

def show_analisis_historico():
    st.title("Análisis por temporada")
    # Cargar los datos
    partidos = load_data()
    st.title("Clasificación general")
    temporada_seleccionada = st.selectbox("Selecciona una Temporada", options=partidos['Temporada'].unique())
     #filtro los partidos de la temporada seleccionada
    partidos = partidos[partidos['Temporada'] == temporada_seleccionada]
    
    partidos['HP'] = None
    partidos['AP'] = None

    for index, row in partidos.iterrows():
        if row["FTHG"] > row["FTAG"]:
            partidos.at[index, "HP"] = 3
            partidos.at[index, "AP"] = 0
        elif row["FTHG"] < row["FTAG"]:
            partidos.at[index, "HP"] = 0
            partidos.at[index, "AP"] = 3
        else:
            partidos.at[index, "HP"] = 1
            partidos.at[index, "AP"] = 1


    #Creo un dataframe con los nombres de los equipos
    equipos = pd.DataFrame({'Equipo': partidos['HomeTeam'].unique()})

    #Creo una tabla auxiliar con el nombre del equipo sus puntos totales y sus puntos en casa y fuera
    puntos_loc = partidos.groupby("HomeTeam")["HP"].sum()
    puntos_vis = partidos.groupby("AwayTeam")["AP"].sum()
    puntos = puntos_loc + puntos_vis

    #Goles marcados
    goles_loc = partidos.groupby("HomeTeam")["FTHG"].sum()
    goles_vis = partidos.groupby("AwayTeam")["FTAG"].sum()

    #Goles recibidos
    goles_con_loc = partidos.groupby("HomeTeam")["FTAG"].sum()
    goles_con_vis = partidos.groupby("AwayTeam")["FTHG"].sum()

    #Tiros de campo realizados
    tiros_loc = partidos.groupby("HomeTeam")["HS"].sum()
    tiros_vis = partidos.groupby("AwayTeam")["AS"].sum()

    #Tiros de campo recibidos
    tiros_con_loc = partidos.groupby("HomeTeam")["AS"].sum()
    tiros_con_vis = partidos.groupby("AwayTeam")["HS"].sum()

    #Tiros a puerta realizados
    tiros_puerta_loc = partidos.groupby("HomeTeam")["HST"].sum()
    tiros_puerta_vis = partidos.groupby("AwayTeam")["AST"].sum()

    #Tiros a puerta recibidos
    tiros_puerta_con_loc = partidos.groupby("HomeTeam")["AST"].sum()
    tiros_puerta_con_vis = partidos.groupby("AwayTeam")["HST"].sum()

    #Faltas cometidas
    faltas_loc = partidos.groupby("HomeTeam")["HF"].sum()
    faltas_vis = partidos.groupby("AwayTeam")["AF"].sum()

    #Faltas recibidas
    faltas_con_loc = partidos.groupby("HomeTeam")["AF"].sum()
    faltas_con_vis = partidos.groupby("AwayTeam")["HF"].sum()

    #Tarjetas amarillas recibidas
    tarjetas_amarillas_loc = partidos.groupby("HomeTeam")["HY"].sum()
    tarjetas_amarillas_vis = partidos.groupby("AwayTeam")["AY"].sum()

    #Tarjetas amarillas contrincantes
    tarjetas_amarillas_con_loc = partidos.groupby("HomeTeam")["AY"].sum()
    tarjetas_amarillas_con_vis = partidos.groupby("AwayTeam")["HY"].sum()

    #Tarjetas rojas recibidas
    tarjetas_rojas_loc = partidos.groupby("HomeTeam")["HR"].sum()
    tarjetas_rojas_vis = partidos.groupby("AwayTeam")["AR"].sum()

    #Tarjetas rojas contrincantes
    tarjetas_rojas_con_loc = partidos.groupby("HomeTeam")["AR"].sum()
    tarjetas_rojas_con_vis = partidos.groupby("AwayTeam")["HR"].sum()

    #Media de cotización Bet 365
    cot_loc_victoria_b365 = partidos.groupby("HomeTeam")["B365H"].mean()
    cot_loc_empate_b365 = partidos.groupby("HomeTeam")["B365D"].mean()
    cot_loc_derrota_b365 = partidos.groupby("HomeTeam")["B365A"].mean()
    cot_vis_victoria_b365 = partidos.groupby("AwayTeam")["B365A"].mean()
    cot_vis_empate_b365 = partidos.groupby("AwayTeam")["B365D"].mean()
    cot_vis_derrota_b365 = partidos.groupby("AwayTeam")["B365H"].mean()

    #Media de cotización William Hill
    cot_loc_victoria_wh = partidos.groupby("HomeTeam")["WHH"].mean()
    cot_loc_empate_wh = partidos.groupby("HomeTeam")["WHD"].mean()
    cot_loc_derrota_wh = partidos.groupby("HomeTeam")["WHA"].mean()
    cot_vis_victoria_wh = partidos.groupby("AwayTeam")["WHA"].mean()
    cot_vis_empate_wh = partidos.groupby("AwayTeam")["WHD"].mean()
    cot_vis_derrota_wh = partidos.groupby("AwayTeam")["WHH"].mean()

    #Media de cotización de Bet&Win
    cot_loc_victoria_bw = partidos.groupby("HomeTeam")["BWH"].mean()
    cot_loc_empate_bw = partidos.groupby("HomeTeam")["BWD"].mean()
    cot_loc_derrota_bw = partidos.groupby("HomeTeam")["BWA"].mean()
    cot_vis_victoria_bw = partidos.groupby("AwayTeam")["BWA"].mean()
    cot_vis_empate_bw = partidos.groupby("AwayTeam")["BWD"].mean()
    cot_vis_derrota_bw = partidos.groupby("AwayTeam")["BWH"].mean()

    #Media de cotización de Interwetten
    cot_loc_victoria_iw = partidos.groupby("HomeTeam")["IWH"].mean()
    cot_loc_empate_iw = partidos.groupby("HomeTeam")["IWD"].mean()
    cot_loc_derrota_iw = partidos.groupby("HomeTeam")["IWA"].mean()
    cot_vis_victoria_iw = partidos.groupby("AwayTeam")["IWA"].mean()
    cot_vis_empate_iw = partidos.groupby("AwayTeam")["IWD"].mean()
    cot_vis_derrota_iw = partidos.groupby("AwayTeam")["IWH"].mean()

    #Media de cotización de VC Bet
    cot_loc_victoria_vcb = partidos.groupby("HomeTeam")["VCH"].mean()
    cot_loc_empate_vcb = partidos.groupby("HomeTeam")["VCD"].mean()
    cot_loc_derrota_vcb = partidos.groupby("HomeTeam")["VCA"].mean()
    cot_vis_victoria_vcb = partidos.groupby("AwayTeam")["VCA"].mean()
    cot_vis_empate_vcb = partidos.groupby("AwayTeam")["VCD"].mean()
    cot_vis_derrota_vcb = partidos.groupby("AwayTeam")["VCH"].mean()



    #fusiono todas las tablas en una sola
    clasificacion = pd.merge(puntos_loc, puntos_vis, left_index=True, right_index=True)

    #añado una columna con el total de puntos
    clasificacion["TotalPoints"] = clasificacion["HP"] + clasificacion["AP"]
    clasificacion["Goles_Favor"] = goles_loc + goles_vis
    clasificacion["Goles_Contra"] = goles_con_loc + goles_con_vis
    clasificacion["Diferencia_Goles"] = clasificacion["Goles_Favor"] - clasificacion["Goles_Contra"]
    
    #creo tabla tiros
    tiros = pd.DataFrame(clasificacion["TotalPoints"])
    tiros.columns = ["Puntos"]
    tiros["Tiros_local"] = tiros_loc
    tiros["Tiros_visitante"] = tiros_vis
    tiros["TOTAL Tiros"] = tiros_loc + tiros_vis
    tiros["Tiros_puerta_local"] = tiros_puerta_loc
    tiros["Tiros_puerta_local"] = tiros_puerta_vis
    tiros["TOTAL Tiros a puerta"] = tiros["Tiros_puerta_local"] + tiros["Tiros_puerta_local"]
    tiros["% Puntería"] = (tiros["TOTAL Tiros a puerta"] / tiros["TOTAL Tiros"]) * 100
    
    #creo tabla faltas
    faltas = pd.DataFrame(clasificacion["TotalPoints"])
    faltas.columns = ["Puntos"]
    faltas["Faltas cometidas local"] = faltas_loc
    faltas["Faltas cometidas visitante"] = faltas_vis
    faltas["Faltas cometidas"] = faltas_loc + faltas_vis
    faltas["Faltas recibidas local"] = faltas_con_loc
    faltas["Faltas recibidas visitante"] = faltas_con_vis
    faltas["Faltas recibidas"] = faltas_con_loc + faltas_con_vis
    
    #creo tabla tarjetas
    tarjetas = pd.DataFrame(clasificacion["TotalPoints"])
    tarjetas.columns = ["Puntos"]
    tarjetas["T. Amarillas recibidas LOC"] = tarjetas_amarillas_loc
    tarjetas["T. Amarillas recibidas VIS"] = tarjetas_amarillas_vis
    tarjetas["T. Amarillas recibidas TOT"] = tarjetas_amarillas_loc + tarjetas_amarillas_vis
    tarjetas["T. Amarillas contrincante LOC"] = tarjetas_amarillas_con_loc
    tarjetas["T. Amarillas contrincante VIS"] = tarjetas_amarillas_con_vis
    tarjetas["T. Amarillas contrincante TOT"] = tarjetas_amarillas_con_loc + tarjetas_amarillas_con_vis
    tarjetas["T. Rojas recibidas LOC"] = tarjetas_rojas_loc
    tarjetas["T. Rojas recibidas VIS"] = tarjetas_rojas_vis
    tarjetas["T. Rojas recibidas TOT"] = tarjetas_rojas_loc + tarjetas_rojas_vis
    tarjetas["T. Rojas contrincante LOC"] = tarjetas_rojas_con_loc
    tarjetas["T. Rojas contrincante VIS"] = tarjetas_rojas_con_vis
    tarjetas["T. Rojas contrincante TOT"] = tarjetas_rojas_con_loc + tarjetas_rojas_con_vis

    #creo cotizaciones apuestas
    apuestas = pd.DataFrame(clasificacion["TotalPoints"])
    apuestas["B365_LOC_V"] = cot_loc_victoria_b365
    apuestas["B365_LOC_E"] = cot_loc_empate_b365
    apuestas["B365_LOC_D"] = cot_loc_derrota_b365
    apuestas["B365_VIS_V"] = cot_vis_victoria_b365
    apuestas["B365_VIS_E"] = cot_vis_empate_b365
    apuestas["B365_VIS_D"] = cot_vis_derrota_b365
    apuestas["WH_LOC_V"] = cot_loc_victoria_wh
    apuestas["WH_LOC_E"] = cot_loc_empate_wh
    apuestas["WH_LOC_D"] = cot_loc_derrota_wh
    apuestas["WH_VIS_V"] = cot_vis_victoria_wh
    apuestas["WH_VIS_E"] = cot_vis_empate_wh
    apuestas["WH_VIS_D"] = cot_vis_derrota_wh
    apuestas["BS_LOC_V"] = cot_loc_victoria_bw
    apuestas["BS_LOC_E"] = cot_loc_empate_bw
    apuestas["BS_LOC_D"] = cot_loc_derrota_bw
    apuestas["BS_VIS_V"] = cot_vis_victoria_bw
    apuestas["BS_VIS_E"] = cot_vis_empate_bw
    apuestas["BS_VIS_D"] = cot_vis_derrota_bw
    apuestas["IW_LOC_V"] = cot_loc_victoria_iw
    apuestas["IW_LOC_E"] = cot_loc_empate_iw
    apuestas["IW_LOC_D"] = cot_loc_derrota_iw
    apuestas["IW_VIS_V"] = cot_vis_victoria_iw
    apuestas["IW_VIS_E"] = cot_vis_empate_iw
    apuestas["IW_VIS_D"] = cot_vis_derrota_iw
    apuestas["VCB_LOC_V"] = cot_loc_victoria_vcb
    apuestas["VCB_LOC_E"] = cot_loc_empate_vcb
    apuestas["VCB_LOC_D"] = cot_loc_derrota_vcb
    apuestas["VCB_VIS_V"] = cot_vis_victoria_vcb
    apuestas["VCB_VIS_E"] = cot_vis_empate_vcb
    apuestas["VCB_VIS_D"] = cot_vis_derrota_vcb


    efectividad = pd.DataFrame(clasificacion["TotalPoints"])
    efectividad.columns = ["Puntos"]
    efectividad["Efectividad local"] = clasificacion["HP"] / 57
    efectividad["Efectividad visitante"] = clasificacion["AP"] / 57
    efectividad["Efectividad total"] = clasificacion["TotalPoints"] / 114

    #clasificacion["Goles_por_partido_loc"] = goles_loc/19
    #clasificacion["Goles_por_partido_vis"] = goles_vis/19
    #clasificacion["Goles_por_partido"] = (goles_loc + goles_vis)/38
    #clasificacion["Goles_rec_partido_loc"] = goles_con_loc/19
    #clasificacion["Goles_rec_partido_vis"] = goles_con_vis/19
    #clasificacion["Goles_rec_partido"] = (goles_con_loc + goles_con_vis)/38
    #clasificacion["Gol_prom_partido_loc"] = clasificacion["Goles_por_partido_loc"] - clasificacion["Goles_rec_partido_loc"]
    #clasificacion["Gol_prom_partido_vis"] = clasificacion["Goles_por_partido_vis"] - clasificacion["Goles_rec_partido_vis"]
    #clasificacion["Gol_prom_tot"] = clasificacion["Gol_prom_partido_loc"] + clasificacion["Gol_prom_partido_vis"]
    
    # Mostrar las tablas
    st.dataframe(clasificacion.sort_values(by="TotalPoints", ascending=False), use_container_width=True)
    st.header("Tiros")
    st.dataframe(tiros.sort_values(by="Puntos", ascending=False), use_container_width=True)

    st.header("Faltas")
    st.dataframe(faltas.sort_values(by="Puntos", ascending=False), use_container_width=True)

    st.header("Tarjetas")
    st.dataframe(tarjetas.sort_values(by="Puntos", ascending=False), use_container_width=True)

    st.header("Efectividad")
    st.text("Porcentaje de puntos conseguidos entre puntos posibles")
    st.dataframe(efectividad.sort_values(by="Puntos", ascending=False), use_container_width=True)

    st.header("Análisis de Apuestas")
    st.text("A menor cotización más probabilidad de victoria según la casa de apuestas")
    equipo_seleccionado = st.selectbox("Selecciona un Equipo para ver las Cotizaciones de Apuestas", options=partidos['HomeTeam'].unique())

    # Filtrar las cotizaciones para el equipo seleccionado
    cotizaciones_equipo = apuestas.loc[equipo_seleccionado]

    # Preparar los datos para el gráfico
    categorias = ['Victoria', 'Empate', 'Derrota']
    casas_apuestas = ['B365', 'WH', 'BS', 'IW', 'VCB']
    valores_casas = {casa: [cotizaciones_equipo[f'{casa}_LOC_V'], 
                            cotizaciones_equipo[f'{casa}_LOC_E'], 
                            cotizaciones_equipo[f'{casa}_LOC_D']] for casa in casas_apuestas}

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.15
    for i, casa in enumerate(casas_apuestas):
        ax.bar([x + i * bar_width for x in range(len(categorias))], 
               valores_casas[casa], 
               width=bar_width, 
               label=casa)

    # Añadir detalles al gráfico
    ax.set_xlabel('Tipo de Apuesta')
    ax.set_ylabel('Cotización Media')
    ax.set_title(f'Cotizaciones de Apuestas para {equipo_seleccionado}')
    ax.set_xticks([r + bar_width for r in range(len(categorias))])
    ax.set_xticklabels(categorias)
    ax.legend()

    st.pyplot(fig)