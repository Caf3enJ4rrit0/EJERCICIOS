#Ejercicio 17:
"""Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""


#SIN FUNCION

num = int(input("ingrese numero para multiplicar: "))

while num != 0 and num < 10:
    for multi in range(11):
        if multi != 0:
            print(f"{num} x {multi}= {num * multi}")
            num + 1
    if multi == 10:
        break


#CON FUNCION

tabla = int(input("ingrese numero para multiplicar: "))

def tablas(num):
    while num != 0 and num < 10:
        for multi in range(11):
            if multi != 0:
                print(f"{num} x {multi}= {num * multi}")
                num + 1
        if multi == 10:
            break
tablas(tabla)