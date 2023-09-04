#!/usr/bin/env python 

import sys

params = sys.argv

# Los parametros utilizados al correr este
# script son:

for i in range(len(params)):
    print(i, params[i])

# Ojo que estos parametros siempre se guardan como 
# strings, de modo que si deseo utilizarlos para 
# que el usuario/a ingrese valores numéricos
# ES NECESARIO CONVERTIRLOS:

# Imaginemos que queremos guardar solo los numeros
# en una lista:
nums = []
for p in params:
    if p.isnumeric():
        nums.append(float(p))

# en vez de float() también se puede usar int() si 
# saben de antemano que es un entero. 

print("Solo los siguientes son numeros:")
print(nums)

