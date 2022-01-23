#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:01:38 2022

@author: manuel
"""
#%%




import entradaDatos
import pandas as pd
import numpy as np
import computarpuntos
import escribirEnArchivo
import time
import algoritmos

nombreArchivo="d.txt"
PRINT=True


cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
#%%algotimo
parametros={}
parametros["ciclo"]=15
parametros["tiempoPorCalle"]=1
solucionAEscribir,solucion=algoritmos.algoritmo0(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)





#%%
#escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
escribirEnArchivo.escribirEnArchivo2(solucionAEscribir)
sumaPuntos=0
sumaPuntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,sumaPuntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
print(sumaPuntos)


#%%
#bucle con todos los archivos
nombres=["a.txt","b.txt","c.txt","d.txt","e.txt","f.txt"]
sumaPuntos=0
PRINT=False
for nombreArchivo in nombres:
    cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
    parametros={}
    parametros["ciclo"]=15
    parametros["tiempoPorCalle"]=2
    solucionAEscribir,solucion=algoritmos.algoritmo0(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)
    escribirEnArchivo.escribirEnArchivo2(solucionAEscribir)
    #escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
   
    sumaPuntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,sumaPuntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
print(sumaPuntos)
