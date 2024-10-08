# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# AREA DE UN ROMBO
import threading
import queue
import random

cola = queue.Queue()
def calcular_area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    cola.put([diagonal1,diagonal2,area])


def main():
    cantidad_rombos = int(input("Ingrese la cantida de rombos: "))
    hilos = []
    for i in range(cantidad_rombos):
        diagonal1 = random.randint(5, 30)
        diagonal2 = random.randint(5, 30)
        hilo = threading.Thread(target=calcular_area_rombo, args=(diagonal1,diagonal2))
        hilos += [hilo]
        hilo.start()

    for i in range(cantidad_rombos):
        diagonal1, diagonal2, area = cola.get()
        print(f"El rombo {i + 1} su primera diagonal es: {diagonal1}, su segunda diagonal es: {diagonal2} y su area es: {area}")



if __name__ == "__main__":
    main()