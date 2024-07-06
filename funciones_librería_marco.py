
# Validar texto
def validar_texto(texto):
    return texto.isalpha()

# Función para registrar un préstamo
def registrar_prestamo(prestamos):
    # Ciclo para asegurar que sean letras
    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if validar_texto(nombre):
            break
        else:
            print("El nombre solo debe contener letras.")

    # Ciclo para asegurar que sean letras
    while True:
        apellido = input("Ingrese el apellido del cliente: ")
        if validar_texto(apellido):
            break
        else:
            print("El apellido solo debe contener letras.")
    
    id_libro = input("Ingrese el ID del Libro: ")
    fecha_prestamo = input("Ingrese la fecha del préstamo: ")
    fecha_devolucion = input("Ingrese la fecha de devolución: ")        

    # Se crea el diccionario de prestamos y se van agregando los prestamos
    prestamo = {
        'nombre': nombre,
        'apellido': apellido,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion': fecha_devolucion,
    }
    
    prestamos.append(prestamo)
    print("Préstamo registrado exitosamente.")

# Función para listar todos los préstamos
def listar_prestamos(prestamos):
    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for prestamo in prestamos:
        print("Recibo de préstamo")
        print(f"Nombre: {prestamo['nombre']} {prestamo['apellido']}")
        print(f"ID del libro: {prestamo['id_libro']}")
        print(f"Fecha de préstamo: {prestamo['fecha_prestamo']}")
        print(f"Fecha de devolución: {prestamo['fecha_devolucion']}")
        print("")

# Función para imprimir el recibo de préstamo
def imprimir_recibo_de_prestamo(prestamos):
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    
    id_libro = input("Ingrese el ID del libro para generar el recibo: ")
    prestamos_id_libro = [prestamo for prestamo in prestamos if prestamo['id_libro'] == id_libro]
    
    if not prestamos_id_libro:
        print(f"No hay préstamos registrados para el ID del libro {id_libro}.")
        return

    # Se escribe en el archivo de texto
    with open(f"recibo_prestamo_{id_libro}.txt", "w") as file:
        for prestamo in prestamos_id_libro:
            file.write("Recibo de préstamo\n")
            file.write(f"Nombre: {prestamo['nombre']} {prestamo['apellido']}\n")
            file.write(f"ID del libro: {prestamo['id_libro']}\n")
            file.write(f"Fecha de préstamo: {prestamo['fecha_prestamo']}\n")
            file.write(f"Fecha de devolución: {prestamo['fecha_devolucion']}\n")
            file.write("\n")
    
    print(f"Recibo de préstamo para el libro {id_libro} generado exitosamente.")

# Función para salir del programa
def salir():
    print("Saliendo del programa. Adiooooos...")
