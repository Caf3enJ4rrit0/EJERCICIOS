#Ejercicio 3
"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
ciento. Construir los siguientes métodos para la clase:
● Un constructor.
● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad., por lo tanto hay que crear un método esTitularValido() que devuelve
verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
contrario.
● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.
● Pensar los métodos heredados de la clase madre que hay que reescribir.
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
            print("no ingreso un monto invalido")


class CuentaJoven(Cuenta):
    def __init__(self, titular_nombre, titular_edad, titular_dni, cantidad = 0, bonificacion = 0):
        super().__init__(titular_nombre, titular_edad, titular_dni, cantidad)
        self.clj_nombre = titular_nombre
        self.clj_edad = titular_edad
        self.__clj_dni = titular_dni
        self.__clj_cantidad = cantidad
        self.bonificacion = bonificacion

    def esTitularValido(self):
        while self.clj_edad >= 18 and self.clj_edad <= 25:
            return True
        else:
            return False

    def mostrar(self):
        if self.clj_edad >= 18 and self.clj_edad <= 25:              #se puede hacer que llame a la funcion esTitularValido?
            print(f"DATOS TITULAR - Cuenta Joven - : \nNOMBRE COMPLETO: {self.clj_nombre}, \nEDAD: {self.clj_edad}, \nDNI:{self.__clj_dni}")
            print(f"BONITICACION: {self.bonificacion}%")
            print(f"SALDO: ${self.__clj_cantidad}")
        else:
            print(mostrar())                                  #Se puede llamar a un metodo de la clase padre dentro de un metodo de la clase hija?



    def retirar(self, valor):
        if self.clj_edad >= 18 and self.clj_edad <= 25:             #se puede hacer que llame a la funcion esTitularValido?
            if valor != 0:
                self.__clj_cantidad -= valor
                if self.__clj_cantidad < 0:
                    print("la cuenta esta en numeros rojos")
                    print(f"Su saldo: {self.__clj_cantidad}")
            elif valor == 0:
                print("no ingreso un monto invalido")






t_nom = input("ingrese su nombre completo: ")
t_edad = int(input("ingrese su edad: "))
t_dni = int(input("ingrese su dni: "))

alguien = Persona(t_nom, t_edad, t_dni)                                                #Objeto de Persona

cliente = CuentaJoven(alguien.nombre, alguien.edad, alguien.dni, 2000, 25)                  #objeto de Cuenta

cliente.mostrar()
print()"""

"""cantidad_d = float(input("ingresar el monto a depositar: "))
humano.ingresar(cantidad_d)
print()

humano.mostrar()
print()""""""

cantidad_r = float(input("ingresar el monto a retirar: "))
cliente.retirar(cantidad_r)"""

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
        self.cantidad = cantidad

    def mostrar(self):
        print(f"DATOS TITULAR: \n{self.titular.muestra()}")
        print(f"SALDO: ${self.cantidad}")

    def ingresar(self):
        valor_i = float(input("Ingrese el valor a depositar: "))
        if valor_i != 0 and valor_i > 0:
            self.cantidad += valor_i
        elif valor_i == 0:
            print("no ingreso un monto valido")
        elif valor_i < 0:
            self.cantidad = 0

    def retirar(self):
        valor_r = float(input("Ingrese el valor a retirar: "))
        if valor_r != 0.0:
            self.cantidad -= valor_r
            if self.cantidad < 0.0:
                print("la cuenta esta en numeros rojos")
                print(f"Su saldo: {self.cantidad}")
        elif valor_r == 0:
            print("no ingreso un monto invalido")


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.titular.esMayorDeEdad() and self.titular.edad <= 25:
            return True
        else:
            return False

    def mostrar(self):
        validez = self.esTitularValido()
        if validez:
            print(f"DATOS TITULAR - Cuenta Joven - : \n{self.titular.muestra()}")
            print(f"SALDO: ${self.cantidad}")
            print(f"BONITICACION: {self.bonificacion}%")
        else:
            print("Esta cuenta no cumple los requisitos")

    def retirar(self):
        validez = self.esTitularValido()
        if validez:
            print("Puede retirar dinero.")
            retiro = float(input("Retire dinero o presione 0 para salir: "))
            if retiro != 0.0:
                self.cantidad -= retiro
            if self.cantidad < 0.0:
                print("la cuenta esta en numeros rojos")
                print(f"Su saldo: {self.cantidad}")
            elif retiro == 0:
                print("no ingreso un monto invalido")



belen = Persona("Belen ", 22, 11333222)
cliente = CuentaJoven(belen, 2000, 50)


cliente.mostrar()
cliente.ingresar()
cliente.mostrar()
print()
cliente.retirar()
cliente.mostrar()
