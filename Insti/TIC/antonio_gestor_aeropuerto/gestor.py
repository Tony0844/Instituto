from os import system
from time import sleep
from colorama import init, Fore
from util import guardar_datos, cargar_datos
import util
if system("cls") !=0: system("clear")
init(autoreset=True)


while True:
    print(Fore.BLUE + "_____________________   _______________   __________________")
    print(Fore.BLUE + "||1-Añadir aeropuerto || 2-Añadir vuelo || 3-Listar vuelos||")
    print(Fore.BLUE + "---------------------   ---------------   ------------------")
    print(Fore.BLUE + "_________________________________  ___________________________")
    print(Fore.BLUE + "||4-Buscar vuelos por aeropuerto ||5-Editar o eliminar vuelos|| ")
    print(Fore.BLUE + "---------------------------------  ---------------------------")
    print(Fore.BLUE + "__________________________________________  ________________________")
    print(Fore.BLUE + "||6-Guardar / cargar aeropuertos y vuelos || 7-Mostrar estadísticas||")
    print(Fore.BLUE + "------------------------------------------  ------------------------")
    print(Fore.BLUE + "___________")
    print(Fore.BLUE + "||8-Salir||")
    print(Fore.BLUE + "-----------")

    op = int(input(Fore.WHITE + "Opción: "))
    if op == 1: # 1 opción
        util.nuevo_aeropuerto(util.aeropuertos)

    elif op == 2: # 2 opción
        util.nuevo_vuelo(util.vuelos, util.aeropuertos)

    elif op == 3: # 3 opción
        print("\n")
        print(Fore.BLUE + "Vuelos")
        print(Fore.BLUE + "------")
        util.listar_vuelos(util.vuelos_del_usuario)

    elif op == 4: # 4 opción
        util.buscar_por_aeropuerto(util.vuelos_del_usuario)

    elif op == 5: # 5 opción
        util.editar_eliminar_vuelos(util.vuelos_del_usuario)
        guardar_datos(util.aeropuertos, util.vuelos)

    elif op == 6: # 6 opción
        print("1. Guardar datos")
        print("2. Cargar datos")
        opcion_sec = input(Fore.LIGHTMAGENTA_EX + "Elige una opción: ")

        if opcion_sec == "1":
            guardar_datos(util.aeropuertos, util.vuelos_del_usuario)
            print(Fore.GREEN + "Datos guardados correctamente.")
        elif opcion_sec == "2":
            util.aeropuertos, util.vuelos_del_usuario = cargar_datos()
            print(Fore.GREEN + "Datos cargados correctamente.")
        else:
            print(Fore.RED + "Error: Opción inválida.")
        sleep(1)

    elif op ==7: # 7 opción
        util.mostrar_estadisticas(util.vuelos_del_usuario)

    elif op == 8: #8 opción
        util.clear_terminal() #Limpia la terminal
        print("Cerrando gestor.")
        sleep(0.5)
        util.clear_terminal()
        print("Cerrando gestor..")
        sleep(0.5)
        util.clear_terminal()
        print("Cerrando gestor...")
        sleep(0.5)
        util.clear_terminal()
        break
