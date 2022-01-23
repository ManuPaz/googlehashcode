#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:01:38 2022

@author: manuel
"""
#%%



#importar modulos
import entradaDatos
import pandas as pd
import numpy as np
import computarpuntos
import escribirEnArchivo
import time
import algoritmos
import ejecutarEnBucle
#entrada de datos con modulo entradadatos
nombreArchivo="f.txt"
PRINT=True
cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
#%%algoritmo
parametros={}
parametros["ciclo"]=15
parametros["tiempoPorCalle"]=1
#solucionAEscribir es la solucion en formato array para escribirla en el archivo
solucionAEscribir,solucion=algoritmos.algoritmo(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)





#%%
#escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
#escribirenarchivolasolucion
escribirEnArchivo.escribirEnArchivo2(solucionAEscribir,"solucion.txt")
puntos=0
#calcular los puntos obtenidos con esa solucion
puntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,puntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
print(puntos)


#%%
#bucle para ejecutar el algoritmo con  todos los archivos con los mismos parametros
parametros={}
parametros["ciclo"]=15
parametros["tiempoPorCalle"]=1
nombres=["a.txt","b.txt","c.txt","d.txt","e.txt","f.txt"]
ejecutarEnBucle.ejecutarTodosLosArchivosMP(nombres,parametros)

#%%
#bucle buscando los mejores parametros por archivo
"""arrays=([0,3,4,5],[1,2],[7,8,9,10])
matriz=np.meshgrid([0,3,4,5],[1,2],[7,8,9,10])
for i in  np.transpose(matriz).reshape(-1,len(arrays)):
    print(i)"""
nombres=["a.txt","b.txt","c.txt","d.txt","e.txt","f.txt"]
matriz=np.meshgrid([1,2,3])
matriz=np.transpose(matriz).reshape(-1,1)
diccionarioParam=ejecutarEnBucle.ejecutarPorArchivoMP(nombres, matriz,PRINT=True)




