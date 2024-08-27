# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CALCULAR RAIZ A LA N
import threading

numero = 0
exponente = 0
lock = threading.Lock()

def calcular():
    with lock:
        resultado = numero ** (1/exponente)
        print(f"La raíz {exponente}-ésima de {numero} es:", resultado)


def datos():
    global numero
    global exponente
    with lock:
        numero = float(input("Ingrese el número: "))
        exponente = float(input("Ingrese el exponente (raíz): "))

def main():
    hilo1 = threading.Thread(target=datos)
    hilo2 = threading.Thread(target=calcular)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()


if __name__ == "__main__":
    main()