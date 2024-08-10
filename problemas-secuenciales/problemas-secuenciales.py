# Programacion en red y multihilo
# Desarrollar los ejercicios contenidos en el documento adjunto, 
# de la forma estructurada, como se socializo en clase.

import math

# NOMINA DE N EMPLEADOS
def calcular_nomina():
    n = int(input("Ingrese el número de empleados: "))
    nomina_total = 0
    for i in range(n):
        salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
        nomina_total += salario
    print("La nómina total de la empresa es:", nomina_total)


# INVENTARIO
def inventario_flores():
    inventario = []
    n = int(input("Ingrese el número de tipos de flores en el inventario: "))
    for i in range(n):
        flor= []
        flor += [input(f"Ingrese el nombre de la flor {i+1}: ")]
        flor += [int(input(f"Ingrese la cantidad de {flor[0]}: "))]
        inventario += [flor]
        
    for item in inventario:
        print("Hay", item[1], "de", item[0])


# CALCULAR RAIZ A LA N

def calcular_raiz():
    numero = float(input("Ingrese el número: "))
    exponente = float(input("Ingrese el exponente (raíz): "))
    # resultado = math.pow(numero, 1/exponente)
    resultado = numero ** (1/exponente)
    print(f"La raíz {exponente}-ésima de {numero} es:", resultado)


# AREA DE UN CIRCULO

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * (math.pow(radio, 2))
    print("El área del círculo es:", area)


# AREA DE UN ROMBO
def calcular_area_rombo():
    diagonal1 = float(input("Ingrese la longitud de la primera diagonal: "))
    diagonal2 = float(input("Ingrese la longitud de la segunda diagonal: "))
    area = (diagonal1 * diagonal2) / 2
    print("El área del rombo es:", area)


# HALLAR SENO, COSENO Y TANGENTE

def calcular_trigonometricas():
    angulo = float(input("Ingrese el ángulo en grados: "))
    radianes = math.radians(angulo)
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)
    print(f"Seno: {seno}, Coseno: {coseno}, Tangente: {tangente}")


# ORDENAR NUMERO DE MAYOR A MENOR
def ordenar_numeros():
    n = int(input("Ingrese el número de elementos: "))
    numeros = []
    for i in range(n):
        numero = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
    numeros.sort(reverse=True)
    print("Números ordenados de mayor a menor:", numeros)


# HALLAR NUMERO PRIMOS Y PARES
def numeros_primos_pares():
    rango = int(input("Ingrese el rango de números: "))
    primos = []
    pares = []
    for num in range(2, rango + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primos.append(num)
        if num % 2 == 0:
            pares.append(num)
    print("Números primos:", primos)
    print("Números pares:", pares)


# LOGARITMO NATURAL

def calcular_logaritmo():
    numero = float(input("Ingrese el número: "))
    logaritmo = math.log(numero)
    print("El logaritmo natural de", numero, "es:", logaritmo)


# CONTAR 2 EN 2
def contar_dos_en_dos():
    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))
    contador = 0
    for num in range(inicio, fin + 1, 2):
        contador += 1
    print("Cantidad de números de 2 en 2:", contador)


#  CONTAR SILABAS DE UNA PALABRA
def contar_silabas():
    palabra = input("Ingrese una palabra: ").lower()
    vocales = "aeiou"
    cantidad_silabas = 0
    for letra in palabra:
        if letra in vocales:
            cantidad_silabas += 1
    print("Cantidad de sílabas en la palabra:", cantidad_silabas)


# CONTADOR DE LETRAS DE UNA PALABRA
def contar_letras():
    palabra = input("Ingrese una palabra: ").lower()
    contador_letras = {}
    for letra in palabra:
        if letra.isalpha():
            if letra in contador_letras:
                contador_letras[letra] += 1
            else:
                contador_letras[letra] = 1
    print("Contador de letras:", contador_letras)


#  CONVERSOR DE PEASO A DOLARES Y EUROS
def convertir_pesos():
    cantidad_pesos = float(input("Ingrese la cantidad en pesos: "))
    tasa_dolar = 0.047  # Tasa de cambio de pesos a dólares
    tasa_euro = 0.039  # Tasa de cambio de pesos a euros
    cantidad_dolares = cantidad_pesos * tasa_dolar
    cantidad_euros = cantidad_pesos * tasa_euro
    print(f"{cantidad_pesos} pesos equivalen a {cantidad_dolares} dólares y {cantidad_euros} euros.")


# CONVERSOR DE MM A CM Y MTS
def convertir_milimetros():
    cantidad_milimetros = float(input("Ingrese la longitud en milímetros: "))
    cantidad_centimetros = cantidad_milimetros / 10
    cantidad_metros = cantidad_milimetros / 1000
    print(f"{cantidad_milimetros} milímetros equivalen a {cantidad_centimetros} centímetros y {cantidad_metros} metros.")

# convertir_milimetros()

# VOCAL O CONSONANTE
def identificar_vocal_consonante():
    caracter = input("Ingrese un carácter alfabético: ")
    vocales = "aeiou"
    if caracter.isalpha() and len(caracter) == 1:
        if caracter.lower() in vocales:
            print(f"{caracter} es una vocal.")
        else:
            print(f"{caracter} es una consonante.")
    else:
        print("Ingrese un único carácter alfabético.")

# identificar_vocal_consonante(caracter)

def menu():
    print("\n|----------------------------------------------------|")
    print("Seleccione una opción:")
    print("1. Calcular nómina")
    print("2. Inventario de flores")
    print("3. Calcular raíz a la n")
    print("4. Calcular área de un círculo")
    print("5. Calcular área de un rombo")
    print("6. Hallar seno, coseno y tangente")
    print("7. Ordenar números de mayor a menor")
    print("8. Hallar números primos y pares")
    print("9. Calcular logaritmo natural")
    print("10. Contar números de 2 en 2")
    print("11. Contar sílabas de una palabra")
    print("12. Contar letras de una palabra")
    print("13. Convertir pesos a dólares y euros")
    print("14. Convertir milímetros a centímetros y metros")
    print("15. Identificar vocal o consonante")
    print("0. Salir")
    print("|----------------------------------------------------|\n")

def main():
    while True:
        menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            calcular_nomina()
        elif opcion == "2":
            inventario_flores()
        elif opcion == "3":
            calcular_raiz()
        elif opcion == "4":
            calcular_area_circulo()
        elif opcion == "5":
            calcular_area_rombo()
        elif opcion == "6":
            calcular_trigonometricas()
        elif opcion == "7":
            ordenar_numeros()
        elif opcion == "8":
            numeros_primos_pares()
        elif opcion == "9":
            calcular_logaritmo()
        elif opcion == "10":
            contar_dos_en_dos()
        elif opcion == "11":
            contar_silabas()
        elif opcion == "12":
            contar_letras()
        elif opcion == "13":
            convertir_pesos()
        elif opcion == "14":
            convertir_milimetros()
        elif opcion == "15":
            identificar_vocal_consonante()
        elif opcion == "0":
            print("Chao :D")
            break
        else:
            print("La opción no corresponde a alguna mensionada.")

if __name__ == "__main__" :
    print('hola bom dia')
    main()