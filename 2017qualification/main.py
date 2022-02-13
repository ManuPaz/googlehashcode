import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
#%%
import os
archivos=os.listdir("entrada/")
archivo=archivos[1]

H,W,R,Pb,Pr,B, array,inicialPos=leerArchivo.leerArchivo("entrada/"+archivo)
matriz=np.array(array)
#%%
archivos=["charleston_road.in","lets_go_higher.in","opera.in","rue_de_londres.in"]
for archivo in archivos:

    H,W,R,Pb,Pr,B, array,inicialPos=leerArchivo.leerArchivo("entrada/"+archivo)
    print(" H %s,W %s,R %s,Pb %s,Pr %s,B %s"%(H,W,R,Pb,Pr,B))
    numCells=H*W
    
    print("Num cells %s,inicial pos %s"%(numCells,inicialPos))
    tarjets=len([ u for e in array for u in e if u=="."])
    walls=len([ u for e in array for u in e if u=="#"])
    print("Tarjets %s"%(tarjets/numCells))
    print("Walls %s"%(walls/numCells))
    matriz=np.array(array)
    t=np.where(matriz==".")
    tar=[[t[0][i],t[1][i]] for i in range(len(t[0]))]
    distanciaInicialMedia=np.mean([max(abs((t[0]-inicialPos[0])),abs(np.mean(t[1]-inicialPos[1]))) for t in tar])
    print("Dis inicial media %s"%distanciaInicialMedia)
    print("-------------")

#%%


#%%
solucion=algoritmo.algoritmo1(H,W,R,Pb,Pr,B, array,inicialPos)
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
        

