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

# ~ Problema N.2:
# ~ Diseñe un programa que dados dos puntos en el plano por sus coordenadas 
# ~ (x 1 , y 1) y (x 2 , y 2) calcule y muestre la longitud del segmento 
# ~ que determinan estos puntos, y que se calculen y muestren las coordenadas 
# ~ del punto medio de ese segmento.

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

x1 = InputValue('Ingrese coordenada X1: ')
y1 = InputValue('Ingrese coordenada Y1: ')
x2 = InputValue('Ingrese coordenada X2: ')
y2 = InputValue('Ingrese coordenada Y2: ')

print('Punto 1: (x1 = {0:7.2f}, y1 = {1:7.2f})'.format(x1, y1))
print('Punto 2: (x2 = {0:7.2f}, y2 = {1:7.2f})'.format(x2, y2))

D = sqrt((x1 - x2)**2 + (y1 - y2)**2)
xm, ym = (x1 + x2) / 2, (y1 + y2) / 2

print('Distancia: D = {0:8.5f}'.format(D))
print('Punto Medio: (Xm = {0:8.5f}, Ym = {0:8.5f})'.format(xm, ym))

