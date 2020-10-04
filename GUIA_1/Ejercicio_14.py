#Ejercicio 14:
"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener
en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que
pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad
de dinero conseguida en cada nivel es de 100000 multiplicada por la puntuación del nivel.

Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más

Crear un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario."""



#SIN FUNCION

empleado = input("ingrese el nombre del empleado: ")
puntuacion = float(input("ingrese la puntuacion: "))

sueldo = puntuacion * 100000
rendimiento = "Inaceptable", "Aceptable", "Meritorio"            # tupla

if puntuacion == 0.0:
    print()
    print(f"Evaluacion Personal del Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[0]} \n Su salario es de ${sueldo}")
elif puntuacion == 0.4:
    print()
    print(f"Evaluacion Personal del Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[1]} \n Su salario es de ${sueldo}")
elif puntuacion >= 0.6:
    print()
    print(f"Evaluacion Personal del Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[2]} \n Su salario es de ${sueldo}")

else:
    print()
    print("nivel incorrecto")



"""
ano = int(input("ingrese año: "))
empleado = input("ingrese el nombre del empleado: ")
puntuacion = float(input("ingrese la puntuacion: "))
sueldo = puntuacion * 100000
rendimiento = "Inaceptable", "Aceptable", "Meritorio"            # tupla

if puntuacion % 0.2 == 0.0 and puntuacion != 0.2 or puntuacion == 0.6:
    if puntuacion == 0.0:
        print()
        print(f"Evaluacion Personal del año {ano}\n Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[0]} \n Su salario es de ${sueldo}")
    if puntuacion == 0.4:
        print()
        print(f"Evaluacion Personal del año {ano}\n Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[1]} \n Su salario es de ${sueldo}")
    if puntuacion >= 0.6:  #ME TIRA ERROR SOLO CON 0.6 (porque el MODULO %2 de 0.6 da 0.199999999 (impar)
        print()
        print(f"Evaluacion Personal del año {ano}\n Empleado: {empleado} \n Su puntuacion es {puntuacion} \n Su nivel es {rendimiento[2]} \n Su salario es de ${sueldo}")

else:
    print()
    print("nivel incorrecto")
"""



"""
nomina = {                                                         # DICCONARIO
    "empleado": "nombre",
    "nivel": 0.0,
}

nomina["empleado"] = input("ingrese nombre empleado: ")
nomina["nivel"] = float(input("ingrese evaluacion: "))

nom_empleado = nomina.get("empleado")
puntuacion = nomina.get("nivel")
sueldo = puntuacion * 100000
rendimiento = "Inaceptable", "Aceptable", "Meritorio"

if puntuacion % 0.2 == 0.0 and puntuacion != 0.2:
    if puntuacion == 0.0:
        print()
        print(f"Nivel Puntuacion \n Empleado: {nom_empleado} \n La puntuacion de este usuario es {puntuacion} \n Su nivel es {rendimiento[0]} \n Su salario sera ${sueldo}")
    if puntuacion == 0.4:
        print()
        print(f"Nivel Puntuacion \n Empleado: {nom_empleado} \n La puntuacion de este usuario es {puntuacion} \n Su nivel es {rendimiento[1]} \n Su salario sera ${sueldo}")
    if puntuacion == 0.6:  #ME TIRA ERROR SOLO CON 0.6
        print()
        print(f"Nivel Puntuacion \n Empleado: {nom_empleado} \n La puntuacion de este usuario es {puntuacion} \n Su nivel es {rendimiento[2]} \n Su salario sera ${sueldo}")

else:
    print()
    print("nivel incorrecto")
    """


#CON FUNCION

empleado = input("ingrese el nombre del empleado: ")
puntuacion = float(input("ingrese la puntuacion: "))


def evaluacion(nombre, valor):
    sueldo = valor * 100000
    rendimiento = "Inaceptable", "Aceptable", "Meritorio"            # tupla

    if puntuacion == 0.0:
        print()
        print(f"Evaluacion Personal del Empleado: {nombre} \n Su puntuacion es {valor} \n Su nivel es {rendimiento[0]} \n Su salario es de ${sueldo}")
    elif puntuacion == 0.4:
        print()
        print(f"Evaluacion Personal del Empleado: {nombre} \n Su puntuacion es {valor} \n Su nivel es {rendimiento[1]} \n Su salario es de ${sueldo}")
    elif puntuacion >= 0.6:
        print()
        print(f"Evaluacion Personal del Empleado: {nombre} \n Su puntuacion es {valor} \n Su nivel es {rendimiento[2]} \n Su salario es de ${sueldo}")
    else:
        print()
        print("nivel incorrecto")


evaluacion(empleado, puntuacion)






