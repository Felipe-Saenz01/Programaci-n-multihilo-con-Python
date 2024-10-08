# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CALCULAR RAIZ A LA N
import threading
import queue

cola = queue.Queue()

def calcular(numero, exponente):
    cola.put(numero ** (1/exponente))


def main():
    numeros = [3,5,7,9,11]
    exponente = 2
    hilos = []

    for numero in numeros:
        hilo = threading.Thread(target=calcular, args=(numero,exponente))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
        hilo.join()

    for num in numeros:
        print(f"La raiz {exponente}-ésima de {num} es: {cola.get()}")



if __name__ == "__main__":
    main()