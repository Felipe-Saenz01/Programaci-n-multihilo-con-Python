# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# ORDENAR NUMERO DE MAYOR A MENOR
import threading
from threading import Semaphore

numeros = []
semaphore = Semaphore()

def ordenar_numeros():
    global numeros
    with semaphore:
        n = int(input("Ingrese el número de elementos: "))
        for i in range(n):
            numeros += [float(input(f"Ingrese el número {i+1}: "))]
        numeros.sort(reverse=True)

def mostrar_numeros():
    with semaphore:
        print("Números ordenados de mayor a menor:")
        for numero in numeros:
            print(numero)

def main():
    hilo1 = threading.Thread(target=ordenar_numeros)
    hilo2 = threading.Thread(target=mostrar_numeros)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()