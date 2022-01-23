#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:48:03 2022

@author: manuel
"""
import numpy as np
import pandas as pd


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


def algoritmo1(cabecera, numerocalles, numerocoches, numerointersecciones, adyacencia, incidencia, adyacencia1, incidencia1, interseccionesvscohes, cochesvsinteresecciones, rotondas, calles, dicCalles, arrayCalles, cars, **parametros):
    solucionAEscribir = list()
    tiempoTotal = cabecera[0]

    i = 0

    j = 0
    for rotonda in rotondas:
        for llega, i in rotonda.items():

            if(adyacencia1[j, llega]) == 0:
                print("es 0")
        j += 1

    j = 0
    for rotonda in rotondas:
        # print(rotonda)

        if len(rotonda.keys()) > 0:
            suma = np.sum([adyacencia1[j, llega]
                          for llega, i in rotonda.items()])
            minimo = np.min(
                [adyacencia1[j, llega]/suma for llega, i in rotonda.items()])
            #print("Suma %s, minimo %s"%(suma,minimo))

            if not np.isnan(minimo):
                for llega, i in rotonda.items():
                    i
                    # print(int(adyacencia1[j,llega]/(suma*minimo)))

        j += 1
