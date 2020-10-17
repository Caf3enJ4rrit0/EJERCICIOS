# se utiliza en web scrapping

import re

patron = ".hola"                #coincide con cualquier caracter/lo busca sin importar que tiene adelante
cadena = "$%%$%&$%$$%&$%%&hola"

if re.findall(patron, cadena):
    print(True)