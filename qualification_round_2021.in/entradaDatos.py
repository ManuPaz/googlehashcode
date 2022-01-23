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
    numerocalles=cabecera[2]
    numerointersecciones=cabecera[1]
    numerocoches=cabecera[3]
    #print(cabecera)
    calles=[lin.strip() .split(" ")for lin in lineas[1:(numerocalles+1)]]
    nombrescalles=[calle[2] for calle in calles]
    cars=[lin.strip() .split(" ")for lin in lineas[(numerocalles+1):]]
    numCalles=np.array([car[0] for car in cars],dtype=int)
    adyacencia=np.empty(shape=(numerointersecciones,numerointersecciones),dtype=int)
    adyacencia1=np.empty(shape=(numerointersecciones,numerointersecciones),dtype=int)
    adyacencia.fill(-1)
    adyacencia1.fill(0)
    incidencia=np.zeros(shape=(numerointersecciones,numerocalles),dtype=int)
    incidencia1=np.zeros(shape=(numerointersecciones,numerocalles),dtype=int)
    interseccionesVScallesIniciales=[]
    interseccionesVScallesFinales=[]
    arrayCostes=np.empty(shape=(numerocalles))
    rotondas=[]
    for i in range(0,numerointersecciones):
        rotondas.append({})

    arrayCalles=np.empty(shape=(numerocalles),dtype=object)
    dicCalles=dict()
    for i in range(0,numerocalles):
        #print(i)
        calle=calles[i]
        #print(calle)
        arrayCalles[i]=calle[2]
        dicCalles[calle[2]]=i
        arrayCostes[i]=int(calle[3])
        adyacencia[int(calle[0]),int(calle[1])]=i
        incidencia[int(calle[0]),i]=1
        incidencia[int(calle[1]),i]=-1
        rotondas[int(calle[1])][int(calle[0])]=calle[2]

    interseccionesvscohes=[]
    cochesvsinteresecciones=[]
    for i in range(0,numerointersecciones):
        interseccionesvscohes.append([])
    for i in range(0,numerocoches):
        cochesvsinteresecciones.append([])

    for i in range (0,numerocoches):
        coche=cars[i]
        k=0
        for calle in coche[1:]:

            rua=dicCalles[calle]
            rotondaFinal=calles[rua][1]
            cochesvsinteresecciones[i].append(int(rotondaFinal))
            if k==0:
                interseccionesvscohes[int(rotondaFinal)].append(i)
            k+=1



    for coche,car in zip(cochesvsinteresecciones,cars):
        adyacencia1[coche[0],int(calles[dicCalles[car[1]]][0])]+=1
        
        for j in range(0,len(coche)-1):
            adyacencia1[coche[j+1],coche[j]]+=1
            #print("%s,%s,%s"%(coche[j+1],coche[j],adyacencia1[coche[j+1],coche[j]]))
            #time.sleep(2)
    l=0
    for rotonda in rotondas:
        #print(rotonda)
        array=[]
        for u in rotonda.keys():
               #print(u)
               if   adyacencia1[l,u]==0:

                    array.append(u)

                    #print(adyacencia1[l,u])
        for aa in array:
            rotonda.pop(aa)
               #print(adyacencia1[l,u])
        l+=1
    return cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars
