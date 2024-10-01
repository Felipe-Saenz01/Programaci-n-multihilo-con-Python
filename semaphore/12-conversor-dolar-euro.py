# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

#  CONVERSOR DE PEASO A DOLARES Y EUROS
import threading
from threading import Semaphore

cantidad_pesos = 0
semaphore = Semaphore()


def convertir_pesos():
    with semaphore:
        tasa_dolar = 0.047  # Tasa de cambio de pesos a dólares
        tasa_euro = 0.039  # Tasa de cambio de pesos a euros
        cantidad_dolares = cantidad_pesos * tasa_dolar
        cantidad_euros = cantidad_pesos * tasa_euro
        print(f"{cantidad_pesos} pesos equivalen a {cantidad_dolares} dólares y {cantidad_euros} euros.")


def obtener_datos():
    global cantidad_pesos
    with semaphore:
        cantidad_pesos = float(input("Ingrese la cantidad en pesos: "))



def main():
    hilo1 = threading.Thread(target=obtener_datos)
    hilo2 = threading.Thread(target=convertir_pesos)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()