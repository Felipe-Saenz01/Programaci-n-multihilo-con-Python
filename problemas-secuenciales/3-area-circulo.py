# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# AREA DE UN CIRCULO
import math
import threading
area = 0
lock = threading.Lock()

def calcular_area_circulo():
    global area
    with lock:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * (radio ** 2)

def mostrar_area():
    with lock:
        print("El área del círculo es:", area)


def main():
    hilo1 = threading.Thread(target=calcular_area_circulo)
    hilo2 = threading.Thread(target=mostrar_area)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()