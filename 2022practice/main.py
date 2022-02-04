import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
import operator
#%%
archivos=["a_an_example.in.txt","b_basic.in.txt","c_coarse.in.txt","d_difficult.in.txt","e_elaborate.in.txt"]
for archivo in archivos:
    infogeneral,diccionario1,ingredientes=leerArchivo.leerArchivo("entrada/"+archivo)
    print("-----------------------------")
    print(infogeneral)
    print(np.mean([len(e["si"]) for e in diccionario1.values() ]))
    print(np.mean([len(e["no"]) for e in diccionario1.values() ]))
    print(np.mean([len(x["si"]) for x in ingredientes.values() ]))
    print(np.mean([len(x["no"]) for x in ingredientes.values() ]))
    print("-----------------------------")
#viendo las salidas se ve que en el archivo d hay que buscar maximizar por ingredientes y en el e por clientes

#%%

archivo=archivos[4]
infogeneral,diccionario1,ingredientes=leerArchivo.leerArchivo("entrada/"+archivo)
#solucion=algoritmo.algoritmo1(diccionario1,ingredientes,infogeneral[0],operator.ge)
solucion=algoritmo.algoritmo2(diccionario1,ingredientes,infogeneral[0],operator.ge,numeroInicios=30,aleatorizacionIngredientes=10)

archivoSolucion="salida/solucion_"+archivo[0]
#escribirArchivo.escribirSolucion(solucion, archivoSolucion)

#%%
import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
import operator
import time
tiempo1=time.time()
for archivo in archivos:
    
  
    
    infogeneral,diccionario1,ingredientes=leerArchivo.leerArchivo("entrada/"+archivo)
    solucion,c=algoritmo.algoritmo5(diccionario1,ingredientes,infogeneral[0],operator.ge,numeroAgrupacion=20,iteraciones=100,param1=1,param2=1,salto=50,inicios=5,aleatoriedad=100)
    print(c)
    archivoSolucion="salida/solucion_"+archivo[0]
    escribirArchivo.escribirSolucion(solucion, archivoSolucion)
tiempo2=time.time()
print("Tiempo %s"%(tiempo2-tiempo1))
    
#%%
c=0
while (c<2000):
    
    infogeneral,diccionario1,ingredientes=leerArchivo.leerArchivo("entrada/"+archivos[4])
    solucion,c=algoritmo.algoritmo2(diccionario1,ingredientes,infogeneral[0],operator.ge,numeroAgrupacion=20,iteraciones=100)
    print(c)
    archivoSolucion="salida/solucion_"+archivo[0]
    escribirArchivo.escribirSolucion(solucion, archivoSolucion)