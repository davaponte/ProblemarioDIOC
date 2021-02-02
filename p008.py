#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
