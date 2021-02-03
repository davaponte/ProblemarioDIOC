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

# ~ Problema N.7:
# ~ En un reloj de agujas (que sólo tiene horario y minutero), elabore un programa
# ~ que calcule y muestre el menor ángulo en grados que forman tales agujas dada
# ~ una hora suministrada por el usuario.

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

H = InputValue('Ingrese las horas: ')
M = InputValue('Ingrese los minutos: ')

# Hay 60 minutos en 360 grados. Por cada minuto hay 6 grados
MAngle = M * 6 

# Hay 12 horas en 360 grados. Por cada hora hay 30 grados
# Pero si la hora es 12 se usa 0
HAngle = H * 30 if H != 12 else 0
# Ahora hay que ajustar el mini desfase por los minutos pasados
# Por cada 30 grados de una hora hay 60 minutos
HAngle += M * 0.5

Dif = abs(HAngle - MAngle)
if Dif > 180:
    Dif = 360 - Dif

print('Ángulo mínimo: {}'.format(Dif))
