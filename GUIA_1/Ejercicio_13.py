# Ejercicio 13:
"""Crear un programa que pida al usuario un número entero y
muestre por pantalla si es par o impar."""

#SIN FUNCION

num = int(input("Ingrese un numero: "))

if num != 0 and num > 0:
    if num % 2 == 0:
        print ("este numero es par")
    else:
        print("este numero es impar")
else:
    print("ingrese valor mayor a 0")


#CON FUNCION

num = int(input("Ingrese un numero: "))

def par_imp(valor):
    if valor != 0 and valor > 0:
        if valor.__mod__(2) == 0:                   # Devuelve el resto
            print ("este numero es par")
        else:
            print("este numero es impar")
    else:
        print("ingrese valor mayor a 0")

par_imp(num)