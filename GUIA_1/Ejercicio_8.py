# Ejercicio 8:
"""Crear un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión."""

#SIN FUNCION

inversion = int(input("ingrese el monto a invertir ($): "))
int_anual = int(input("ingrese el interes anual (%): "))
anos = int(input("ingrese el numero de años: "))

operacion = ((int_anual * inversion)/100) * anos
print()
print(f"{operacion}$ es el capital obtenido en la inversion")

#CON FUNCION

def invierte():
    inversion = int(input("ingrese el monto a invertir ($): "))
    int_anual = int(input("ingrese el interes anual (%): "))
    anos = int(input("ingrese el numero de años: "))

    operacion = ((int_anual * inversion)/100) * anos
    print()
    print(f"${operacion} es el capital obtenido en la inversion")

invierte()

