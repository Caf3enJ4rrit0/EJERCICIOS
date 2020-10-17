import re

patron = "hola$"            # si se encuentra al principio
cadena = "buenos dias, hola"

if re.search(patron, cadena):
    print(True)



patron_2 = "^mi nombre"     # si se encuentra al final
cadena_2 = "mi nombre es Magali"

if re.search(patron_2, cadena_2):
    print(True)