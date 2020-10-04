#Ejercicio 10:
"""Crear un programa que pida al usuario su edad y muestra por pantalla
si es mayor de edad o no, siendo 18 años la mayoría de edad."""

#SIN FUNCION

edad = int(input("ingrese su edad: "))


if edad != 0 and edad < 120:                    # Si edad es distinta a 0 y menor a 120 entonces seguir la linea de codigo
    if edad < 18:
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")
else:
    print("edad incorrecta")



#CON FUNCION

edad = int(input("ingrese su edad: "))                    #Variable fuera del metodo

def mayor(anios):                                         # El nombre del parametro es anios
    if anios != 0 and anios < 120:                        # Si edad es distinta a 0 y menor a 120 entonces seguir la linea de codigo
       if anios < 18:
            print("Usted es menor de edad")
       else:
            print("Usted es mayor de edad")
    else:
        print("edad incorrecta")

mayor(edad)                                                # Se llama al metodo y se le pasa como parametro la variable edad, por lo cual se ejecuta la misma