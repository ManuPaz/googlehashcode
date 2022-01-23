#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:39:55 2022

@author: manuel
"""

from multiprocessing import Process,Array

def ejecutarTodosLosArchivos(nombres,parametros):
    import entradaDatos
    import pandas as pd
    import numpy as np
    import computarpuntos
    import escribirEnArchivo
    import time
    import algoritmos
    
    sumaPuntos=0
    PRINT=False
    for nombreArchivo in nombres:
        cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
       
        solucionAEscribir,solucion=algoritmos.algoritmo(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)
        escribirEnArchivo.escribirEnArchivo2(solucionAEscribir,"solucion.txt")
        #escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
       
        sumaPuntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,sumaPuntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
    print(sumaPuntos)
    
    
def ejecutarTodosLosArchivosMP(nombres,parametros):
    import entradaDatos
    import pandas as pd
    import numpy as np
    import computarpuntos
    import escribirEnArchivo
    import time
    import algoritmos
    
    sumaPuntos=0
    PRINT=True
    i=0
    arrayPuntos=Array("d",range(len(nombres)))
    procesos=[]
    for nombreArchivo in nombres:
            p = Process(target=ejecutar, args=(nombreArchivo,1,i,PRINT,arrayPuntos))
            p.start()
            procesos.append(p)
          
            i+=1
    for p in procesos:
                p.join()
          
            
            
    puntosTotales=np.sum(arrayPuntos)
    print("Puntos totales %s"%puntosTotales)
    
    
    
   
    
def ejecutarPorArchivo(nombres,parametrosArg,PRINT):
    import entradaDatos
    import pandas as pd
    import numpy as np
    import computarpuntos
    import escribirEnArchivo
    import time
    import algoritmos
    diccionarioParametrosOptimos={}
    for  nombreArchivo in nombres: 
        diccionarioParametrosOptimos[nombreArchivo]=0
        arrayPuntos=np.zeros(shape=(len(parametrosArg)))
        i=0
        for parametro in parametrosArg:
            parametros={}
            parametro=parametro[0]
            
            cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
            parametros={}
            parametros["ciclo"]=15
            parametros["tiempoPorCalle"]=parametro
            solucionAEscribir,solucion=algoritmos.algoritmo0(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)
            escribirEnArchivo.escribirEnArchivo2(solucionAEscribir,"solucion.txt")
            #escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
            puntos=0
            puntos=computarpuntos.computarpuntos("solucion.txt",nombreArchivo,puntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
            arrayPuntos[i]=puntos
            if PRINT:
                print("Archivo %s, parametro %s, puntos %s"%(nombreArchivo,parametro,puntos))
            i+=1
        diccionarioParametrosOptimos[nombreArchivo]=parametrosArg[np.argmax( arrayPuntos)][0]
    return  diccionarioParametrosOptimos
            
            
def ejecutar(nombreArchivo,parametro,i,PRINT,arrayPuntos): 
            import entradaDatos
            import pandas as pd
            import numpy as np
            import computarpuntos
            import escribirEnArchivo
            import time
            import algoritmos
            cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars=entradaDatos.entradaDatos(nombreArchivo)
            parametros={}
            parametros["ciclo"]=15
            parametros["tiempoPorCalle"]=parametro
            solucionAEscribir,solucion=algoritmos.algoritmo(cabecera,numerocalles,numerocoches,numerointersecciones,adyacencia,incidencia,adyacencia1,incidencia1,interseccionesvscohes,cochesvsinteresecciones,rotondas,calles,dicCalles,arrayCalles,cars,**parametros)
            escribirEnArchivo.escribirEnArchivo2(solucionAEscribir,"solucion"+str(i)+".txt")
            #escribirEnArchivo.escribirEnArchivo(incidencia,arrayCalles,numerointersecciones)
            puntos=0
            puntos=computarpuntos.computarpuntos("solucion"+str(i)+".txt",nombreArchivo,puntos,cochesvsinteresecciones,calles,dicCalles,interseccionesvscohes,PRINT=False)
            arrayPuntos[i]=puntos
            if PRINT:
                print("Archivo %s, parametro %s, puntos %s"%(nombreArchivo,parametro,arrayPuntos[i]))
           
def ejecutarPorArchivoMP(nombres,parametrosArg,PRINT):
    diccionarioParametrosOptimos={}
    import numpy as np
    for  nombreArchivo in nombres: 
        diccionarioParametrosOptimos[nombreArchivo]=0
        arrayPuntos=Array("d",range(len(parametrosArg)))
        i=0
        procesos=[]
        for parametro in parametrosArg:
            parametros={}
            parametro=parametro[0]
            p = Process(target=ejecutar, args=(nombreArchivo,parametro,i,PRINT,arrayPuntos))
            p.start()
            procesos.append(p)
          
            i+=1
        for p in procesos:
            p.join()
          
            
            
        diccionarioParametrosOptimos[nombreArchivo]=parametrosArg[np.argmax( arrayPuntos)][0]
    return  diccionarioParametrosOptimos
            
    