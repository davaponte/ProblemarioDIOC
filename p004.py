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

# ~ Problema N.4:
# ~ Diseñe un programa que dada una cantidad de segundos, entera y positiva,
# ~ indique a cuanto equivale en años, meses, días, horas y segundos. Asuma años de
# ~ 360 días y simplifique a que todos los meses poseen 30 días. Por ejemplo:
# ~ 31803310 segundos equivalen a 1 año, 3 días, 2 horas, 15 minutos y 10
# ~ segundos.

# ~ El ejemplo tiene un error. Calculan para 365 días pero dicen que usen años de 360

from sys import exit

def InputValue(Msg):
    print(Msg, end='')
    v = input()
    try:
        v = int(v)
        if (v <= 0):
            raise Exception()
        return v
    except:
        print('Error Capa 8. Debes ingresar un número entero y positivo, cacho cabrón!')
        exit(1)

S = InputValue('Ingrese número de segundos: ')

Years, Res = divmod(S, 360 * 86400)

Months, Res = divmod(Res, 30 * 86400)

Days, Res = divmod(Res, 86400)

Hours, Res = divmod(Res, 3600)

Minutes, Seconds = divmod(Res, 60)

print('{} años, {} meses, {} días, {} horas, {} minutos y {} segundos'.format(Years, Months, Days, Hours, Minutes, Seconds))

