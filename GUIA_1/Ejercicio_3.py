# Ejercicio 3:
"""Crear un programa que pida al usuario nombre y edad
e imprima dichos datos en renglones distintos."""

#SIN FUNCION

nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")

print(f" mi nombre es {nombre} y\n mi edad es: {edad}")


#CON FUNCION

def persona():
    nombre = input("ingrese su nombre: ")
    edad = input("ingrese su edad: ")

    print(f" mi nombre es {nombre} y\n mi edad es: {edad}")

persona()