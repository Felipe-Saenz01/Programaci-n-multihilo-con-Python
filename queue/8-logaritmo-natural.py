# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# LOGARITMO NATURAL
import math
import threading
import random
import queue

logaritmos = queue.Queue()


def calcular_logaritmo(num):
    log = math.log(num)
    logaritmos.put([num, log])



def main():
    rango = int(input("Ingrese la cantidad de números: "))
    hilos = []

    for i in range(rango):
        num = random.randint(i+1, 50)
        hilo = threading.Thread(target=calcular_logaritmo, args=(num,))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
        hilo.join()

    while not logaritmos.empty():
        numero, log = logaritmos.get()
        print(f"El logaritmo natural de {numero} es: {log}")



if __name__ == "__main__":
    main()