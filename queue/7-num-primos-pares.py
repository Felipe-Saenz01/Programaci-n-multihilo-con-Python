# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# HALLAR NUMERO PRIMOS Y PARES
import threading
import queue


primos = queue.Queue()
pares = queue.Queue()


def primos_pares(num):
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
        primos.put(num)
    if num % 2 == 0:
        pares.put(num)


def main():
    rango = int(input("Ingrese el rango de números: "))
    hilos = []

    for i in range(2,rango+1):
        hilo = threading.Thread(target=primos_pares, args=(i,))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Números pares:")
    while not pares.empty():
        print(pares.get())

    print("\nNúmeros primos:")
    while not primos.empty():
        print(primos.get())
   


if __name__ == "__main__":
    main()