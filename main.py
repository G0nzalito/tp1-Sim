from simulaciones_TP1 import *
import histograma

decision = 0

while decision != 3:
    menu = "Seleccione una opción: \n1. Generador uniforme\n2. Generador exponencial\n3. Salir"
    print(menu)

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
            while b <= a:
                print("El valor de b debe ser mayor que a.")
                b = float(input("Ingrese de nuevo el valor de b: "))
            print(
                "Los numeros aleatorios son: ",
                generador_uniforme(a, b, cantidadAGenerar),
            )
            histograma.histograma( distribucion="Uniforme")
        elif decision == 2:
            media = float(input("Ingrese el valor de la media: "))
            print(
                "Los numeros aleatorios son: ", generador_expo(media, cantidadAGenerar)
            )
            histograma.histograma(distribucion="Exponencial")
    elif decision == 3:
        print("Saliendo...")
    else:
        print("Opción inválida. Intente nuevamente.")
