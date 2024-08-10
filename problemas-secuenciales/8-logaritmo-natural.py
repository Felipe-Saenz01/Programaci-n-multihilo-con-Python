# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# LOGARITMO NATURAL
import math
import threading

numero = 0

def calcular_logaritmo():
    logaritmo = math.log(numero)
    print("El logaritmo natural de", numero, "es:", logaritmo)

def obtener_numero():
    global numero
    numero = float(input("Ingrese el número: "))



def main():
    hilo1 = threading.Thread(target=obtener_numero)
    hilo2 = threading.Thread(target=calcular_logaritmo)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()