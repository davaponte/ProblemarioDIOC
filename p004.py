#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

