#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

