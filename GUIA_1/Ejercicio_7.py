# Ejercicio 7:
"""Crear un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m>
da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c>
y <r> son el cociente y el resto de la división entera respectivamente."""

#SIN FUNCION

n = int(input("ingrese un numero: "))
m = int(input("ingrese otro numero: "))

cociente = n // m
resto = n - (cociente * m)


print()
print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")


#CON FUNCION

def div():
    n = int(input("ingrese un numero: "))
    m = int(input("ingrese otro numero: "))

    cociente = n // m                   # devuelve el cociente
    resto = n - (cociente * m)          # r = n % m    -------> el modulo devuelve el resto

    print()
    print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")


div()




