import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def histograma(datos, distribucion, bins=20):
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
