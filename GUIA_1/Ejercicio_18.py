#Ejercicio 18:
"""Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última."""

#SIN FUNCION

palabra = input("ingrese una palabra: ")
palabra = palabra[::-1]             # Da vuelta la palabra

for largo in range(len(palabra)):       #segun longitud de palabra recorre todos los espacios desde el 0
    print(palabra[largo])


#CON FUNCION

palabra = input("ingrese una palabra: ")
palabra = palabra[::-1]                         # Da vuelta la palabra

def caracteres(unstr):
    for largo in range(len(unstr)):           # segun longitud de palabra recorre todos los espacios desde el 0
        print(unstr[largo])

caracteres(palabra)