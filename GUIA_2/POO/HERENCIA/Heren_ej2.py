#Ejercicio 2
"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Construir los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● El atributo no se puede modificar directamente, sólo ingresando o retirando
dinero.
● mostrar(): Muestra los datos de la cuenta.
● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida
es negativa, no se hará nada.
● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
números rojos.
"""

class Cuenta:
    def __init__(self, titular,):
