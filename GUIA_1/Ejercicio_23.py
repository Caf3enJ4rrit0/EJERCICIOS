#Ejercicio 23:
"""Crear un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.

Fruta Precio (kg)
Banana 80
Manzana 100
Pera 50
Naranja 70"""

#SIN FUNCION

stock = {                       # diccionario de los precios de las frutas por Kg
    "banana": 80,
    "manzana": 100,
    "pera": 50,
    "naranja": 70
}

fruta = input("Que fruta quiere?: ")
kilos = int(input("Cuantos kilos quiere?: "))


if fruta in stock:
    pedido = stock[fruta] * kilos
    print(f"El precio de la {fruta} por {kilos}Kg es de ${pedido} Total")
else:
    print(f"La {fruta} no esta en stock")



#CON FUNCION

f = input("Que fruta quiere?: ")
k = int(input("Cuantos kilos quiere?: "))


def mercaderia(fruta, kilos):

    stock = {                       # diccionario de los precios de las frutas por Kg
        "banana": 80,
        "manzana": 100,
        "pera": 50,
        "naranja": 70
    }

    if fruta in stock:
        pedido = stock[fruta] * kilos
        print(f"El precio de la {fruta} por {kilos}Kg es de ${pedido} Total")
    else:
        print(f"La {fruta} no esta en stock")

mercaderia(f, k)