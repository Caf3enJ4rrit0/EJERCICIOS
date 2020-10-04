#Ejercicio 19:
"""Crear un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase."""

#SIN FUNCION

frase = input("Ingrese una Frase: ")
letra = input("Ingrese una Letra: ")
contador = 0

for caracter in frase:
        if caracter == letra:
            contador += 1

print(f"La letra {letra} se repite {contador} veces en la frase")


#CON FUNCION

frase = input("Ingrese una Frase: ")
letra = input("Ingrese una Letra: ")


def veces(oracion, ltr):
    contador = 0
    for caracter in oracion:
        if caracter == ltr:
            contador += 1

    print(f"La letra {ltr} se repite {contador} veces en la frase")

veces(frase, letra)

