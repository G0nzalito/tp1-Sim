from simulaciones_TP1 import *

decision = 0

while decision != 3:
    print("Seleccione una opción")
    print("1. Generador uniforme")
    print("2. Generador exponencial")
    print("3. Salir")

    decision = int(input("Opción: "))

    if decision != 3:
        cantidadAGenerar = int(
            input("Cuantos números aleatorios desea generar? (Maximo: 50000) ")
        )
        if cantidadAGenerar > 50000:
            print("El máximo es 50000. Se generarán 50000 números aleatorios.")
            cantidadAGenerar = 50000
        if decision == 1:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            print(
                "Los numeros aleatorios son: ",
                generador_uniforme(a, b, cantidadAGenerar),
            )
        elif decision == 2:
            media = float(input("Ingrese el valor de la media: "))
            print(
                "Los numeros aleatorios son: ", generador_expo(media, cantidadAGenerar)
            )
    elif decision == 3:
        print("Saliendo...")
    else:
        print("Opción inválida. Intente nuevamente.")
