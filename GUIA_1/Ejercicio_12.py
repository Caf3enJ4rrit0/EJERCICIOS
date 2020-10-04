#Ejercicio 12:
"""Crear un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede
dividir por 0."""

#SIN FUNCION

dividendo = int(input("ingrese un numero: "))
divisor = int(input("ingrese otro numero: "))

if divisor == 0:
    print("NO se puede dividir")
else:
    cociente = dividendo / divisor
    print(f"{dividendo}/{divisor} = {cociente}")


#CON FUNCION

dividendo = int(input("ingrese un numero: "))
divisor = int(input("ingrese otro numero: "))

def divide(num1, num2):
    if num1 == 0 and num2 == 0:
        print("NO se puede dividir")
    else:
        cociente = num1 / num2
        print(f"{num1}/{num2} = {cociente}")
        return cociente

divide(dividendo, divisor)

"""
div = divide(dividendo, divisor)            # Almacenando lo que devuelve el metodo en una variable

print(div)                                  # imprimiendo la variable

"""