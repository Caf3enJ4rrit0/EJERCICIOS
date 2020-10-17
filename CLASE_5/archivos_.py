data = """
Este sera el primer 
contenido de mi archivo.
"""

with open("archivo.txt", "w+") as f:
        f.write(data)
        f.seek(0)
        print(f.read())
        f.tell()
        print(f.tell())
        f.close()
        """for linea in readlines():
                print(linea)
        contenido_readlines = f.readlines()
        print(contenido_readlines)"""

