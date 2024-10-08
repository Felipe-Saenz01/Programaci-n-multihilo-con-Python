# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# AREA DE UN CIRCULO
import math
import threading
import queue
import random

cola = queue.Queue()

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    cola.put((radio,area))


def main():
    cantidad_circulos = int(input("Ingrese la cantida de circulos: "))
    hilos = []
    for i in range(cantidad_circulos):
        radio = random.randint(5, 30)
        hilo = threading.Thread(target=calcular_area_circulo, args=(radio,))
        hilos += [hilo]
        hilo.start()

    for i in range(cantidad_circulos):
        radio, area = cola.get()
        print(f"El circulo {i+1} tiene radio: {radio} y area: {area}")


if __name__ == "__main__":
    main()