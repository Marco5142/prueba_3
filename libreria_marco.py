
# Importar las funciones desde el archivo de funciones_librería_marco.py
from funciones_librería_marco import registrar_prestamo, listar_prestamos, imprimir_recibo_de_prestamo, salir

# Lista para almacenar los préstamos
prestamos = []

# Menú principal
while True:
    print("\nSistema de Gestión de Préstamos")
    print("1. Registrar préstamo")
    print("2. Listar todos los préstamos")
    print("3. Imprimir recibo de préstamo")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_prestamo(prestamos)
    elif opcion == '2':
        listar_prestamos(prestamos)
    elif opcion == '3':
        imprimir_recibo_de_prestamo(prestamos)
    elif opcion == '4':
        salir()
        break
    else:
        print("Opción no válida. Intente de nuevo.")
