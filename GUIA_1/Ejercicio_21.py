#Ejercicio 21:
"""Crear un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla
el mensaje “Yo estudio <asignatura>”, donde <asignatura> es cada una de las
asignaturas de la lista."""

#SIN FUNCION

asignatura = ("Matemáticas", "Física", "Química", "Historia", "Lengua")         #Lista

for lista in asignatura:
    print(f"Yo estudio {lista}")


#CON FUNCION

def materia():
    asignatura = ("Matemáticas", "Física", "Química", "Historia", "Lengua")         #Lista
    for lista in asignatura:
        print(f"Yo estudio {lista}")

materia()





