#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~ Problema N.1:
# ~ Diseñe un programa que dadas las coordenadas (x,y) de un punto en el plano,
# ~ determine y muestre sus coordenadas polares (R, θ).

from sys import exit
from math import sqrt, atan2, degrees

print('Ingrese coordenada X: ', end='')
x = input()
try:
    x = float(x)
except:
    print('Error Capa 8. Debes ingresar un número, cacho cabrón!')
    exit(1)

print('Ingrese coordenada Y: ', end='')
y = input()
try:
    y = float(y)
except:
    print('Error Capa 8. Debes ingresar un número, cacho cabrón!')
    exit(1)

print('Coordenadas: (x = {0:7.2f}, y = {1:7.2f})'.format(x, y))

R = sqrt(x**2 + y**2)
θ = atan2(y, x)

print('Polares: (R = {0:8.5f}, θ = {1:8.5f} rad)'.format(R, θ))
print('         (      "     , θ = {0:8.5f} deg)'.format(degrees(θ)))

