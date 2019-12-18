import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans 

def agrupa(coordenadas, numero):
    kmeans_1 = KMeans(n_clusters=numero)
    X = coordenadas[['Longitud','Latitud']].values
    predicciones = kmeans_1.fit_predict(X)
    agrupado = pd.concat([coordenadas.reset_index(), pd.DataFrame({'Cluster':predicciones})], axis=1)
    agrupado.drop('index', axis=1, inplace=True)
    condiciones = []
    dias = []
    for cluster in range(10):
        condiciones.append(agrupado['Cluster'] == cluster)
        dias.append('Día ' + str(cluster+1))
    agrupado['DiadeVacaciones'] = np.select(condiciones, dias, default='black')
    agrupado.sort_values(by=['Cluster'], inplace=True)
    centros = kmeans_1.cluster_centers_
    return agrupado, centros