# busqueda en datos

import re

patron = "[AR]"
lista_vuelos = [
    "AR2606",
    "AR2607",
    "IB1304"
]

for vuelo in lista_vuelos:
    if re.findall(patron, vuelo):
        print(f"El vuelo {vuelo} es de AR")