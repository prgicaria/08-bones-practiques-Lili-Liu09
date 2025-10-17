#!/usr/bin/env python

'''Bones pràctiques.
Pràctica del Shebang, l'informació bàsica i l'ús de docstrings.

Institut Icària
Programació - 1r Batxillerat - Curs 2025-56
'''

__author__ = "Lili Liu"
__emails__ = ["lliu@instituticaria.cat", "lili2009liu@gmail.com"]
__date__ = 2025/10/17

divident = float(input("Quin és el divident?"))
divisor = float(input("Quin és el divisor?"))

quocient = divident//divisor
residu = divident-(divisor*quocient)

print(f"Divisió: {divident}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
