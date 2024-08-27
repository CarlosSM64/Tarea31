usuarios = []
reservas = []

def menu_inicial():
    while True:
        print("Menú Principal")
        print("1. Registrar un usuario")
        print("2. Reservar un viaje")
        print("3. Ver reservas")
        print("4. Cancelar reservas")
        print("5. Salir")
        
        opcion = input("Seleccione un opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            reservar_viajes()
        elif opcion == "3":
            ver_reservas()
        elif opcion == "4":
            cancelar_reservas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo, por favor")
            
def  registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario para registrarse: ").strip()
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya está registrado.")
    else:
        usuarios.append(nombre_usuario)
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")
        
def reservar_viajes():
    nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
    if nombre_usuario not in usuarios:
        print("El usuario no está registrado. Por favor, regístrese primero.")
        registrar_usuario()
    
    destino = input("Ingrese el destino del viaje: ").strip()
    fecha = input("Ingrese la fecha del viaje (formato YYYY-MM-DD): ").strip()
    
    reservas.append({
        'usuario': nombre_usuario,
        'destino': destino,
        'fecha': fecha
    })
    print(f"Reserva realizada para el usuario '{nombre_usuario}'.")
    
def ver_reservas():
    nombre_usuario = input("Ingrese su nombre de usuario para ver las reservas: ").strip()
    if nombre_usuario not in usuarios:
        print("El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    if not reservas_usuario:
        print("No hay reservas.")
    else:
        print(f"Reservas de {nombre_usuario}:")
        for reserva in reservas_usuario:
            print(f"Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
    
def cancelar_reservas():
    nombre_usuario = input("Ingrese su nombre de usuario para cancelar una reserva: ").strip()
    if nombre_usuario not in usuarios:
        print("El usuario no está registrado.")
        return
    
    reservas_usuario = [reserva for reserva in reservas if reserva['usuario'] == nombre_usuario]
    if not reservas_usuario:
        print("No tiene reservas para cancelar.")
        return
    
    print("Sus reservas:")
    for idx, reserva in enumerate(reservas_usuario):
        print(f"{idx + 1}. Destino: {reserva['destino']}, Fecha: {reserva['fecha']}")
    
    try:
        seleccion = int(input("Ingrese el número de la reserva que desea cancelar: ")) - 1
        if 0 <= seleccion < len(reservas_usuario):
            reserva_a_cancelar = reservas_usuario[seleccion]
            reservas.remove(reserva_a_cancelar)
            print("Reserva cancelada exitosamente.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        
menu_inicial()