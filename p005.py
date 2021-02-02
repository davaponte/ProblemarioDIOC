#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

