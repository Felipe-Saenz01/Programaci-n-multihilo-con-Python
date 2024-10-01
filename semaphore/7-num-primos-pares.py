# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# HALLAR NUMERO PRIMOS Y PARES
import threading
from threading import Semaphore

primos = []
pares = []
semaphore = Semaphore()

def numeros_primos_pares():
    rango = int(input("Ingrese el rango de números: "))
    with semaphore:
        for num in range(2, rango + 1):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                primos.append(num)
            if num % 2 == 0:
                pares.append(num)

def mostrar_primos_pares():
    with semaphore:
        print("Números primos:", primos)
        print("Números pares:", pares)


def main():
    hilo1 = threading.Thread(target=numeros_primos_pares)
    hilo2 = threading.Thread(target=mostrar_primos_pares)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()