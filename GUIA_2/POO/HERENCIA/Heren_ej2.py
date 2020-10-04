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

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni



class Cuenta(Persona):
    def __init__(self, nombre, edad, dni, titular, cantidad):
        super().__init__(nombre, edad, dni)
        self.titular = titular
        self. cantidad = cantidad


    def mostrar(self):
        print(self.titular)
        print(self.cantidad)

    def ingresar(self):
        ingresa = int(input("Desea ingresar dinero a la cuenta? S=1/N=0: "))
        print(ingresa)
        if ingresa == 1:
            monto = int(input("ingresar el monto a depositar: "))
            if monto != 0:
                self.cantidad += monto
            elif monto == 0:
                print("no ingreso un monto invalido")
                print(ingresa)
        elif ingresa == 0:
            print("gracias por usar nuestros servicios")
        elif ingresa != 1 and ingresa!= 0:
            print("error")

    def retirar(self):
        retira = int(input("Desea retirar dinero de la cuenta? S=1/N=0: "))
        print(retira)
        if retira == 1:
            valor = int(input("ingresar el monto a retirar: "))
            if valor != 0:
                self.cantidad -= valor
                if self.cantidad < 0:
                    print("la cuenta esta en numeros rojos")
                    print(f"Su saldo: {self.cantidad}")
            elif valor == 0:
                print("no ingreso un monto invalido")
                print(retira)
        elif retira == 0:
            print("gracias por usar nuestros servicios")
        elif ingresa != 1 and ingresa != 0:
            print("error")


belen = Cuenta("Belen", 32, 33589676, "hola", 200)


belen.mostrar()
belen.ingresar()
belen.mostrar()
belen.retirar()

