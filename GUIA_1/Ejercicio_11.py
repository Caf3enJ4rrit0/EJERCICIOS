#Ejercicio 11:
"""Crear un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable."""

#SIN FUNCION

password = input("ingrese contraseña: ")

pass_baul = "C0ntr4s3ñ4"

if password == pass_baul:
    print("Contraseña correcta")
else:
    print("La contraseña no coincide")


"""
# OTRA OPCION

baul = input("ingrese su nueva contraseña: ")
if baul != 0:
    print("Contraseña guardada")
    password = input("ingrese contraseña: ")
    if password == baul:
        print("Contraseña correcta")
    else:
        print("La contraseña no coincide")
else:
    print("La contraseña NO se guardo")
"""

#CON FUNCION

password = input("ingrese contraseña: ")

def passw(caracter):
    pass_baul = "C0ntr4s3ñ4"
    if caracter == pass_baul:
        print("Contraseña correcta")
    else:
        print("La contraseña no coincide")

passw(password)






