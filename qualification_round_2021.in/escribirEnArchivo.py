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
    
    
def escribirEnArchivo2(rotondas):
    file=open("solucion.txt","w")
    filasaescribir=[]
   
        
    file.writelines(str(len(rotondas))+"\n")
    for rotonda in rotondas:
        file.writelines(str(len(rotonda.keys()))+"\n")
        #print(linea)
        for i,e in rotonda.items():
          
             file.writelines(i+" "+str(e)+"\n")
      
    file.close()

