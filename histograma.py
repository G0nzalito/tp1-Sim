import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def histograma(distribucion):
    # Generar datos de tiempos de traslado con una distribución gamma
    size, scale = 1000, 10
    commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)
    print (commutes)
    # Crear el histograma bins son los intervalos, rwidth es el ancho de las barras
    # y color es el color de las barras
    commutes.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')

    # Añadir título y etiquetas
    plt.title('Histograma de la distribucion' +  distribucion)
    plt.xlabel('Cantidad')
    plt.ylabel('Numeros')

    # Configuración de la cuadrícula para mejorar la visualización
    plt.grid(axis='y', alpha=0.75)

    # Mostrar el gráfico
    plt.show()

# def convertirNumerosAHistogramaFriendly():
