#Ejercicio 25:
"""Crear un programa que, a partir de una lista con todas las letras del abecedario, haga
un copia y borre de esta última todas las vocales. Luego imprimir por pantalla ambas
listas, la completa y la sin vocales.
Para crear la lista del abecedario se puede importar la variable ascii_lowercase del
módulo string"""

#SIN FUNCION

from string import ascii_lowercase

lista_abc = list(ascii_lowercase)
lista2 = lista_abc.copy()
voc = ("a", "e", "i", "o", "u")

for f in lista2:
    for a in voc:
        if f == a:
            lista2.remove(a)

print(lista_abc)
print(lista2)



#CON FUNCION

from string import ascii_lowercase

lista_abc = list(ascii_lowercase)
lista2 = lista_abc.copy()

def abc(abcedario):
    voc = ("a", "e", "i", "o", "u")

    for f in abcedario:
        for a in voc:
            if f == a:
                abcedario.remove(a)
    print(lista_abc)
    print(abcedario)

abc(lista2)
