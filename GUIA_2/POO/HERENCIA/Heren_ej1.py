#Ejercicio 1
"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construir los siguientes métodos para la clase:

● Un constructor, donde los datos pueden estar vacíos.
● mostrar(): Muestra los datos de la persona.
● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""


class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def muestra(self):
        print(f"{self.nombre} \n{self.edad} \n{self.dni}")

    def esMayorDeEdad(self):

        if self.edad <= 18:
            print(bool(self.edad == 0))
        elif self.edad >= 18:
            print(bool(self.edad))



belen = Persona("Belen", 32, 33226854)

belen.muestra()
belen.esMayorDeEdad()


