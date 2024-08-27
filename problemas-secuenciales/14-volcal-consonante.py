# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# VOCAL O CONSONANTE
import threading
caracter = ''
vocales = "aeiou"
lock = threading.Lock()

def identificar_vocal_consonante():
    with lock:
        if caracter.isalpha() and len(caracter) == 1:
            if caracter.lower() in vocales:
                print(f"{caracter} es una vocal.")
            else:
                print(f"{caracter} es una consonante.")
        else:
            print("Ingrese un único carácter alfabético.")

def obtener_datos():
    global caracter
    with lock:
        caracter = input("Ingrese un carácter alfabético: ")


def main():
    hilo1 = threading.Thread(target=obtener_datos)
    hilo2 = threading.Thread(target=identificar_vocal_consonante)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()