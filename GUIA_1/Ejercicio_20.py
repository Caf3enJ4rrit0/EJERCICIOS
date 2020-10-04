#Ejercicio 20:
"""Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que
el usuario escriba “salir” que terminará."""

#SIN FUNCION

eco = input("Escriba algo: ")
salir = "salir"

while eco != salir:
    print(eco)
    eco = input("Escriba algo: ")
    if eco == salir:
        break

#CON FUNCION

intro = input("Escriba algo: ")

def ecos(eco):
    salir = "salir"
    while eco != salir:
        print(eco)
        eco = input("Escriba algo: ")
        if eco == salir:
            break
ecos(intro)
