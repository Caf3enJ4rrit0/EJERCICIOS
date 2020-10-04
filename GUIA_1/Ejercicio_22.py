#Ejercicio 22:
"""Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre
por pantalla su producto escalar."""

#SIN FUNCION

v1 = (1,2,3)
v2 = (-1,0,2)

prod_esc = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])

print(f"El producto escalar de los Vectores {v1} y {v2} es {prod_esc}.")


#CON FUNCION

v1 = (1,2,3)
v2 = (-1,0,2)

def escalar(vector1, vector2):
    prod_esc = (vector1[0] * vector2[0]) + (vector1[1] * vector2[1]) + (vector1[2] * vector2[2])

    print(f"El producto escalar de los Vectores {v1} y {v2} es {prod_esc}.")


escalar(v1, v2)
