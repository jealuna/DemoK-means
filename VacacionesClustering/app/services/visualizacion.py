import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def grafica (coordenadas):
    """
    Grafica una lista de coordenadas

    Args:
        coordenadas (List): Una lista de coordenadas
    """
    fig = plt.figure(figsize=(16,8))
    cmap=plt.cm.rainbow
    norm = matplotlib.colors.BoundaryNorm(np.arange(0,10,1), cmap.N)
    plt.scatter(coordenadas['Longitud'], coordenadas['Latitud'],
                cmap=cmap, norm=norm, s=150, edgecolor='none')
    plt.xlabel('Latitud', fontsize=18)
    plt.ylabel('Longitud', fontsize=18)
    plt.grid()
    plt.show()

def grafica_cluster (cluster, centros):
    """
    Grafica un cluster de puntos

    Args: 
        cluster (List): Una lista con los clústers
        centros (List): Una lista con los centros de los clústers
    """
    cmap=plt.cm.rainbow
    norm = matplotlib.colors.BoundaryNorm(np.arange(0,10,1), cmap.N)
    plt.scatter(cluster['Longitud'], cluster['Latitud'], c=cluster['Cluster'],
                cmap=cmap, norm=norm, s=150, edgecolor='none')
    plt.colorbar(ticks=np.linspace(0,9,10))
    plt.scatter(centros[:, 0], centros[:, 1], c='black', s=100, alpha=0.3);
    plt.xlabel('Latitud', fontsize=14)
    plt.ylabel('Longitud', fontsize=14)
    plt.title('Resultados de aplicar k-means', fontsize=14)
    plt.grid()
    plt.show()