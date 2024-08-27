# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

#  CONTAR SILABAS DE UNA PALABRA
import threading
cantidad_silabas = 0
palabra = ''
letras = []
vocales = "aeiou"
lock = threading.Lock()

def contar_silabas():
    global cantidad_silabas, letras, palabra
    with lock:
        palabra = input("Ingrese una palabra: ").lower()
        for letra in palabra:
            if letra in vocales:
                cantidad_silabas += 1
                letras += [letra]

def mostrar_silabas():
    with lock:
        print("Cantidad de sílabas en la palabra:", cantidad_silabas)
        print(f"Las vocales en la palabra: {palabra} son: {letras}")


def main():
    hilo1 = threading.Thread(target=contar_silabas)
    hilo2 = threading.Thread(target=mostrar_silabas)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()