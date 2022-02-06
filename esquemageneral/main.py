import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
#%%
archivos=["a_example.txt"]
archivo=archivos[0]
infogeneral,diccionario1,generadorParaContar=leerArchivo.leerArchivo("entrada/"+archivo)

#%%
solucion=algoritmo.algoritmo()
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
        

