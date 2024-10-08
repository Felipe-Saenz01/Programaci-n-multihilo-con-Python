# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# HALLAR SENO, COSENO Y TANGENTE
import math
import threading
import queue
import random

cola = queue.Queue()
def calcular_trigonometricas(angulo):
    radianes = math.radians(angulo)
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)
    cola.put([radianes, seno, coseno, tangente])
    #print(f"Seno: {seno}, Coseno: {coseno}, Tangente: {tangente}")


def main():
    cantidad_angulos = int(input("Ingrese la cantida de angulos: "))
    hilos = []
    for i in range(cantidad_angulos):
        angulo = random.randint(0, 380)
        hilo = threading.Thread(target=calcular_trigonometricas, args=(angulo,))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
        hilo.join()
        radianes, seno, coseno, tangente = cola.get()
        print(f"Las trigonometricas de {radianes} son: seno={seno}, coseno={coseno}, tangente={tangente}")


if __name__ == "__main__":
    main()