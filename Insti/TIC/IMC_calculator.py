from os import system
if system("clear") != 0: system("cls")


def imc_calculation():
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))

    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc}")


    if imc <= 18.5:
        print("Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidad 1")
    elif imc >= 35 and imc <= 39.9:
        print("Obesidad 2")
    elif imc >= 40:
        print("Obesidad 3")

imc_calculation()


seguir = input("¿Quieres seguir calculando? (Y / N): \n").lower()
while seguir == "y":
    imc_calculation()
    seguir = input("¿Quieres seguir calculando? (Y / N): \n").lower()

exit()