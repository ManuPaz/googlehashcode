#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:24:43 2022

@author: manuel
"""
import numpy as np
def escribirEnArchivo(incidencia,arrayCalles,numerointersecciones):
    file=open("solucion.txt","w")
    filasaescribir=[]
    j=0
    for i in incidencia:
        filasaescribir.append([])
        u=(np.where(i==-1))
        #print(arrayCalles[u])
        filasaescribir[j]=arrayCalles[u]
        
        j+=1
        
    file.writelines(str(numerointersecciones)+"\n")
    j=0
    for linea in filasaescribir:
        #print(linea)
        file.writelines(str(j)+"\n"+str(len(linea))+"\n")
        for u in linea:
             file.writelines(u+" "+str(1)+"\n")
        j+=1
    file.close()
    
    
def escribirEnArchivo2(solucionAEscribir):
    file=open("solucion.txt","w")
   
    for linea in solucionAEscribir:
        if isinstance(linea, int):
            file.writelines(str(linea)+"\n")
        #print(linea)
        else:
            cadena=""
            for elem in linea:
                cadena+=(str(elem)+" ")
            cadena=cadena[:-1]
            file.writelines(cadena+"\n")
      
    file.close()

