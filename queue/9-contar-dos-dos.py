# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CONTAR 2 EN 2
import threading
import random
import queue

cola = queue.Queue()

def contar_dos_en_dos(inicio, fin):
    contador = 0
    numeros= []
    
    for num in range(inicio, fin + 1, 2):
        contador += 1
        numeros += [num]

    cola.put([inicio, fin, contador, numeros])

def main():
    rango = int(input("Ingrese la cantidad de pares: "))
    hilos = []
    for i in range(rango):
        inicio = random.randint(i,100)
        fin = random.randint(inicio,100)
        hilo = threading.Thread(target=contar_dos_en_dos, args=(inicio,fin))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
        hilo.join()
        inicio, fin, contador, numeros = cola.get()
        print(f"Inicio: {inicio}, Fin: {fin}")
        print("Cantidad de números de 2 en 2:", contador)
        print(f"los numeros son: {numeros}")


if __name__ == "__main__":
    main()