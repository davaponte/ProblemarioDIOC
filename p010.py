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

# ~ Problema N.10:
# ~ Diseñe un programa que indique si tres puntos dados por sus coordenadas (x, y)
# ~ forman triángulo y en caso de formarlo debe indicarse que tipo de triángulo
# ~ forma.

from sys import exit
from math import sqrt

def InputValue(Msg):
    print(Msg, end='')
    v = input()
    try:
        v = float(v)
        return v 
    except:
        print('Error Capa 8. Debes ingresar un número, cacho cabrón!')
        exit(1)

def Distancia(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

x, y = [], []
for c in range(3):
    x.append(InputValue('Ingrese x' + str(c + 1) + ': '))
    y.append(InputValue('Ingrese y' + str(c + 1) + ': '))

dyA = y[1] - y[0] 
dxA = x[1] - x[0] 
dyB = y[2] - y[1] 
dxB = x[2] - x[1] 

IsTriangle = False

if (dxA == 0) or (dxB == 0):
    if (dxA == 0) and (dxB == 0):
        print('Los puntos no forman un triángulo')
    else:
        print('Los puntos SÍ forman un triángulo')
        IsTriangle = True
else:
    if (dyA / dxA == dyB / dxB):
        print('Los puntos no forman un triángulo')
    else:
        print('Los puntos SÍ forman un triángulo')
        IsTriangle = True
      
if IsTriangle:
    dA = Distancia(x[0], y[0], x[1], y[1])
    dB = Distancia(x[1], y[1], x[2], y[2])
    dC = Distancia(x[2], y[2], x[0], y[0])
    if (dA == dB) and (dB == dC):
        print('Triángulo equilátero')
    elif (dA == dB) or (dB == dC):
        print('Triángulo isóceles')
    else:
        print('Triángulo escaleno')
