import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Partido(BaseModel):
    Index: int
    Date: str
    HomeTeam: str
    AwayTeam: str
    FTHG: int
    FTAG: int
    FTR: str
    HTHG: int
    HTAG: int
    HTR: str
    HS: int
    AS: int
    HST: int
    AST: int
    HF: int
    AF: int
    HC: int
    AC: int
    HY: int
    AY: int
    HR: int
    AR: int
    B365H: float
    B365D: float
    B365A: float
    BWH: float
    BWD: float
    BWA: float
    IWH: float
    IWD: float
    IWA: float
    WHH: float
    WHD: float
    WHA: float
    VCH: float
    VCD: float
    VCA: float
    Temporada: int


class ListadoPartidos(BaseModel):
    partidos: List[Partido]

app = FastAPI()


@app.get("/retrieve_data/")
async def retrieve_data ():
    todosmisdatos = pd.read_csv('./data/liga.csv',sep=',')
    todosmisdatos.fillna(0, inplace=True)
    partidos_list = todosmisdatos.to_dict(orient='records')
    listado = ListadoPartidos(partidos=partidos_list)
    return listado