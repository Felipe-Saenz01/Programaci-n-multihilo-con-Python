# NOMINA DE N EMPLEADOS
import threading

num_empleados=0
nomina_total = 0
lock = threading.Lock()

def calcular_nomina():
    global nomina_total
    with lock:
        for i in range(num_empleados):
            salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
            nomina_total += salario

def obtener_datos():
    global num_empleados
    with lock:
        num_empleados = int(input("Ingrese el número de empleados: "))

def mostrar_nomina():
    print("La nómina total de la empresa es:", nomina_total)


def main():
    hilo1 = threading.Thread(target=obtener_datos)
    hilo2 = threading.Thread(target=calcular_nomina)
    hilo3 = threading.Thread(target=mostrar_nomina)
    hilo1.start()
    hilo1.join()
    hilo2.start()
    hilo2.join()
    hilo3.start()
    hilo3.join()

if __name__ == '__main__':
    main()