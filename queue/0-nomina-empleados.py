# NOMINA DE N EMPLEADOS
import threading
import queue


cola = queue.Queue()


def obtener_salario(numero, salario):
    cola.put((numero, salario))


def main():
    num_empleados = int(input("Ingrese el número de empleados: "))
    hilos = []
    nomina_total= 0
    for i in range(num_empleados):
        salario = float(input(f"Ingrese el salario del empleado {i + 1}: "))
        hilo = threading.Thread(target=obtener_salario, args=(i,salario))
        hilos += [hilo]
        hilo.start()


    for hilo in hilos:
        hilo.join()
        num, salario = cola.get()
        print(f"El salario de empleado {num} es: {salario}")
        nomina_total += salario

    print("La nómina total de la empresa es:", nomina_total)


if __name__ == '__main__':
    main()