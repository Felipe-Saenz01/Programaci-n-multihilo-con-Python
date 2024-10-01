# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CONTAR 2 EN 2
import threading
from threading import Semaphore

inicio = 0
final = 0
semaphore = Semaphore()

def contar_dos_en_dos():
    contador = 0
    numeros= []
    with semaphore:
        for num in range(inicio, final + 1, 2):
            contador += 1
            numeros += [num]
        print("Cantidad de números de 2 en 2:", contador)
        print(f"los numeros son: {numeros}")

def obtener_datos():
    global inicio
    global final
    with semaphore:
        inicio = int(input("Ingrese el número inicial: "))
        final = int(input("Ingrese el número final: "))


def main():
    hilo1 = threading.Thread(target=obtener_datos)
    hilo2 = threading.Thread(target=contar_dos_en_dos)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()