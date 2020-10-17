# Filtrar datos

import re

vuelos_ar = [
    "AR1133",
    "AR1305",
    "AR1293",
    "AR1371",
    "AR1303",
    "AR2709",
    "AR2701",
    "A#2602"
]

for i in vuelos_ar:
    if re.findall("AR[1100-1800]", i):
        print(f"El vuelo {i} es un vuelo internacion")
    else:
        print(f"El vuelo {i} es un vuelo de cabotaje")