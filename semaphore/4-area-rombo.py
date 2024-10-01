# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# AREA DE UN ROMBO
import threading
from threading import Semaphore

diagonal1 = 0
diagonal2 = 0
semaphore = Semaphore()

def calcular_area_rombo():
    with semaphore:
        area = (diagonal1 * diagonal2) / 2
        print("El área del rombo es:", area)


def obtener_diagonales():
    global diagonal1
    global diagonal2
    with semaphore:
        diagonal1 = float(input("Ingrese la longitud de la primera diagonal: "))
        diagonal2 = float(input("Ingrese la longitud de la segunda diagonal: "))


def main():
    hilo1 = threading.Thread(target=obtener_diagonales)
    hilo2 = threading.Thread(target=calcular_area_rombo)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()