#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:48:03 2022

@author: manuel
"""
import numpy as np
import pandas as pd
import time
#funcion que llama al algoritmo que este definido abajo
def algoritmo(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros):
    return alg(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros)

#algoritmo basico que hace schedules con tiempo1 para todas las calles por las  que entran coches en cada interseccion
def algoritmo0(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros):
    solucionAEscribir = list()

    j = 0
    for rotonda in rotondas:
        numCallesEntrantes = len(rotonda.keys())
        if (numCallesEntrantes) > 0:
            j += 1

    solucionAEscribir.append(j)
    j = 0
    for rotonda in rotondas:
        numCallesEntrantes = len(rotonda.keys())

        if (numCallesEntrantes) > 0:
            solucionAEscribir.append(j)
            solucionAEscribir.append(numCallesEntrantes)

            for llega, i in rotonda.items():
                solucionAEscribir.append([])
                indice = len(solucionAEscribir)-1
                solucionAEscribir[indice].append(i)
                solucionAEscribir[indice].append(parametros["tiempoPorCalle"])

        j += 1
    return solucionAEscribir, None

#algoritmo que asigna tiempos proporcionales al numero de coches que entran en cada interseccion
def algoritmo1(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros):
    solucionAEscribir = list()
    tiempoTotal = cabecera[0]
    j = 0


   
    for rotonda in rotondas:
        numCallesEntrantes = len(rotonda.keys())
        if (numCallesEntrantes) > 0:
            j += 1
    solucionAEscribir.append(j)
    j = 0
    for rotonda in rotondas:
        # print(rotonda)
        numCallesEntrantes = len(rotonda.keys())
        if numCallesEntrantes > 0:
            solucionAEscribir.append(j)
            solucionAEscribir.append(numCallesEntrantes)
            suma = np.sum([adyacencia1[j, llega]
                          for llega, i in rotonda.items()])
            minimo = np.min(
                [adyacencia1[j, llega]/suma for llega, i in rotonda.items()])
            #print("Suma %s, minimo %s"%(suma,minimo))
            if suma==0 or np.isnan(minimo) or minimo==0:
                print("na")
            if not np.isnan(minimo):
                for llega, i in rotonda.items():
                     i
                     
                     tiempo=int(adyacencia1[j,llega]/(suma*minimo))
                     #print("Numero de coches que entran %s, tiempo que se le asigna %s, numero total de coches que entran %s"%(adyacencia1[j,llega],tiempo,suma))
                     solucionAEscribir.append([])
                     indice = len(solucionAEscribir)-1
                     solucionAEscribir[indice].append(i)
                     solucionAEscribir[indice].append(tiempo)
       

        j += 1
    return solucionAEscribir,None


def inspeccionarCaminos(adyacencia,adyacencia1,incidencia,cochesvsinteresecciones,cars,rotondas):
    print(adyacencia)
    numRotondas=[]
    for rotonda in incidencia:
        print(np.mean(rotonda==-1))
    
#algorimo buscando bucles y diferenciando nodos de llegada y salida
def algoritmo2(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros):
    solucionAEscribir = list()
    

    j = 0
    for rotonda in rotondas:
        numCallesEntrantes = len(rotonda.keys())
        if (numCallesEntrantes) > 0:
            j += 1

    solucionAEscribir.append(j)
    j = 0
    for rotonda in rotondas:
        numCallesEntrantes = len(rotonda.keys())

        if (numCallesEntrantes) > 0:
            solucionAEscribir.append(j)
            solucionAEscribir.append(numCallesEntrantes)

            for llega, i in rotonda.items():
                solucionAEscribir.append([])
                indice = len(solucionAEscribir)-1
                solucionAEscribir[indice].append(i)
                solucionAEscribir[indice].append(parametros["tiempoPorCalle"])

        j += 1
    return solucionAEscribir, None



#seleccion de la funcion que se va a utilizar como algoritmo        
alg=algoritmo1