# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# ORDENAR NUMERO DE MAYOR A MENOR
import threading
import random
import queue

cola = queue.Queue()

def almacenar_numeros(num):
    cola.put(num)
        

def mostrar_numeros(numeros):
    print("Números ordenados de mayor a menor:")
    numeros.sort(reverse=True)
    for numero in numeros:
        print(numero)

def main():
    cantidad = int(input("Ingrese el número de elementos: "))
    hilos = []
    numeros = []
    print(f"Numeros:")
    for i in range(cantidad):
        num = random.randint(i, 50)
        print(num)
        hilo = threading.Thread(target=almacenar_numeros, args=(num,))
        hilos += [hilo]
        hilo.start()

    for hilo in hilos:
         hilo.join()
         numeros += [cola.get()]

    
    hilo2 = threading.Thread(target=mostrar_numeros, args=(numeros,))
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()