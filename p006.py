#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~ Problema N.6:
# ~ Diseñar un programa que dadas las coordenadas cartesianas (x, y, z) de un
# ~ punto en el espacio, calcule y muestre sus coordenadas cilíndricas y sus
# ~ coordenadas esféricas.

from sys import exit
from math import sqrt, atan2, asin, degrees

def InputValue(Msg):
    print(Msg, end='')
    v = input()
    try:
        v = float(v)
        return v
    except:
        print('Error Capa 8. Debes ingresar un número, cacho cabrón!')
        exit(1)

X = InputValue('Ingrese X: ')
Y = InputValue('Ingrese Y: ')
Z = InputValue('Ingrese Z: ')


ρ = sqrt(X**2 + Y**2)
if (X == 0):
    φ = asin(Y / ρ)
else:
    φ = atan2(Y, X)
z = Z

print('Cilíndricas')
print('ρ: {0}, φ: {1} rad / {3} deg, z: {2}'.format(ρ, φ, z, degrees(φ)))

r = sqrt(X**2 + Y**2 + Z**2)
θ = atan2(Y, X)  # ~ Faltan casos
φ = atan2(ρ, z)

print('Esféricas')
print('r: {0}, θ: {1} rad / {2} deg, φ: {3} rad / {4} deg'.format(r, θ, degrees(θ), φ, degrees(φ)))
