#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:22:14 2022

@author: manuel
"""
import numpy as np
def computarpuntos(nombreArchivoSolucion,nombreArchivoInicial,sumaPuntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False):
    archivoFinal=open(nombreArchivoSolucion)
    archivoInicial=open(nombreArchivoInicial)
    lineasInicial=archivoInicial.readlines()
    lineasFinal=archivoFinal.readlines()
    cabecera=np.array(lineasInicial[0].split(" "),dtype=int)
    numerocalles=cabecera[2]
    rotonas=[]
    numerointersecciones=cabecera[1]
    numerocoches=cabecera[3]
    puntosPorCoche=cabecera[4]
    segundosTotales=cabecera[0]
    
    cars=[lin.strip() .split(" ")for lin in lineasInicial[(numerocalles+1):]]
    lineasfinal=lineasFinal[1:]
    lineasfinal=lineasfinal[::-1]
    intersec=[]
    rotondas=[]
    ll=0
    while(1):
        try:
            u=lineasfinal.pop()
           
            
        except:
            break
        
        
        
      
        numero=lineasfinal.pop()
        j=0
        suma=0
        while ll<=int(u):
            rotondas.append(0)
            intersec.append({})
            ll+=1
        #print(numero)
        while(j<int(numero)):
            vv=lineasfinal.pop().split(" ")
            l=int(vv[1])
            intersec[len(intersec)-1][vv[0]]=suma
            #print(l)
            suma+=l
             
            j+=1
        rotondas[len(rotondas)-1]=(suma)
    #print(len(intersec))   
    i=0
    puntos=0
    segundosPorCoche=np.zeros(shape=( numerocoches))
    for coche in cars:
        #print(i)
        segundosActuales=0
        j=0
        rotondaInicial=cochesvsinteresecciones[i][0]
        
        #print( max(segundosPorCoche[interseccionesvscohes[rotondaInicial]]))
        segundosActuales+=max(segundosPorCoche[interseccionesvscohes[rotondaInicial]])
        l=0
        for rotonda in cochesvsinteresecciones[i][0:-1]:
            calle=coche[1+j]
            #print(rotonda)
            longciclo=rotondas[rotonda]
            
            seg=segundosActuales%longciclo
           
            esp=intersec[rotonda][calle]-seg
            array=np.array(list(intersec[rotonda].keys()))
           
            indice=np.where(array==calle)
            indice=int(indice[0])
            if indice==len(array)-1:
                duracion=longciclo-intersec[rotonda][calle]
            else:
                duracion=intersec[rotonda][array[indice+1]]-intersec[rotonda][calle]
        
           
            if esp>=0:
                espera=esp
            elif intersec[rotonda][calle]+duracion-seg-1<0:
                espera=longciclo-seg+intersec[rotonda][calle]
            else:
                espera=0
            
            j+=1
            segundosActuales+=espera
            calle=coche[1+j]
            if j>0:
                segundosActuales+=int(calles[dicCalles[calle]][3])
            if PRINT:
                print("Calle %s, espera %s, segundos actuales %s, duracion intervalo %s "%(calle,espera,segundosActuales,duracion))
               
            if l==0:
                segundosPorCoche[i]=(espera+1)
            if PRINT:
                print("----------------")
            l+=1
        if PRINT:
                print("####################")
        
        if segundosActuales<=segundosTotales:  
            
            #print(segundosActuales)
            puntos+=(segundosTotales-segundosActuales+ puntosPorCoche)
        #print(segundosPorCoche)
            
            
        i+=1
    if PRINT:
        print("Puntos finales %s"%puntos)
    sumaPuntos+=puntos
    return sumaPuntos