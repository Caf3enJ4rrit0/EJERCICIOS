# Ejercicio 5:
"""Crear un programa que pregunte el nombre del usuario y después de
que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras."""

#SIN FUNCION

nombre = input("ingrese su nombre: ")
count = 0

for letra in nombre:
    count += 1

print(f"{nombre} tiene {count} letras")

#CON FUNCION

def nom_letra():
    nombre = input("ingrese su nombre: ")
    count = 0

    for letra in nombre:
        count += 1

    print(f"{nombre} tiene {count} letras")

nom_letra()