#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:48:03 2022

@author: manuel
"""
import numpy as np
import pandas as pd
def algoritmo1(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros):
    print("Parametros %s"%parametros)
    lineasaescribir=[]
    tiempoTotal=cabecera[0]

    i=0

    """for fila in adyacencia1:
        j=0
        for elem in fila:
            if elem!=0:
                print("%s,%s"%(i,j))
                print(elem)
                time.sleep(2)
            j+=1
        i+=1"""
    j=0
    for rotonda in rotondas:
         for llega,i in rotonda.items():

             if(adyacencia1[j,llega])==0:
                 print("es 0")
         j+=1

    j=0
    for rotonda in rotondas:
        print(rotonda)
        print(rotonda)
        print(rotonda)

        if len(rotonda.keys())>0:
            suma=np.sum([adyacencia1[j,llega] for llega,i in rotonda.items()])
            minimo=np.min([adyacencia1[j,llega]/suma for llega,i in rotonda.items()])
            #print("Suma %s, minimo %s"%(suma,minimo))

            if not np.isnan(minimo):
                for llega,i in rotonda.items():
                    i
                    #print(int(adyacencia1[j,llega]/(suma*minimo)))


        j+=1
