# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CONVERSOR DE MM A CM Y MTS
import threading
milimetros = 0


def convertir_milimetros():
    print(f"{milimetros} milímetros equivalen a {milimetros/10} centímetros y {milimetros/1000} metros.")


def obtener_datos():
    global milimetros
    milimetros = float(input("Ingrese la longitud en milímetros: "))


def main():
    hilo1 = threading.Thread(target=obtener_datos)
    hilo2 = threading.Thread(target=convertir_milimetros)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()

if __name__ == "__main__":
    main()