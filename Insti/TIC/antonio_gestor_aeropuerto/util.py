import os
import json
from colorama import init, Fore, Style
from time import sleep

init(autoreset=True)

aeropuertos =[] 

vuelos = [
    {"id": "IB101","origen":"Madrid", "destino": "Barcelona", "km": 504, "plazas": 180}, #Madrid => Barcelona -- 1
    {"id": "VY450", "origen": "Barcelona", "destino": "Malaga", "km": 770, "plazas": 160}, #Barcelona => Malaga -- 2
    {"id": "UX333", "origen": "Malaga", "destino": "Madrid", "km": 430, "plazas": 220} #Malaga => Madrid -- 3
]

vuelos_del_usuario = []


                                                               # Retos opcionales
# Editar o eliminar vuelos -- Terminado
# Guardar / cargar aeropurtos y vuelos 'JSON' -- Terminado
# Mostrar estadisticas (vuelo mas largo, promedio de km)
# Colores en la 'CLI' usando el modulo colorama -- Terminado
    #Exitos => Verde
    #Errores => Rojo
    #Inputs => Magenta
    #Info => Amarillo



#Funciones obligatorias

# Terminado
def clear_terminal():
    if os.name == "nt":  
        os.system("cls")
    else:  
        os.system("clear")

# Terminado
def introduce_codigo(msg):
    while True:
        codigo = input(msg)
        existe = False
        for aeropuerto in aeropuertos:
            if aeropuerto['codigo'] == codigo:
                existe = True
                break

        if len(codigo) == 3 and codigo.isalpha() and codigo.isupper() and not existe:
            print(Fore.GREEN + f"El codigo IATA '{codigo}' ha sido añadido")
            return codigo
        elif any(a['codigo'] == codigo for a in aeropuertos):
            print(Fore.RED + "Error: El codigo ya esta en la lista de aerpuertos")
        elif any(a['codigo'] == codigo for a in vuelos):
            print(Fore.RED + "Error: El codigo ya esta en la lista de vuelos")
        elif not codigo.isupper():
            print(Fore.RED + "Error: El codigo debe de estar en mayusculas")
        else:
            print(Fore.RED + "Error: El codigo debe contener solo letras")
 
# Terminada
def nuevo_aeropuerto(lista): #lista = aeropuertos
    codigo = introduce_codigo(Fore.LIGHTMAGENTA_EX + "Código IATA: ") #Funcion anterior (introduce_codigo())

    duplicado = False
    for i in lista: #lista = aeropuertos
        if i["codigo"] == codigo:
            duplicado = True
            break  
    if duplicado:
        print(Fore.RED + f"Error: Ya existe un aeropuerto con el código '{codigo}'.")
        return

    nombre = input(Fore.LIGHTMAGENTA_EX + "Introduce el nombre del aeropuerto: ").strip()
    ciudad = input(Fore.LIGHTMAGENTA_EX + "Introduce la ciudad: ").strip()

    nuevo = {"codigo": codigo, "nombre": nombre, "ciudad": ciudad}

    lista.append(nuevo)
    print(Fore.GREEN + f" Aeropuerto '{nombre}' añadido correctamente.")
    sleep(2)
    clear_terminal()

#Terminado
def nuevo_vuelo(vuelos, aeropuertos):
    id_vuelo = input(Fore.LIGHTMAGENTA_EX + "ID del vuelo: ")

    vuelo = input(Fore.LIGHTMAGENTA_EX + "¿Dónde estás y a dónde quieres ir? (Origen,Destino): ").split(',')
    km = int(input(Fore.LIGHTMAGENTA_EX + "KM'S: "))
    plazas = int(input(Fore.LIGHTMAGENTA_EX + "PLAZAS: "))
    try:
        origen, destino = vuelo
        origen = origen.strip().upper()
        destino = destino.strip().upper()
    except ValueError:
        print(Fore.RED + "Error: Escribe 2 códigos IATA separados por una coma")
        return

    codigos = [n["codigo"] for n in aeropuertos]

    for v in vuelos:
        if v['origen'] == origen and v['destino'] == destino:
            print(Fore.RED + "Error: Este vuelo ya existe")
            return

    vuelo = {"id": id_vuelo, "origen": origen, "destino": destino, "km": km, "plazas": plazas}
    vuelos_del_usuario.append(vuelo)

    # el mensaje 
    mensaje = f"{vuelo['id']}: {vuelo['origen']} => {vuelo['destino']} -- KM'S:{vuelo['km']} PLAZAS:{vuelo['plazas']}"
    ancho = len(mensaje)
    borde_superior = "┌" + "─" * (ancho + 2) + "┐"
    borde_inferior = "└" + "─" * (ancho + 2) + "┘"
    linea_contenido = f"│ {mensaje} │"

    # enseña el marco los cojones
    print(Fore.GREEN + borde_superior)
    print(Fore.GREEN + linea_contenido)
    print(Fore.GREEN + borde_inferior)

    sleep(2)
    clear_terminal()

