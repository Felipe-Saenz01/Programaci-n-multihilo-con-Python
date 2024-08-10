# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

# CALCULAR RAIZ A LA N
import math

def calcular_raiz():
    numero = float(input("Ingrese el número: "))
    exponente = float(input("Ingrese el exponente (raíz): "))
    resultado = math.pow(numero, 1/exponente)
    print(f"La raíz {exponente}-ésima de {numero} es:", resultado)

def main():
    calcular_raiz()

if __name__ == "__main__":
    main()