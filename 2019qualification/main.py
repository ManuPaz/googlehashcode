import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
#%%
archivos=["a_example.txt","b_lovely_landscapes.txt","c_memorable_moments.txt","d_pet_pictures.txt","e_shiny_selfies.txt"]
archivo=archivos[1]
infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivo)
numFotos=infogeneral[0]
numFotosVerticales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==True ])
numFotosHorizonales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==False])
print("Fotos totales %s,verticales %s, horizonateles %s"%(numFotos,numFotosVerticales,numFotosHorizonales))

#%%
solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags)
#a=funciones.devolverColumnaDiccionario(diccionario1, "a")
#matriz=funciones.crearmatriz((2,2),10)

#%%
archivos=["a_example.txt","b_lovely_landscapes.txt","c_memorable_moments.txt","d_pet_pictures.txt","e_shiny_selfies.txt"]
for archivo in archivos:
    print(archivo)
    infogeneral,diccionarioFotos,diccionarioTags=leerArchivo.leerArchivo("entrada/"+archivo)
    numFotos=infogeneral[0]
    numFotosVerticales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==True ])
    numFotosHorizonales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==False])
    numTags=len(diccionarioTags)
    fotosPorTag=np.mean([len(e) for e in diccionarioTags.values()] )
    tagsPorFoto=np.mean([e["numTags"] for e in diccionarioFotos.values()])
    solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags)
    print("Fotos totales %s,verticales %s, horizonateles %s, tags totales %s"%(numFotos,numFotosVerticales,numFotosHorizonales,numTags))
    print("Media de fotos por tag %s"% fotosPorTag)
    print("Media de tags por  foto %s"% tagsPorFoto)
    print("---------------\n")
#en los que hay fotos verticales hay que ver como se juntan primero para tener el mayor numero de fotos distintas y mas relaciones con el resto
#en e;muchas verticales y muchas fotos por tag, hay que juntar bien las fotos teniendo en cuenta con que otras fotos se van a juntar despues
#en d igual a e,pero hay horizontales
#en c hay horizontales pero menos tags por foto: al agrupar solo hay que conseguir muchos tags en cada slice
#en b no hay verticales, solo hay que preocuparse de comos se juntan


#prueba de hierarchical clustering
#%%



#%%
solucion=algoritmo.algoritmo1(infogeneral,diccionarioFotos,diccionarioTags)
#a=funciones.devolverColumnaDiccionario(diccionario1, "a")
#matriz=funciones.crearmatriz((2,2),10)

#%%
archivoSolucion="salida/solucion_"+archivo[0]
escribirArchivo.escribirSolucion(solucion, archivoSolucion)

