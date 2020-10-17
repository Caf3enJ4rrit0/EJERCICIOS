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

"""class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def muestra(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

class Cuenta:
    def __init__(self, titular_nombre, titular_edad, titular_dni, cantidad = 0):
        self.tt_nom = titular_nombre
        self.tt_edad = titular_edad
        self.__tt_dni = titular_dni
        self.__cantidad = cantidad


    def mostrar(self):
        print(f"DATOS TITULAR: \nNOMBRE COMPLETO: {self.tt_nom}, \nEDAD: {self.tt_edad}, \nDNI:{self.__tt_dni}")
        print(f"SALDO: ${self.__cantidad}")

    def ingresar(self, monto):
        if monto != 0 and monto >= 0:
            self.__cantidad += monto
        elif monto == 0:
            print("no ingreso un monto valido")
        elif monto < 0:
            self.__cantidad = 0

    def retirar(self, valor):
        if valor != 0:
            self.__cantidad -= valor
            if self.__cantidad < 0:
                print("la cuenta esta en numeros rojos")
                print(f"Su saldo: {self.__cantidad}")
        elif valor == 0:
            print("no ingreso un monto invalido")"""

"""    def ingresar(self):
        ingresa = input("Desea ingresar dinero a la cuenta? s/n: ")
        if ingresa == "s":
            monto = float(input("ingresar el monto a depositar: "))
            if monto != 0 and monto >= 0:
                self.__cantidad += monto
            elif monto == 0:
                print("no ingreso un monto valido")
            elif monto < 0:
                self.__cantidad = 0                
        elif ingresa == "n":
            print("gracias por usar nuestros servicios")
        elif ingresa != "s" and ingresa != "n":
            print("error")


    def retirar(self):
        retira = input("Desea retirar dinero de la cuenta? s/n: ")
        if retira == "s":
            valor = float(input("ingresar el monto a retirar: "))
            if valor != 0:
                self.__cantidad -= valor
                if self.__cantidad < 0:
                    print("la cuenta esta en numeros rojos")
                    print(f"Su saldo: {self.__cantidad}")
            elif valor == 0:
                print("no ingreso un monto invalido")
        elif retira == "n":
            print("gracias por usar nuestros servicios")
        elif ingresa != "s" and ingresa != "n":
            print("error")"""

"""t_nom = input("ingrese su nombre completo: ")
t_edad = int(input("ingrese su edad: "))
t_dni = int(input("ingrese su dni: "))

alguien = Persona(t_nom, t_edad, t_dni)                                 #Objeto de Persona

p = Cuenta(alguien.nombre, alguien.edad, alguien.dni)                   #objeto de Cuenta

p.mostrar()
print()

cantidad_d = float(input("ingresar el monto a depositar: "))
p.ingresar(cantidad_d)
print()

p.mostrar()
print()

cantidad_r = float(input("ingresar el monto a retirar: "))
p.retirar(cantidad_r)"""

###########################################################################################################

class Persona:
    def __init__(self, nombre=" ", edad=" ", dni=" "):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def muestra(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        if int(self.edad) >= 18:
            print(f"{self.nombre} es mayor de edad")
            return True

class Cuenta:
    def __init__(self, titular=Persona(), cantidad = 0):
        self.titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"DATOS TITULAR: \n{self.titular.muestra()}")
        print(f"SALDO: ${self.__cantidad}")

    def ingresar(self):
        valor_i = float(input("Ingrese el valor a depositar: "))
        if valor_i != 0 and valor_i > 0:
            self.__cantidad += valor_i
        elif valor_i == 0:
            print("no ingreso un monto valido")
        elif valor_i < 0:
            self.__cantidad = 0

    def retirar(self):
        valor_r = float(input("Ingrese el valor a retirar: "))
        if valor_r != 0:
            self.__cantidad -= valor_r
            if self.__cantidad < 0:
                print("la cuenta esta en numeros rojos")
                print(f"Su saldo: {self.__cantidad}")
        elif valor_r == 0:
            print("no ingreso un monto invalido")

belen = Persona("Belen ", 32, 11333222)

cliente = Cuenta(belen, 2000)


cliente.mostrar()
cliente.ingresar()
cliente.mostrar()
cliente.retirar()
cliente.mostrar()

