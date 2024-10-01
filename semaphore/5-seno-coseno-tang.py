# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# HALLAR SENO, COSENO Y TANGENTE
import math
import threading
from threading import Semaphore

radianes = 0
semaphore = Semaphore()

def calcular_trigonometricas():
    with semaphore:
        seno = math.sin(radianes)
        coseno = math.cos(radianes)
        tangente = math.tan(radianes)
    print(f"Seno: {seno}, Coseno: {coseno}, Tangente: {tangente}")

def obtener_angulo():
    global radianes
    with semaphore:
        angulo = float(input("Ingrese el ángulo en grados: "))
        radianes = math.radians(angulo)

def main():
    hilo1 = threading.Thread(target=obtener_angulo)
    hilo2 = threading.Thread(target=calcular_trigonometricas)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()