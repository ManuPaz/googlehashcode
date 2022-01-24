import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
#%%
archivos=["a.txt"]
archivo=archivos[0]
infogeneral,diccionario1,generadorParaContar=leerArchivo.leerArchivo(archivo)

#%%
#creacion de arrays de clases
v=[]
#v=[clases.clase(j,u[0]) for j,u in zip(range(len(diccionario1)),diccionario1.items())]
#v=[clases.clase(j,u[1]["a"]) for j,u in zip(range(len(diccionario1)),diccionario1.items())]
#devolver array ordenado por campo en dict
#calles=list(diccionario1.keys())
#calles=funciones.devolverListaOrdenada(calles, diccionario1)
#devolver dataframe de diccionario
#dataframe=funciones.crearDataFrame(diccionario1).transpose()
#%%
solucion=algoritmo.algoritmo()
a=funciones.devolverColumnaDiccionario(diccionario1, "a")
#matriz=funciones.crearmatriz((2,2),10)

#%%
archivoSolucion="solucion"+archivo
escribirArchivo.escribirSolucion(solucion, archivoSolucion)

