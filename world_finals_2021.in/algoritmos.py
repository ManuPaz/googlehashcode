#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 19:48:03 2022

@author: manuel
"""
import numpy as np
import pandas as pd
import time
from itertools import combinations
#funcion que llama al algoritmo que este definido abajo

#algoritmo 
def definirCosteParaFeatures(df,servicesclase,featuresclase,binarysclase):
    for nombreFeature in df["nombre"]:
        coste=0
        binarysUsados=[]
        for servicio in  featuresclase[nombreFeature].listaServicios:
            
            if servicio.binary not in  binarysUsados:
                binarysUsados.append(servicio.binary)
                coste+=len(servicio.binary.listaservicios)
                #print(len(servicio.binary.listaservicios))
                #print(df.loc[df.nombre== nombreFeature,"dificultad"].item())
                coste+=df.loc[df.nombre== nombreFeature,"dificultad"].item()
                #coste+=len(featuresclase[nombreFeature].listaServicios)
        #print(coste)
        featuresclase[nombreFeature].dificultad=coste
        df.loc[df.nombre== nombreFeature,"costeActual"]=coste


def quedanfeatures(df):
    return len(df)>0


def agrupacionInicial(df,servicesclase,featuresclase,binarysclase,servicesvsservices,dicServices,parametroCambio=0.6):
    matrizpesos=servicesvsservices/np.sum(servicesvsservices,axis=1)
    #print(servicesvsservices)
    
    cambiados=[]
    u=np.where(matrizpesos>parametroCambio)
    arrayX=[]
    arrayY=[]
    arrayValores=[]
    for i in range(0,len(u[0])):
        arrayX.append(u[0][i])
        arrayY.append(u[1][i])
        arrayValores.append(matrizpesos[u[0][i],u[1][i]])
        #print("(%s,%s"%(u[0][i],u[1][i]))
    dataframe=pd.DataFrame({"x":arrayX,"y":arrayY,"value":arrayValores})
    dataframe.sort_values(by="value")
    while (np.max(  dataframe["value"])>0):
        u=dataframe.values[0]
        servicio1=servicesclase[dicServices[u[0]]]
        servicio2=servicesclase[dicServices[u[1]]]
        if servicio1.binary!=servicio2.binary:
           
            dataframe=dataframe.loc[(dataframe["x"]!=u[0])&(dataframe["y"]!=u[0])&(dataframe["x"]!=u[1])&(dataframe["y"]!=u[1])]
            cambiados.append([servicio1,servicio2])
            
        dataframe=dataframe.loc[(dataframe["x"]!=u[0])|(dataframe["y"]!=u[1])]
        dataframe=dataframe.loc[(dataframe["x"]!=u[1])|(dataframe["y"]!=u[0])]
        #print(u)
    return cambiados
        
        #print(dataframe)
  
#def calcularTodoConLosCambios():
              
           
def calcularCostes(trabajos,df,servicesclase,featuresclase,binarysclase,cambiados):
    #df["costeActualIng"]=np.zeros(len(df)) 
    costeAñadidoServicios=[]

    
    
        
    for feature in df.index:
        nombre=df.loc[feature,"nombre"]
        binarys=[]
        sumaAñadida=0
        for e in featuresclase[nombre].listaServicios:
            binary=e.binary
            sumaAñadida+=np.sum(trabajos["binary"]==binary.indentificador)
        df.loc[feature,"costeActualIng"]=df.loc[feature,"costeActual"]+sumaAñadida
        
    """for cambio in cambiados:
        binary0=cambio[0].binary
        binary1=cambio[1].binary
        binary0.listaServiciosCambiados=binary0.listaServicios
        binary1.listaServiciosCambiados=binary1.listaServicios
        cambio[0].binarycambio=binary1
        cambio[1].binarycambio=binary0
        costeCambio=max(len(binary0.listaservicios),len(binary1.listaservicios))
        print("Coste cambio %s"%costeCambio)
    calcularTodoConLosCambios"""
        
def calcularCosteCambio(cambio,feature,df,featureclase,trabajos):
        binary0=cambio[0].binary
        binary1=cambio[1].binary
        binary1.listaserviciosCambiados.remove(cambio[1])
        binary0.listaserviciosCambiados.append(cambio[1])
        
        cambio[1].binarycambio=binary0
        coste=max(len(binary0.listaservicios),len(binary1.listaservicios))
        suma=0
        for servicio in  featureclase.listaServicios:
            binarysUsados=[]
            binary=servicio.binary
            coste+=np.sum(trabajos["binary"]==binary.identificador)
            suma+=np.sum(trabajos["binary"]==binary.identificador)
            if servicio.binarycambio not in  binarysUsados:
                binarysUsados.append(servicio.binary)
                coste+=len(servicio.binarycambio.listaserviciosCambiados)
               
               
                coste+=df.loc[feature,"dificultad"].item()
                #coste+=len(featuresclase[nombreFeature].listaServicios)f.nombre== nombreFeature
        if coste<df.loc[feature,"costeActualIng"]:
            df.loc[feature,"costeActualIng"]=coste
            df.loc[feature,"costeActual"]=coste-suma
            cambio[1].binary=binary0
            binary1.listaServicios.remove(cambio[1])
            binary0.listaServicios.append(cambio[1])
            cambio[1].cambiado=True
            return True
            
        else:
         
            binary1.listaserviciosCambiados.append(cambio[1])
            binary0.listaserviciosCambiados.remove(cambio[1])
        
            cambio[1].binarycambio=binary1
           
            return False
            
            
            
            
        
        
    
        
        
def algoritmo(infoGeneral,dicServicesNombre,dicServices,servicesvsservices,featuresvsbinarys,servicios,serviciosvsfeatures,df,servicesclase,featuresclase,binarysclase):
     tiempoRestante=infoGeneral["numerodias"]
     trabajos=pd.DataFrame(columns=["feature","servicio","binary","dias"])
     featuresPendientes=[]
     ingenierosLibres=infoGeneral["numeroingenieros"]
     while (quedanfeatures(df) and tiempoRestante>0):
         
         while ingenierosLibres>0:
          
                 
             
         
            cambiados=agrupacionInicial(df,servicesclase,featuresclase,binarysclase,servicesvsservices,dicServices,parametroCambio=0.3)
            calcularCostes(trabajos,df,servicesclase,featuresclase,binarysclase,cambiados)
            hacerCambio=False
            featureAElimar=df.loc[df.index[0],:]
            for servicio in featuresclase[featureAElimar["nombre"]].listaServicios:
                if len(servicio.featuresImplementados)==0 and not servicio.cambiado:
                    for cambio in cambiados:
                       
                        if servicio in cambio:
                            hacerCambio=calcularCosteCambio(cambio,df.index[0],df,featuresclase[featureAElimar["nombre"]],trabajos)
                          
                            break
            if hacerCambio==False:
                k=0
              
                binarysUsados=[]
                for servicio in  featuresclase["nombre"].listaServicios:
                  
                    if  featuresclase["nombre"] not in servicio.featuresImplementados:
                        
                        if servicio.binary not in  binarysUsados:
                            ingenierosLibres-=1
                            binarysUsados.append(servicio.binary)
                            coste=featuresclase[featureAElimar["nombre"]].dificultad+np.sum(trabajos["binary"]==servicio.binary.identificador)+len(servicio.binary.servicios)
                            trabajos.loc[len(trabajos)-1]=[featureAElimar["nombre"],servicio.identificador,servicio.binary,df.loc[featureAElimar,"costeActualIng"]]
                            servicio.featuresImplementados.append(featuresclase[featureAElimar["nombre"]])
                            featuresclase[featureAElimar["nombre"]].append(servicio)
                        else:
                             servicio.featuresImplementados.append(featuresclase[featureAElimar["nombre"]])
                             featuresclase[featureAElimar["nombre"]].serviciosImplementados.append(servicio)
                        if ingenierosLibres==0:
                            break
                                
                         
                            
                    ingenierosLibres-=1
                if ingenierosLibres==0 and len(featuresclase[featureAElimar["nombre"]].serviciosImplementados)<int(featureAElimar["servicios"]):
                     featuresPendientes.append(featureAElimar["nombre"])
                    
            
            
                
            
          
            
            df.drop(df.index[0],inplace=True)
            combinaciones=combinations( featuresclase[featureAElimar["nombre"]].listaServicios,2)
            for i in (combinaciones):
               servicesvsservices[i[0].indentificador,i[1].indentificador]-=1
               servicesvsservices[i[1].indentificador,i[0].indentificador]-=1
            print(df)
              
              
          
       #  feature=features
  
    
    
    #print(np.argmin(servicesvsservices))
    
    
    
    