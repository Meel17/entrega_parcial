def cargar_pacientes(pacientes):
    cantidad = int(input("Ingrese la cantidad de pacientes a cargar: "))
    for _ in range(cantidad):
        historia_clinica = int(input("Ingrese número de historia clínica: "))
        nombre = input("Ingrese nombre del paciente: ")
        edad = int(input("Ingrese edad del paciente: "))
        diagnostico = input("Ingrese diagnóstico: ")
        dias_internacion = int(input("Ingrese cantidad de días de internación: "))
        
        # Agregar el paciente a la lista
        
        pacientes.append([historia_clinica, nombre, edad, diagnostico, dias_internacion])
    
    print(f"{cantidad} pacientes cargados exitosamente.")



def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return 
    
    print("*** Lista de Pacientes ***")
    for paciente in pacientes:
        print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, "
              f"Diagnóstico: {paciente[3]}, Días de Internación: {paciente[4]}")
    return pacientes


def buscar_paciente(pacientes, historia_clinica):
    """Busca un paciente por su número de historia clínica y muestra sus datos."""
    for paciente in range(len(pacientes)):
        if paciente[0] == historia_clinica:  # Compara con el número de historia clínica
            print(f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, "
                  f"Diagnóstico: {paciente[3]}, Días de Internación: {paciente[4]}")
            return  paciente
    return None
    # Si no se encontró al paciente
def ordenar_pacientes(pacientes):
    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) -i -1):
            if pacientes[j][i] > pacientes [j + 1][1]: # SI LO QUERES ORDENAR DE MANERA DESCENDENTE DAS VUELTA ">"
               tem = pacientes[+1]
               pacientes[j + 1] = pacientes[j]
               pacientes[j] = tem

    print("Pacientes ordenados por precio de forma ascendente: ")
    for paciente in pacientes:
        (f"Historia Clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, "
         f"Diagnóstico: {paciente[3]}, Días de Internación: {paciente[4]}")
    return pacientes

def mostrar_max(pacientes):
    if not pacientes:
        print("No hay pacientes registrados!.")
        return
    max_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[1] > max_paciente[1]:
            max_paciente = paciente
        print(f"El paciente con mas dias de internacion: {paciente[max_paciente]}" 
              f"Historia Clinica: {paciente[1]}, Nombre: {paciente[2]}, Edad: {paciente[3]}" 
            f"Diagnóstico: {paciente[4]}, Días de Internación: {paciente[5]}")

def mostrar_min(pacientes):
    if not pacientes:
        print("No hay pacientes registrados!.")
        return
    min_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[1] < min_paciente[1]:
            min_paciente = paciente
    print(f"El paciente con menos dias de internacion: {min_paciente}"
          f"Historia Clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}"
          f"Diagnóstico: {paciente[3]}, Días de Internación: {paciente[4]}")


def contar_pacientes_mas_dias(pacientes):
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:  # Comprobamos si los días de internación son mayores a 5
            contador += 1
    print(f"Número de pacientes con más de 5 días de internación: {contador}")

def promedio_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    total_dias = 0
    contador = 0  # Contador para el número de pacientes

    for paciente in pacientes:
        total_dias += paciente[4]  # Sumar los días de internación
        contador += 1  #contador por cada paciente

    promedio = total_dias / contador  # Calcular el promedio
  
    print(f"El promedio de días de internación es: {promedio} días")

def menu():
    pacientes = []
    salir = ""


    while salir != "salir":
        print("----- Menú de Gestión de Pacientes -----")
        print("1. Cargar pacientes")
        print("2. Mostrar todos los pacientes")
        print("3. Buscar paciente por numero de Historia clinica")
        print("4. Ordenar pacientes  por numero de Historia clinica")
        print("5. Mostrar paciente con mas dias de internacion")
        print("6. Mostrar paciente con menos dias de internacion")
        print("7. Cantidad de pacientes con mas de 5 dias de internacion")
        print("8. Promedio de dia de internacion de todos los pacientes")
        print("6. Salir")
        opcion = input("Seleccione una opcion")


        if opcion == '1':
            pacientes = cargar_pacientes(pacientes)
        elif opcion == '2':
            nombre_paciente = input("Ingrese el nombre del paciente a buscar: ")
            paciente = buscar_paciente(pacientes, nombre_paciente)
            if paciente:
                print(f"Producto encontrado: {paciente}")
            else:
                print("Paciente no encontrado!!")
        elif opcion == '3':
            pacientes = ordenar_pacientes(pacientes)
        elif opcion == '4':
            mostrar_max(pacientes)
        elif opcion == '5':
            mostrar_min(pacientes)
        elif opcion == "6":
           ordenar_pacientes(pacientes)
        elif opcion == "7":
           contar_pacientes_mas_dias(pacientes)
        elif opcion == "8":
            promedio_dias_internacion(pacientes)
        elif opcion == '9':
            print("Saliendo...!")
            salir = "salir"
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

# menu()