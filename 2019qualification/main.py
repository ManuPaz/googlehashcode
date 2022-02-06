import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
import trace
import sys

#%%
#resumen de los archivos para saber que algoritmo aplicar
archivos=["a_example.txt","b_lovely_landscapes.txt","c_memorable_moments.txt","d_pet_pictures.txt","e_shiny_selfies.txt"]
for archivo in archivos:
    print(archivo)
    infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivo)
    numFotos=infogeneral[0]
    numFotosVerticales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==True ])
    numFotosHorizonales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==False])
    numTags=len(diccionarioTags)
    fotosPorTag=np.mean([len(e) for e in diccionarioTags.values()] )
    tagsPorFotoDesv=np.std([e["numTags"]  for e in diccionarioFotos.values()] )
    tagsPorFoto=np.mean([e["numTags"] for e in diccionarioFotos.values()])
    #solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags,1)
    print("Fotos totales %s,verticales %s, horizonateles %s, tags totales %s"%(numFotos,numFotosVerticales,numFotosHorizonales,numTags))
    print("Media de fotos por tag %s"%( fotosPorTag  ))
    print("Media de tags por  foto %s,desv tags por foto %s"%( tagsPorFoto,tagsPorFotoDesv))
    print("---------------\n")
#%%
archivo=archivos[0]
infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivo)
diccionarioFotos1=diccionarioFotos.copy()
#solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags,1)
solucion=algoritmo.algoritmo2(infogeneral,diccionarioFotos,diccionarioTags,1,paramMinimoH=4,paramMaximoH=7,paramMinimoV=3,paramMaximoV=6,paramParada=0.05)

print(archivo)
archivoSolucion="salida/solucion_"+archivo[0]
escribirArchivo.escribirSolucion(solucion, archivoSolucion)
#%%
#print(len(solucion))
puntos=0
for i,l in enumerate(solucion[:-1]):
    tags1=set([tag for e in l for tag in diccionarioFotos1[e]["tags"]])
    tags2=set([tag for e in solucion[i+1] for tag in diccionarioFotos1[e]["tags"]])
    inter=tags1.intersection(tags2)
    puntos+=min(len(inter),len(tags2)-len(inter),len(tags1)-len(inter))
print(puntos)
#b 208803
#c 1716   
#e 276000 
#d 201000
    

#%%
infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivos[0])
#%%
#herramienta que da el tiempo total y llamadas a cada funcion
import cProfile

#perf=cProfile.run("algoritmo.algoritmo2(infogeneral,diccionarioFotos,diccionarioTags,1)")
cProfile.run("algoritmo.algoritmo2(infogeneral,diccionarioFotos,diccionarioTags,1,paramMinimoH=2,paramMaximoH=8,paramMinimoV=2,paramMaximoV=6,paramParada=0.2)")



#%%
#ejecucion de todos los archivos en multiprocessing
import time
import multiprocessing  as mp

def ejecutar(i,archivo, shared_list):
    tiempo1=time.time()
     
    infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivo)
    diccionarioFotos1=diccionarioFotos.copy()
    #solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags,1)
    solucion=algoritmo.algoritmo2(infogeneral,diccionarioFotos,diccionarioTags,1,paramMinimoH=2,paramMaximoH=8,paramMinimoV=1,paramMaximoV=7,paramParada=0.01)
    
    print(archivo)
    archivoSolucion="salida/solucion_"+archivo[0]
    escribirArchivo.escribirSolucion(solucion, archivoSolucion)
    tiempo2=time.time()
    print("Tiempo total %s,archivo %s"%((tiempo2-tiempo1),archivo))
sharedList=mp.Manager().list() 
process=[]
for i,archivo in enumerate(archivos[3:5]):
    sharedList.append(0)

    
    process.append(mp.Process(target=ejecutar,args=[i,archivo,sharedList]))
    process[i].start()
    for proces in process:
        proces.join()
        

