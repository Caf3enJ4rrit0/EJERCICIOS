# Ejercicio 15:
"""Crear un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por
entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de
la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18
años debe pagar 500 y si es mayor de 18 años, 1000."""

#SIN FUNCION

edad = int(input("ingrese edad: "))

if edad != 0 and edad > 4:
    if edad <= 18:
        print("La entrada sale $500")
    else:
        print("La entrada sale $1000")
else:
    print("El cliente entra gratis")



#CON FUNCION

edad = int(input("ingrese edad: "))

def entradas(anios):
    if anios!= 0 and anios > 4:
        if anios <= 18:
            print("La entrada sale $500")
        else:
            print("La entrada sale $1000")
    else:
        print("El cliente entra gratis")

entradas(edad)