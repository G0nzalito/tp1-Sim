import math
import random
from collections import defaultdict

def exponencial(lambda_param, size=1):
    return [-math.log(1 - random.random()) / lambda_param 
            for _ in range(size)]

def histograma_texto(datos, bins=10, lambda_param=None):
    # Calcular rangos
    min_val = min(datos)
    max_val = max(datos)
    bin_size = (max_val - min_val) / bins
    
    # Crear bins
    frecuencias = defaultdict(int)
    for val in datos:
        bin_num = int((val - min_val) / bin_size)
        if bin_num == bins:  # Caso para el valor máximo
            bin_num -= 1
        frecuencias[bin_num] += 1
    
    # Dibujar histograma en texto
    max_freq = max(frecuencias.values())
    scale = 50 / max_freq  # Escala para ajustar a 50 caracteres
    
    print("\nHISTOGRAMA DE DISTRIBUCIÓN EXPONENCIAL (TEXTO)\n")
    for bin in range(bins):
        lower = min_val + bin * bin_size
        upper = min_val + (bin + 1) * bin_size
        count = frecuencias.get(bin, 0)
        bar = '■' * int(count * scale)
        print(f"{lower:.2f}-{upper:.2f}: {bar} {count}")
    
    print(f"\nTotal de valores: {len(datos)}")
    print(f"Valor mínimo: {min_val:.4f}")
    print(f"Valor máximo: {max_val:.4f}")
    print(f"Media teórica (1/λ): {1/lambda_param:.4f}")

# Ejemplo de uso
lambda_valor = 1.5
datos = exponencial(lambda_valor, 100)

# Mostrar histograma en texto
histograma_texto(datos, bins=10, lambda_param=lambda_valor)