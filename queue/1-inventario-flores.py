# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

import threading
import queue
import random

# INVENTARIO
cola = queue.Queue()


def inventario_flores(nombre, cantidad):
    cola.put((nombre,cantidad))


def main():
    numero_flores = random.randint(1,7)
    flores = ['Rosas', 'Tulipanes', 'Claveles', 'Girasoles', 'Orquideas', 'Margarita', 'Lirios']
    hilos = []

    for num in range(numero_flores):
        nombre = random.choice(flores)
        flores.remove(nombre)
        cantidad = random.randint(10,50)
        hilo = threading.Thread(target=inventario_flores,args=(nombre,cantidad) )
        hilos += [hilo]
        hilo.start()

    for num in range(numero_flores):
        nombre, cantidad = cola.get()
        print(f"Hay {cantidad} de {nombre}")


if __name__ == '__main__':
    main()