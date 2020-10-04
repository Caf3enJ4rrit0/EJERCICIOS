# Ejercicio 9:
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
la empresa de logística les cobra por el peso de cada paquete así que deben calcular el peso de los payasos y
muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que
lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
Mostrar el resultado por pantalla."""

#SIN FUNCION

payaso = 112  # peso en g
muneca = 75   # peso en g

v_pay = int(input("ingrese la cantidad de payasos vendidos: "))
v_mun = int(input("ingrese la cantidad de muñecas vendidas: "))

peso_env = (v_pay * payaso) + (v_mun * muneca)
print()
print(f"El paquete pesa {peso_env}g")



#CON FUNCION

def payaso():
    payaso = 112  # peso en g
    v_pay = int(input("ingrese la cantidad de payasos vendidos: "))
    envio_p = v_pay * payaso
    return envio_p                              # Devuelve el valor de envio_p

def muneca():
    muneca = 75  # peso en g
    v_mun = int(input("ingrese la cantidad de muñecas vendidas: "))
    envio_m = v_mun * muneca
    return envio_m                              # Devuelve el valor de envio_m


def jugueteria(pay_env, mun_env):               # Recibe 2 parametros
    peso = pay_env + mun_env                    # Esos parametros los utiliza para la variable peso
    print(f"El paquete pesa {peso}g")

p = payaso()                                    # Guardo en la variable p el valor de retorno del metodo payaso()
m = muneca()                                    # Guardo en la variable m el valor de retorno del metodo muneca()
jugueteria(p, m)                                # Llamo al metodo Jugueteria y le paso los parametros necesarios,
                                                # en este caso los valores alojados en la variable de p y m para obtener el peso total del envio

