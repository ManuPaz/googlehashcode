#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:14:53 2022

@author: manuel
"""
import pandas as pd
import numpy as np
import time

def entradaDatos(nombreArchivo):
        #nombreArch="a.txt"
    nombreArch=nombreArchivo
    archivo=open(nombreArch)
    lineas=archivo.readlines()
    cabecera=np.array(lineas[0].split(" "),dtype=int)
    numerodias=int(cabecera[0])
    numeroingenieros=int(cabecera[1])
    numeroservicios=int(cabecera[2])
    numerobinaries=int(cabecera[3])
    numerofeatures=int(cabecera[4])
    infoGeneral={}
    infoGeneral["numerodias"]= numerodias
    infoGeneral["numeroingenieros"]=  numeroingenieros
    infoGeneral["numerofeatures"]= numerofeatures
    infoGeneral["numeroservicios"]=   numeroservicios
    infoGeneral["numerobinaries"]=  numerobinaries
    
    serviciosvsfeatures=[]
    features=[]
    #print(cabecera)
    servicios1=[lin.strip().split(" ")for lin in lineas[1:(numeroservicios+1)]]
    servicios={}
    for (i,j) in servicios1:
        servicios[i]=int(j) 
    for i in range(1+numeroservicios,1+numeroservicios+2*numerofeatures,2):
        features.append([])
        serviciosvsfeatures.append([])
        features[len(features)-1]=lineas[i].strip().split(" ")
        
        serviciosvsfeatures[len(serviciosvsfeatures)-1]=lineas[i+1].strip().split(" ")
        
    return infoGeneral,servicios,serviciosvsfeatures,features

    
