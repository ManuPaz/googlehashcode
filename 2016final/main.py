import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
NOVENTA=324000
CIENTOOCHENTA=324000*2
#%%
import os
archivos=os.listdir("entrada/")
print(archivos)
archivo=archivos[0]
duracion,numSatelites,numCollections,diccionarioSatelites,diccionarioColecciones,dicImagenes=leerArchivo.leerArchivo("entrada/"+archivo)
dicImagenesAux={i:e for i,e in enumerate(dicImagenes.keys())}

#%%
def distancia(a,b,v):
    
    
    if a[0]>0 and b[0]>0 and v<0:
        
        return abs(b[0]-a[0])+(abs(b[1]-a[1]))
    elif if a[0]>0 and b[0]>0 and v<0:
        return abs(b[0])+abs(NOVENTA-a[0])+(abs(b[1]-a[1]))
        
def posiciones(a,b,v):
    if a[0]+v>NOVENTA:
        a[0]=CIENTOOCHENTA-(a[0]+v)
        a[1]=-CIENTOOCHENTA+(a[1]-15)
        v=-v
    elif a[0]+v<NOVENTA:
        a[0]=-CIENTOOCHENTA-(a[0]+v)
        a[1]=-CIENTOOCHENTA+(a[1]-15)
        v=-v
    else:
        a[0]=(a[0]+v)
        a[1]=a[1]-15
        
        
                  
    
    return a,v
    
distancias=np.zeros((len(diccionarioSatelites),len(dicImagenes)))
for clave,valor in (diccionarioSatelites.items()):
    for clave1,valor1 in (dicImagenesAux.items()):
        distancias[clave,clave1]=distancia(valor["pos"],valor1,valor["v"])
    

#%%
def distancia(a,b,v):
        
        return abs(b[0]-a[0])/v+(abs(b[1]-a[1]))/15
for archivo in archivos:
    print(archivo)
    duracion,numSatelites,numCollections,diccionarioSatelites,diccionarioColecciones,dicImagenes=leerArchivo.leerArchivo("entrada/"+archivo)
    print("Dur %s, num satelites %s, num collections %s"%(duracion,numSatelites,numCollections))
    print("Collections por imagen %s, numero de imagenes %s, imagenes por coleccion %s"%(np.mean([len(e) for e in dicImagenes.values()]),len(dicImagenes.keys()),\
                                                                                         np.mean([e["numLocations"]for e in diccionarioColecciones.values()])))
    print("Tiempo de deteccion %s"%(np.mean([np.sum([u[1]-u[0] for u in e["timeRanges"]]) for e in diccionarioColecciones.values()])))
    print("Rotacion camara %s, max rotacion camara %s"%(np.mean([e["w"] for e in diccionarioSatelites.values()]),np.mean([e["d"] for e in diccionarioSatelites.values()])))
    dicImagenesAux={i:e for i,e in enumerate(dicImagenes.keys())}

    
    distancias=np.zeros((len(diccionarioSatelites),len(dicImagenes)))
    for clave,valor in (diccionarioSatelites.items()):
        for clave1,valor1 in (dicImagenesAux.items()):
            distancias[clave,clave1]=distancia(valor["pos"],valor1,valor["v"])
    print("---------------")
    
#   forever_alone.in da igual el tiempo


#%%
solucion=algoritmo.algoritmo1(duracion,numSatelites,numCollections,diccionarioSatelites,diccionarioColecciones)
#a=funciones.devolverColumnaDiccionario(diccionario1, "a")
#matriz=funciones.crearmatriz((2,2),10)

#%%
archivoSolucion="salida/solucion_"+archivo[0]
escribirArchivo.escribirSolucion(solucion, archivoSolucion)

#%%
import cProfile
cProfile.run("algoritmo.algoritmo()")

#%%

#ejecucion de todos los archivos en multiprocessing
import time
import multiprocessing  as mp

def ejecutar(i,archivo, shared_list):
    puntos=0
    tiempo1=time.time()
    print(archivo)
    infogeneral,diccionario1=leerArchivo.leerArchivo("entrada/"+archivo)
    solucion=algoritmo.algoritmo()
    archivoSolucion="salida/solucion_"+archivo[0]
    escribirArchivo.escribirSolucion(solucion, archivoSolucion)
    tiempo2=time.time()
    
    print("Tiempo total %s,archivo %s"%((tiempo2-tiempo1),archivo))
    sharedList[i]=puntos
    
sharedList=mp.Manager().list() 
process=[]
for i,archivo in enumerate(archivos):
    sharedList.append(0)

    
    process.append(mp.Process(target=ejecutar,args=[i,archivo,sharedList]))
    process[i].start()
    for proces in process:
        proces.join()
        

