# Ejercicio 4:
"""Crear un programa que pregunte el nombre del usuario y un número entero e imprima
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

#SIN FUNCION

nombre = input("ingrese nombre de usuario: ")
num_ent = int(input("ingrese numero entero: "))

for i in range(num_ent):
    print(nombre)


#CON FUNCION

def repetir_nom():
    nombre = input("ingrese nombre de usuario: ")
    num_ent = int(input("ingrese numero entero: "))

    for i in range(num_ent):
        print(nombre)

repetir_nom()
