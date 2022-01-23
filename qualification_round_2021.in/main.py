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
  
nombreArchivo="f.txt" 
PRINT=False
           
   
cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
#%%algotimo           

algoritmos.algoritmo1(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars)
       

    
    
    

#%%
escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
sumaPuntos=0
sumaPuntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,sumaPuntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT)
print(sumaPuntos)
    