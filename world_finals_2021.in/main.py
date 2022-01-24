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
import pandas as pd
from itertools import combinations
import features as fea 
#entrada de datos con modulo entradadatos
nombres=["an_example.txt","breadth_of_choice.txt","five_thousand.txt","distinction.txt","five_thousand.txt","constrained_optimisation"]
nombreArchivo=nombres[0]
PRINT=True
infogeneral,servicios,arrayfeaturesServices,features=entradaDatos.entradaDatos(nombreArchivo)
featuresvsbinarys=np.zeros(shape=(infogeneral["numerofeatures"],infogeneral["numerobinaries"]))
featuresvsservices=np.zeros(shape=(infogeneral["numerofeatures"],infogeneral["numeroservicios"]))
servicesvsbinarys=np.zeros(shape=(infogeneral["numeroservicios"],infogeneral["numerobinaries"]))
servicesvsservices=np.zeros(shape=(infogeneral["numeroservicios"],infogeneral["numeroservicios"]))
dicServices={}
dicServicesNombre={}
dicFeatures={}
print(infogeneral)
j=0
localizacionFeatures={}

for i,e in servicios.items():
    dicServices[j]=i
    dicServicesNombre[i]=j
    j+=1
for j in range(0,infogeneral["numerofeatures"]):
    for servicio in  arrayfeaturesServices[j]:
        featuresvsbinarys[j,servicios[servicio]]+=1
        

    
df = pd.DataFrame.from_records(features)
        

#df=df.set_index(0)
df.columns=["nombre","servicios","dificultad","beneficio"]

df["beneficio"]=pd.to_numeric(df["beneficio"])
df["dificultad"]=pd.to_numeric(df["dificultad"])
df=df.sort_values(by=["beneficio"],ascending=False)
#print(df.tail())
servicesvsservices

for j in range(0,infogeneral["numerofeatures"]):
    combinaciones=combinations(arrayfeaturesServices[j],2)
    for i in (combinaciones):
        servicesvsservices[dicServicesNombre[i[0]],dicServicesNombre[i[1]]]+=1
        servicesvsservices[dicServicesNombre[i[1]],dicServicesNombre[i[0]]]+=1
j=0        
featuresclase={}
servicesclase={}
binarysclase={}
for aux in df.values:
    feat=fea.feature(j,aux[0], aux[3],aux[2], aux[1], [])
    featuresclase[aux[0]]=feat
    
    for aux1 in arrayfeaturesServices[j]:
        if not aux1 in  servicesclase.keys():
            servaux=fea.servicio(dicServicesNombre[aux1],aux1)
            servicesclase[aux1]=(servaux)
        else:
            servaux=  servicesclase[aux1]
            
        servaux.features.append(feat)
        feat.listaServicios.append(servaux)
        if servicios[aux1] not in binarysclase:
            auxbinary=fea.binary(servicios[aux1])
            binarysclase[servicios[aux1]]=( auxbinary)
        else:
            auxbinary=binarysclase[servicios[aux1]]
        if not   servaux in auxbinary.listaservicios:
            auxbinary.listaservicios.append( servaux)
            auxbinary.listaserviciosCambiados.append( servaux)
        servaux.binary= auxbinary
        servaux.binarycambio= auxbinary
    j+=1
j=0
for service,binary in servicios.items():
    binary=int(binary)
    if service not in servicesclase:
        servaux=fea.servicio(dicServicesNombre[service],service)
        servicesclase[service]=(servaux)
        auxbinary=fea.binary(binary)
        binarysclase[binary]=( auxbinary)
        auxbinary.listaservicios.append( servaux)
        servaux.binary= auxbinary
        servaux.binarycambio= auxbinary
        
        
#print(len(servicesclase))   
#print(len(featuresclase))  
#print(len(binarysclase))   


df["costeActual"]=np.zeros(len(df))
df["costeConCambio"]=np.zeros(len(df))
df["costeActualIng"]=np.zeros(len(df))
algoritmos.definirCosteParaFeatures(df,servicesclase,featuresclase,binarysclase)
#algoritmos.anadirCosteIngenieros(df,servicesclase,featuresclase,binarysclase)
algoritmos.agrupacionInicial(df,servicesclase,featuresclase,binarysclase,servicesvsservices,dicServices)
print(df.tail())
algoritmos.algoritmo(infogeneral,dicServicesNombre,dicServices,servicesvsservices,featuresvsbinarys,servicios,arrayfeaturesServices,df,servicesclase,featuresclase,binarysclase)

 
    

#%%inspeccion del problems
algoritmos.inspeccionarCaminos(adyacencia,adyacencia1,incidencia,cochesvsinteresecciones,cars,rotondas)
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




