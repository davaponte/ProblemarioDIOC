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

# ~ Problema N.5:
# ~ Diseñe un programa que, dado un recipiente cilíndrico, solicite los datos
# ~ pertinentes para poder calcular su volumen y área, y mostrar tales resultados.

from sys import exit
from math import pi

def InputValue(Msg):
    print(Msg, end='')
    v = input()
    try:
        v = float(v)
        if (v <= 0):
            raise Exception()
        return v
    except:
        print('Error Capa 8. Debes ingresar un número positivo, cacho cabrón!')
        exit(1)

Altura = InputValue('Ingrese altura: ')
Radio = InputValue('Ingrese radio de la base: ')

Volumen = pi * Radio**2 * Altura
Area = 2 * pi * Radio * Altura + 2 * pi * Radio**2

print('Volumen: {}, Area: {}'.format(Volumen, Area))

