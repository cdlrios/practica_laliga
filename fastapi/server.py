import shutil
import io
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import pandas as pd
from typing import List
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Partido(BaseModel):
    Date:str
    HomeTeam:str
    AwayTeam:str
    FTHG:int
    FTAG:int
    FTR:str
    HTHG:int
    HTAG:int
    HTR:str
    HS:int
    AS:int
    HST:int
    AST:int
    HF:int
    AF:int
    HC:int
    AC:int
    HY:int
    AY:int
    HR:int
    AR:int
    B365H:float
    B365D:float
    B365A:float
    BWH:float
    BWD:float
    BWA:float
    IWH:float
    IWD:float
    IWA:float
    LBH:float
    LBD:float
    LBA:float
    PSH:float
    PSD:float
    PSA:float
    WHH:float
    WHD:float
    WHA:float
    VCH:float
    VCD:float
    VCA:float
    Temporada:int

class ListaPartidos(BaseModel):
    partidos: List[Partido]  # Add the type annotation

app = FastAPI(
    title="Servidor de datos",
    description="""Servimos datos de la liga""",
    version="0.1.0",
)

@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('fastapi/dataliga.csv')
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListaPartidos(partidos=todosmisdatosdict)  # Provide data during instance creation
    return listado
