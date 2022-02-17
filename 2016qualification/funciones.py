#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:38:16 2022

@author: manuel
"""

import numpy as np
import pandas as pd
import itertools
from  itertools import combinations
import clases

def crearmatriz(dimension,valor=0):
    matriz=np.zeros(shape=dimension)
    matriz.fill(valor)
    return matriz
def crearDataFrame(diccionario):
    return  pd.DataFrame.from_records(diccionario)
def devolverListaOrdenada(lista,arrayLambda):
    #con reverse=True devuelve de mayor a penor
    #lista.sort(key=lambda t: arrayLambda[t]["a"], reverse=True)
    lista.sort(key=lambda t: arrayLambda[t], reverse=True)
    return lista
def devolverColumnaDiccionario(diccionario,columna):
    return [row[columna] for row in diccionario.values()]
    
def devolverColumnaLista(lista,columna):
    
    return [row[columna] for row in lista]


def devolverCombinaciones(lista,numero):
     combinaciones=combinations(lista,numero)
     return combinaciones
 
    
def devolverPosicionesCheckeandoPosicionEnMatriz(matriz,condicion):
    u=np.where(matriz>condicion)
    arrayX=[]
    arrayY=[]
    arrayValores=[]
    arrayConjunto=[]
    
    for i in range(len(u[0])):
        arrayX.append(u[0][i])
        arrayY.append(u[1][i])
        arrayConjunto.append([u[0][i],u[1][i]])
    return  arrayX,arrayY,arrayConjunto
    
    
def devolverPosicionesDeMaximos(matriz):
    u=np.unravel_index(np.argmax(matriz, axis=None), matriz.shape)
    return u
def devolverPosicionesDeMinimos(matriz):
    u=np.unravel_index(np.argmin(matriz, axis=None), matriz.shape)
    return u
       
       
