from simulaciones_TP1 import (
    generador_uniforme,
    generador_expo,
    generador_poisson,
    generador_normal,
)
import histograma


def main():
    decision = 0
    while decision != -1:
        menu = "Seleccione una opción: \n1. Generador uniforme\n2. Generador exponencial\n3. Generador Poisson\n4. Generador Normal\n-1. Salir"
        print(menu)

        decision = int(input("Opción: "))

        if decision != -1:
            cantidadAGenerar = int(
                input("Cuantos números aleatorios desea generar? (Maximo: 50000) ")
            )
            if cantidadAGenerar > 50000:
                print("El máximo es 50000. Se generarán 50000 números aleatorios.")
                cantidadAGenerar = 50000
            intervalos = int(
                input("Ingrese el número de intervalos para el histograma: ")
            )
            if decision == 1:
                a = float(input("Ingrese el valor de a: "))

                b = float(input("Ingrese el valor de b: "))
                while b <= a:
                    print("El valor de b debe ser mayor que a.")
                    b = float(input("Ingrese de nuevo el valor de b: "))

                datos_uniformes = generador_uniforme(a, b, cantidadAGenerar)
                print(f"Los numeros aleatorios son: {datos_uniformes}")

                histograma.histograma(
                    datos_uniformes, bins=intervalos, distribucion="Uniforme"
                )
            elif decision == 2:
                media = float(input("Ingrese el valor de la media: "))
                datos_exponenciales = generador_expo(media, cantidadAGenerar)
                print(f"Los numeros aleatorios son: {datos_exponenciales}")
                histograma.histograma(
                    datos=datos_exponenciales,
                    distribucion="Exponencial",
                    bins=intervalos,
                )
            elif decision == 3:
                media = float(input("Ingrese el valor del valor lambda de poisson: "))
                datos_poisson = generador_poisson(media, cantidadAGenerar)
                print(f"Los numeros aleatorios son: {datos_poisson}")
                histograma.histograma(
                    datos=datos_poisson, distribucion="Poisson", bins=intervalos
                )
            elif decision == 4:
                media = float(input("Ingrese el valor de la media normal: "))
                desivacion = float(
                    input("Ingrese el valor de la desviación estándar: ")
                )
                datos_normal = generador_normal(
                    media, desivacion, cantidadAGenerar=cantidadAGenerar
                )
                print(f"Los numeros aleatorios son: {datos_normal}")
                histograma.histograma(
                    datos=datos_normal, distribucion="Normal", bins=intervalos
                )
        elif decision == -1:
            print("Saliendo...")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
