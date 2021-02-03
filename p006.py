#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright 2021 David Aponte
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

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
