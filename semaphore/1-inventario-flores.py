# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

import threading
from threading import Semaphore

# INVENTARIO

inventario = []
semaphore = Semaphore()


def inventario_flores(n):
    global inventario
    # n = int(input("Ingrese el número de tipos de flores en el inventario: "))
    with semaphore:
        for i in range(n):
            flor = []
            flor += [input(f"Ingrese el nombre de la flor {i+1}: ")]
            flor += [int(input(f"Ingrese la cantidad de {flor[0]}: "))]
            inventario += [flor]



def mostrar_invetario():
    semaphore.acquire()
    try:
        for item in inventario:
            print("Hay", item[1], "de", item[0])
    finally:
        semaphore.release()

def main():
    n = int(input("Ingrese el número de tipos de flores en el inventario: "))
    hilo1 = threading.Thread(target=inventario_flores, args=(n,))
    hilo2 = threading.Thread(target=mostrar_invetario)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()
    #print(inventario)
    print(semaphore._value)

if __name__ == '__main__':
    main()