# Terminado    
def listar_vuelos(vuelos_del_usuario):
    if not vuelos_del_usuario:
        print("No hay vuelos disponibles")

    for i, vuelo in enumerate(vuelos_del_usuario, start=1):
            print(Fore.YELLOW + f"{i}. {vuelo['id']}: {vuelo['origen']} => {vuelo['destino']} -- KM'S:{vuelo['km']} PLAZAS:{vuelo['plazas']}")


    sleep(2)
    clear_terminal()


# Terminado
def buscar_por_aeropuerto(vuelos):
    codigo_a_buscar = input("Código IATA: ").strip()
    vuelos_filtrados = []

    for vuelo in vuelos:
        if vuelo['origen'] == codigo_a_buscar or vuelo['destino'] == codigo_a_buscar:
            vuelos_filtrados.append(vuelo)
        
    if vuelos_filtrados:
        print(Fore.LIGHTMAGENTA_EXMAGENTA + f"Estos son los vuelos con el código: {codigo_a_buscar}")
        for i in vuelos_filtrados:
            print(Fore.YELLOW + f"{i['origen']} => {i['destino']} -- Km: {i['km']}")
        
        sleep(2)
        clear_terminal()
    else:
        print(f"No se encontraron vuelos con el código {codigo_a_buscar}")
        sleep(2)
        clear_terminal()


# Funciones opcionales

# Terminado
def editar_eliminar_vuelos(vuelos):

    for n, i in enumerate(vuelos):
        print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")

    editar = input("¿Que quieres hacer, editar o eliminar?: ").lower()
    if editar == "eliminar":    # Opcion elegida = opción
        vuelo_a_eliminar = int(input("¿Que vuelo quieres eliminar?: "))
        if 0 <= vuelo_a_eliminar < len(vuelos): # Verifica si el numero que ha dado esta dentro de el numero de indices que hay
            del vuelos[vuelo_a_eliminar]
            print(Fore.GREEN + f"El vuelo de a se ha eliminado correctamente")
            for n, i in enumerate(vuelos):
                print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")

        else:
            print(Fore.RED + "Índice no válido")
    elif editar == "editar":    # Opcion elegida = editar
        vuelo_a_editar = int(input("¿Que vuelo quieres editar?: "))
        if 0 <= vuelo_a_editar < len(vuelos): # Verifica si el numero que ha dado esta dentro de el numero de indices que hay
            origen_o_destino = input("¿Origen o destino?: ").lower()

            if origen_o_destino == "origen": # Detecta que parte del vuelo quiere editar Origen/Destino
                while True:
                    origen_nuevo = input("Codigo IATA del nuevo origen: ")
                    if origen_nuevo.isupper() and len(origen_nuevo) == 3 and origen_nuevo.isalpha():# Verifica si el código que ha dado el usuario cumple los requisitos del codigo IATA
                        vuelos[vuelo_a_editar]['origen'] = origen_nuevo
                        print(Fore.CYAN + "Lista de vuelos actualizada: ")
                        break
                    else:
                        print(Fore.RED + "Error: El codigo debe de estar en mayusculas y contener 3 letras")

                for n, i in enumerate(vuelos):
                    print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")

            
            elif origen_o_destino == "destino":
                while True:
                    destino_nuevo = input("Codigo IATA del nuevo destino: ")
                    if destino_nuevo.isupper() and len(destino_nuevo) == 3 and destino_nuevo.isalpha(): #Verifica si el código que ha dado el usuario cumple los requisitos del codigo IATA
                        vuelos[vuelo_a_editar]['destino'] = destino_nuevo
                        print(Fore.CYAN + "Lista de vuelos actualizadas: ")
                        break
                    else:
                        print(Fore.RED + "Error: El codigo debe de estar en mayusculas y contener 3 letras")
                
                for n, i in enumerate(vuelos):
                    print(Fore.YELLOW + f"{n}. {i['origen']} => {i['destino']} -- KM: {i['km']}")


# Terminado
def guardar_datos(aeropuertos, vuelos, archivo="datos.json"):
    datos = {
        "aeropuertos": aeropuertos,
        "vuelos": vuelos
    }
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

#Terminado
def cargar_datos(archivo="datos.json"):

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos.get("aeropuertos", []), datos.get("vuelos", [])
    except FileNotFoundError:
        return [], []
    

#Terminado
def mostrar_estadisticas(vuelos):
    vuelo_km = []
    
    try:
        for i in vuelos:
            vuelo_km.append(i['km']) 

        mas_largo = max(vuelo_km)
        total_km = sum(vuelo_km)
        media_km = total_km / len(vuelo_km)
        
        print(Fore.YELLOW + f"Vuelo mas largo: {mas_largo} km")
        print(Fore.YELLOW + f"Media km: {media_km:.2f}km")
        sleep(2)
        clear_terminal()
    except ValueError:
        print(Fore.RED + "Error: No hay vuelos en la lista")
        return