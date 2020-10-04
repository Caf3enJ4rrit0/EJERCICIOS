#Ejercicio 16:
"""Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad)."""



#SIN FUNCION

edad = int(input("Ingrese su edad: "))

for anios in range(edad):     #BUSCAS QUE muestre la edad verdadera
    while anios != 0:
        print(f"Usted cumplio {anios} años")
        anios += 1
        if anios == edad:
            print(f"Usted cumplio {edad} años")
        break


#CON FUNCION

edad = int(input("Ingrese su edad: "))

def cumple(num):
    for anios in range(num):                         #BUSCAS QUE muestre la edad verdadera
        while anios != 0:
            print(f"Usted cumplio {anios} años")
            anios += 1
            if anios == num:
                print(f"Usted cumplio {num} años")
            break

cumple(edad)