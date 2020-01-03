import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans 

def agrupa(coordenadas, numero):
    """
    Realiza el clustering de un conjuto de coordenadas usando k-means

    Args:
        coordenadas (DataFrame): DataFrame de pandas con las coordenadas
        numero (int): Numero de clusters
    Returns:
        DataFrame: Dataframe con las coordenadas contenidas en el archivo
        ndarray: Coordenadas de los centros de los clústers
    """
    kmeans_1 = KMeans(n_clusters=numero)
    X = coordenadas[['Longitud','Latitud']].values
    predicciones = kmeans_1.fit_predict(X)
    agrupado = pd.concat([coordenadas.reset_index(), pd.DataFrame({'Cluster':predicciones})], axis=1)
    agrupado.drop('index', axis=1, inplace=True)
    condiciones = []
    dias = []
    for cluster in range(numero):
        condiciones.append(agrupado['Cluster'] == cluster)
        dias.append('Día ' + str(cluster+1))
    agrupado['DiadeVacaciones'] = np.select(condiciones, dias, default='black')
    agrupado.sort_values(by=['Cluster'], inplace=True)
    centros = kmeans_1.cluster_centers_
    return agrupado, centros