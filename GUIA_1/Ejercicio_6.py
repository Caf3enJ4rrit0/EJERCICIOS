# Ejercicio 6:
"""Crear un programa que realice la siguiente operación aritmética [(3+2)/2*5]2 .
Mostrar el resultado por pantalla."""

#SIN FUNCION

suma = 3+2
division = suma / 2
multiplicacion = division * 5
resultado = multiplicacion ** 2

print(resultado)


"""
# OTRA OPCION
resultado = ((3+2)/2*5)**2
print(resultado)
"""

#CON FUNCION

def operaciom(a,b,c,d):
    suma = a + b
    division = suma / c
    multiplicacion = division * d
    resultado = pow(multiplicacion, 2)
    print(resultado)
    return resultado

operaciom(3,2,2,5)


"""
# OTRA OPCION
def operaciom():
    suma = 3+2
    division = suma / 2
    multiplicacion = division * 5
    resultado = multiplicacion ** 2
    print(resultado)
    return resultado
"""



