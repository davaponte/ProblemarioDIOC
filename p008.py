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

# ~ Problema N.8:
# ~ Diseñe un programa que dado un punto en el plano por sus coordenadas (x,y),
# ~ determinar en qué cuadrante se encuentra indicándolo con un mensaje al
# ~ usuario.

from sys import exit

def InputValue(Msg):
    print(Msg, end='')
    v = input()
    try:
        v = float(v)
        return v 
    except:
        print('Error Capa 8. Debes ingresar un número, cacho cabrón!')
        exit(1)

x = InputValue('Ingrese x: ')
y = InputValue('Ingrese y: ')

if (x == 0) and (y == 0):
    print('Punto en el origen.')
else:
    if (x > 0):
        if (y > 0):
             C = 1
        else:
            C = 4
    else:
        if (y > 0):
             C = 2
        else:
            C = 3
    print('Punto en el cuadrante #: {}'.format(C))
