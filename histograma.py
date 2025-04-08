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

def histograma2(datos, distribucion="uniforme", bins=20):
    """
    Genera un histograma a partir de los datos proporcionados.
    
    Parámetros:
    - datos: Lista o array de valores numéricos a graficar
    - distribucion: Nombre de la distribución (para el título)
    - bins: Número de intervalos para el histograma
    """
    # Convertir los datos a una Serie de pandas
    datos_series = pd.Series(datos)
    
    # Crear el histograma
    datos_series.plot.hist(grid=True, bins=bins, rwidth=0.9, color='#607c8e')
    
    # Añadir título y etiquetas
    plt.title(f'Histograma de la distribución {distribucion}')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    
    # Configuración de la cuadrícula
    plt.grid(axis='y', alpha=0.75)
    
    # Mostrar el gráfico
    plt.show()

# def convertirNumerosAHistogramaFriendly():
