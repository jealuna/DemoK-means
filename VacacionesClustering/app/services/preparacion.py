import pandas as pd
import numpy as np
from app.services.visualizacion import grafica
from app.services.clasificacion import agrupa
from bs4 import BeautifulSoup as Soup

def lee_kml(ruta):
    with open(ruta) as datos:
        kml_soup = Soup(datos, 'lxml-xml')
    coordenadas = kml_soup.find_all('coordinates')
    lista_coordenadas = []
    for coordenada in coordenadas:
        lista_coordenadas.append(str(coordenada))
    nombres = kml_soup.find_all('name')
    lista_nombres = []
    for nombre in nombres:
        lista_nombres.append(str(nombre))
    columnas = ['Longitud', 'Latitud', 'Nombre']
    coordenadas_df = pd.DataFrame(columns=columnas) 
        
    for i, j in zip(range(len(lista_coordenadas)), range(2, len(lista_nombres))):
        coord = lista_coordenadas[i]
        separada = coord.split(',')
        longitud = float(separada[0][26:])
        latitud = float(separada[1])
        nombre = lista_nombres[j][6:-7]
        coordenadas_df.loc[i] = [longitud, latitud, nombre]
    #grafica(coordenadas_df)
    return coordenadas_df
