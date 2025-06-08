from os import system
from time import sleep
if system("cls") !=0: system("clear")


#1.Haz un timer que haga una cuenta atras de 10 a 0

print("Actividad 1")
print("-----------")
timer = 11
while timer <= 10 or timer >= 10:
    timer -= 1
    sleep(1)
    print(f"{timer}s")
    if timer == 0:
        print(timer)
        break #Justo antes de salir del bucle no se porque printea un 0

#2.Haz un programa que printee los numeros del 1 al 10

print("Actividad 2")
print("-----------")

for i in range(11):
    print(f"-  {i}")


#3.Pidele al usuario un numero del 1 al 10, y con el que te de haz su tabla de multiplicar
print("Actividad 3")
print("-----------")

print("Método 1")

    #1º Método que se me ha ocurrido
user_number = int(input("Dame un número del 1 al 10: \n"))
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    result = user_number * i
    print(f"{user_number} x {i} = {result}")
    
    
print("\n")

#2º Método
print("Método 2")
user_number = int(input("Dame un número del 1 al 10:\n"))

for i in range(11):
    print(f"{user_number} x {i} = {user_number * i}")




#4.Pidele al usuario una contrasña y haz que no sea corrwcta hasta que ponga 'abc123'
print("\n")
print("Actividad 4")
print("-----------")
password = "abc123"
user_pass = input("Dame una contraseña: \n")

while user_pass != "abc123":
    print("La contraseña no es correcta")
    user_pass = input("Dame una contraseña: \n")
else:
    print(f"La contraseña '{password}' es correcta!")
