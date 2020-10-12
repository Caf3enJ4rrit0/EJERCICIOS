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


# ARREGLAR!!!!!

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def muestra(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")



class Cuenta:
    def __init__(self, titular_nombre, titular_edad, titular_dni, cantidad = 0):
        self.tit_nom = titular_nombre                      #clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) NO ME SALE
        self.tit_edad = titular_edad
        self.tit_dni = titular_dni
        self.__cantidad = cantidad


    def mostrar(self):
        print(f"DATOS TITULAR: \nNOMBRE COMPLETO: {self.tit_nom}, \nEDAD: {self.tit_edad}, \nDNI:{self.tit_dni}")
        print(f"SALDO: ${self.__cantidad}")

    def ingresar(self):
        ingresa = int(input("Desea ingresar dinero a la cuenta? S=1/N=0: "))
        if ingresa == 1:
            monto = int(input("ingresar el monto a depositar: "))
            if monto != 0:
                self.__cantidad += monto
            elif monto == 0:
                print("no ingreso un monto invalido")
                print(ingresa)
        elif ingresa == 0:
            print("gracias por usar nuestros servicios")
        elif ingresa != 1 and ingresa != 0:
            print("error")

    def retirar(self):
        retira = int(input("Desea retirar dinero de la cuenta? S=1/N=0: "))
        if retira == 1:
            valor = int(input("ingresar el monto a retirar: "))
            if valor != 0:
                self.__cantidad -= valor
                if self.__cantidad < 0:
                    print("la cuenta esta en numeros rojos")
                    print(f"Su saldo: {self.__cantidad}")
            elif valor == 0:
                print("no ingreso un monto invalido")
                print(retira)
        elif retira == 0:
            print("gracias por usar nuestros servicios")
        elif ingresa != 1 and ingresa != 0:
            print("error")

t_nom = input("ingrese su nombre completo: ")
t_edad = int(input("ingrese su edad: "))
t_dni = int(input("ingrese su dni: "))

alguien = Persona(t_nom, t_edad, t_dni)                             #Objeto de Persona

p = Cuenta(alguien.nombre, alguien.edad, alguien.dni)               #objeto de Cuenta

p.mostrar()
p.ingresar()
p.mostrar()
p.retirar()
p.mostrar()




"""belen = Cuenta(titular., 20000)


belen.mostrar()
belen.ingresar()
belen.mostrar()
belen.retirar()
"""
