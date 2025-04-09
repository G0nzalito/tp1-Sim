import random
import math


def generador_uniforme(a, b, cantidadAGenerar):
    numerosRandom = [round(random.random(), 2) for _ in range(cantidadAGenerar)]

    print(numerosRandom)

    rnd = round(random.random(), 2)
    x = a + rnd * (b - a)
    x = round(x, 2)
    return [round(a + (b - a) * u, 2) for u in numerosRandom]


def generador_expo(lambParam, cantidadAGenerar):
    numerosRandom = [round(random.random(), 2) for _ in range(cantidadAGenerar)]

    resultados = []

    for ran in numerosRandom:
        while ran == 0 or ran == 1:
            ran = round(random.random(), 2)

        loge = math.log(1 - ran)
        x = -loge / lambParam
        x = round(x, 2)
        resultados.append(x)

    return resultados


def generador_poisson(lambParam, cantidadAGenerar):
    resultado = []

    for _ in range(cantidadAGenerar):
        p = 1
        x = -1
        a = math.exp(-lambParam)
        u = random.random()
        p = p * u
        x = x + 1
        while p >= a:
            u = random.random()
            p = p * u
            x = x + 1
        resultado.append(x)

    return resultado


def generador_normal(media, desviacion, cantidadAGenerar):
    resultados = []

    for _ in range(cantidadAGenerar):
        ran1 = round(random.random(), 2)
        ran2 = round(random.random(), 2)
        while ran1 == 0 or ran1 == 1 or ran2 == 0 or ran2 == 1:
            ran1 = round(random.random(), 2)
            ran2 = round(random.random(), 2)

        z = math.sqrt(-2 * math.log(ran1)) * math.cos(2 * math.pi * ran2)
        valor = media + z * desviacion
        valor = round(valor, 2)
        resultados.append(valor)

    return resultados

