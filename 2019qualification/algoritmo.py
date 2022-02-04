

import pandas as pd
import numpy as np
import funciones
import itertools

def algoritmo():
    solucion=None
    return solucion


def algoritmo1(infogeneral,diccionarioFotos,diccionarioTags):
    numFotos=infogeneral[0]
    numFotosVerticales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==True ])
    numFotosHorizonales=len([e for e,i in diccionarioFotos.items() if i["vertical"]==False])
    numTags=len(diccionarioTags)
    fotosPorTag=np.mean([len(e) for e in diccionarioTags.values()] )
    tagsPorFoto=np.mean([e["numTags"] for e in diccionarioFotos.values()])
    
    slices={idx:[e] for idx,e in enumerate(diccionarioFotos.keys())}
    grupos=[list((slic,)) for slic in slices.keys()]
       
    tagsPorGrupo=[set([k for e in grupo1 for j in slices[e] for k in diccionarioFotos[e]["tags"]])for grupo1 in grupos]
         
    while 1:
        pass
       
        
    
    return grupos
    
    
    
    