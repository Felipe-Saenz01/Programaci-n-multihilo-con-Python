# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CONTADOR DE LETRAS DE UNA PALABRA
import threading
contador_letras = {}

def contar_letras():
    palabra = input("Ingrese una palabra: ").lower()
    global contador_letras
    for letra in palabra:
        if letra.isalpha():
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1


def mostrar_contador():    
    print("Contador de letras:", contador_letras)

def main():
    hilo1 = threading.Thread(target=contar_letras)
    hilo2 = threading.Thread(target=mostrar_contador)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()