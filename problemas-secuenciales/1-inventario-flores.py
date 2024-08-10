# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

import threading


# INVENTARIO

inventario = []


def inventario_flores():
    global inventario
    n = int(input("Ingrese el número de tipos de flores en el inventario: "))
    for i in range(n):
        flor= []
        flor += [input(f"Ingrese el nombre de la flor {i+1}: ")]
        flor += [int(input(f"Ingrese la cantidad de {flor[0]}: "))]
        inventario += [flor]


def mostrar_invetario():        
    for item in inventario:
        print("Hay", item[1], "de", item[0])


def main():
    hilo1 = threading.Thread(target=inventario_flores)
    hilo2 = threading.Thread(target=mostrar_invetario)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == '__main__':
    main()