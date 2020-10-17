import re

patron = "hola+"
cadena = "hola buenos dias hola"

if re.findall(patron, cadena):
    print(True)