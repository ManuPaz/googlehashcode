

import pandas as pd
import numpy as np
import funciones
import itertools
import collections


      
    
    
class Slice:
    def __init__(self,fotos,tags,fotosRel):
        self.fotos=fotos
        self.tags=tags
        self.fotosRel=fotosRel
    
    
def eliminarFoto(foto,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto):
    [diccionarioTags[e].remove(foto) for e in tagsPorFoto[foto]]
    fotos.remove(foto)
    if diccionarioFotos[foto]["vertical"]:
        diccionarioFotosVerticales.pop(foto)
    else:
             diccionarioFotosHorizontales.pop(foto)
    diccionarioFotos.pop(foto)
   
    
        
        
        
    
#algoritmo cuando no hay tantos tags por foto y se pueden contar todos    
def algoritmo1(infogeneral,diccionarioFotos,diccionarioTags,archivo="arch",verticales=True,semilla=1,parametroCorte=0.5,paramParada=0.05):
    import random
    random.seed(semilla)
    fotos=[foto for foto in diccionarioFotos.keys()]
    fotos.sort(key=lambda t:len(diccionarioFotos[t]["tags"]))
    slices=[]
    solucion=[]
    foto1=fotos[0]
    tagsPorFoto={e:set(foto["tags"]) for e,foto in diccionarioFotos.items()}
    parada=len(fotos)

    diccionarioFotosVerticales={e:u for e,u in diccionarioFotos.items() if u["vertical"]}
    diccionarioFotosHorizontales={e:u for e,u in diccionarioFotos.items() if not  u["vertical"]}

    if diccionarioFotos[foto1]["vertical"]:
       for k in (diccionarioFotos.keys()):
        
           foto2=k
          
          
           if not diccionarioFotos[foto2]["vertical"]:
               solucion.append([foto2])
               eliminarFoto(foto2,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
               
               break;
           else:
               if len(tagsPorFoto[foto2].intersection(tagsPorFoto[foto1]))==0:
                    solucion.append([foto1,foto2])
                    eliminarFoto(foto1,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
                    eliminarFoto(foto2,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
                    break;
    else:
         solucion.append([foto1])
         eliminarFoto(foto1,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
    
    import time
    tiempo1=time.time()
    while(len(fotos))>0:
        parada=len(fotos)*paramParada
        if len(fotos)%2000==0:
            
            tiempo2=time.time()
            print("Tiempo %s, numero de fotos %s, archivo %s"%(tiempo2-tiempo1,len(fotos),archivo))
            tiempo1=tiempo2
        sliceA=solucion[0]
        sliceB=solucion[-1]
        diccionario={}
        for i,slic in enumerate([sliceA,sliceB]):
            if len(slic)==1:
                tags=tagsPorFoto[slic[0]]
            else:
                 tags=tagsPorFoto[slic[0]].union(tagsPorFoto[slic[1]])
                
            
            candidatos=contador=collections.Counter([foto for tag in tags for foto in diccionarioTags[tag]])
           
            suma1=len(tags)
           
            if len(candidatos.keys())==0:
               
                  candidatos[(fotos[0])]=0
                  
         
            candidatos=list((dict.fromkeys(candidatos)))
            contador2={t:len(tagsPorFoto[t])for t in candidatos}
            
            
          
          
            cont={t:np.min([contador[t],suma1-contador[t],contador2[t]-contador[t]]) for t in candidatos}
            candidatos.sort(key=lambda t:cont[t],reverse=True)
            candidato1=candidatos[0]
            tags1=tagsPorFoto[candidato1]
            candidatos.remove(candidato1)
          
            if not diccionarioFotos[candidato1]["vertical"]:
                diccionario[i]=[[candidato1],cont[candidato1]]
            else:
                candidato2=None
                candidatos2=[e for e in candidatos if  diccionarioFotos[e]["vertical"]]
                
                if len (candidatos2)>0:
                    
                     tagsAux={e:(tags1.union(tagsPorFoto[e])) for e in candidatos2}
                     contador2={e:len(tagsAux[e].intersection(tags)) for e in candidatos2}
                     
                     
                     
                     
                     cont={t:min([(contador2[t]),suma1-(contador2[t]),len(tagsAux[t])-contador[t]]) for t in candidatos2}
                     
                     candidatos2.sort(key=lambda t:cont[t],reverse=True)
                     candidato2=candidatos2[0]
                    
                     if cont[candidato2]<=0:
                         candidato2=None
                         
                    
                
                if candidato2 is None and len(diccionarioFotosVerticales)>0:
                        k=0
                        for foto,e in diccionarioFotosVerticales.items():
                            #print(foto)
                            if foto!=candidato1 and len(set.intersection(set(e["tags"]), set(tags1)))<=parametroCorte*len(set(e["tags"])):
                                candidato2=foto
                                break
                            k+=1
                            if k>parada:
                                break
                if candidato2 is None:
                     candidatos=[e for e in candidatos if  not diccionarioFotos[e]["vertical"]]
                     if len (candidatos)>0:
                         candidato1=candidatos[0]
                     else:
                         if len(diccionarioFotosHorizontales)>0:
                            candidato1=list(diccionarioFotosHorizontales.keys())[0]
                         else:
                             lista= list(diccionarioFotosVerticales.keys())
                             if lista[0]!=candidato1:
                                 candidato2=lista[0]
                             else:
                                 candidato2=lista[1]
                                 
                if candidato2 is None:
                          tags2=tagsPorFoto[candidato1]
                          suma2=len(tags.intersection(tags2))
                          minimo=min([suma1-suma2,suma2,len(tags2)-suma2])
                          diccionario[i]=[[candidato1],minimo]
                         
                else:
                          tags2=tagsPorFoto[candidato1].union(tagsPorFoto[candidato2])
                          suma2=len(tags.intersection( tags2))
                          minimo=min([suma1-suma2,suma2,len(tags2)-suma2])
                          diccionario[i]=[[candidato1,candidato2],minimo]
                          
           
        u=max(diccionario,key=lambda t:diccionario[t][1])
       
        for foto in diccionario[u][0]:
                
                 eliminarFoto(foto,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
        if u==0:
            solucion.insert(0, diccionario[u][0])
           
        else:
            solucion.append(diccionario[u][0])
     
            
            
                
                
    return solucion
    
    
  
            
        
        
        
        
            
        
 
 #algoritmo para cuando hay muchos tags por foto y es mejor ir con parametros predeterminados   
def algoritmo2(infogeneral,diccionarioFotos,diccionarioTags,archivo="arch",verticales=True,semilla=1,parametroCorte=0.5,paramParada=0.05,paramMinimoH=3,paramMaximoH=8,paramMinimoV=2,paramMaximoV=7):
    import random
    random.seed(semilla)
    fotos=[foto for foto in diccionarioFotos.keys()]
    fotos.sort(key=lambda t:len(diccionarioFotos[t]["tags"]))
    slices=[]
    solucion=[]
    foto1=fotos[0]
    tagsPorFoto={e:set(foto["tags"]) for e,foto in diccionarioFotos.items()}
    
    
    parada=len(fotos)

    diccionarioFotosVerticales={e:u for e,u in diccionarioFotos.items() if u["vertical"]}
    diccionarioFotosHorizontales={e:u for e,u in diccionarioFotos.items() if not  u["vertical"]}

    if diccionarioFotos[foto1]["vertical"]:
       for k in (diccionarioFotos.keys()):
        
           foto2=k
          
          
           if not diccionarioFotos[foto2]["vertical"]:
               solucion.append([foto2])
               eliminarFoto(foto2,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
               
               break;
           else:
               if len(tagsPorFoto[foto2].intersection(tagsPorFoto[foto1]))==0:
                    solucion.append([foto1,foto2])
                    eliminarFoto(foto1,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
                    eliminarFoto(foto2,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
                    break;
    else:
         solucion.append([foto1])
         eliminarFoto(foto1,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
    
    import time
    tiempo1=time.time()
    while(len(fotos))>0:
        parada=len(fotos)*paramParada
        if len(fotos)%1000==0:
         
            tiempo2=time.time()
            print("Tiempo %s, numero de fotos %s, archivo %s"%(tiempo2-tiempo1,len(fotos),archivo))
            tiempo1=tiempo2
        sliceA=solucion[0]
        sliceB=solucion[-1]
        diccionario={}
        for i,slic in enumerate([sliceA,sliceB]):
            if len(slic)==1:
                tags=tagsPorFoto[slic[0]]
            else:
                 tags=tagsPorFoto[slic[0]].union(tagsPorFoto[slic[1]])
            lon=len(tags)
            slice2=None
            #fotos=random.sample(fotos,len(fotos))
            verticalPendiente=None
            tags3=None
            puntos=0
            for k,foto in enumerate(set([e for tag in tags for e in diccionarioTags[tag]])):
                tags2=tagsPorFoto[foto]
                if not diccionarioFotos[foto]["vertical"]:
                    inter=tags.intersection(tags2)
                    if len(inter)<=paramMaximoH and len(inter)>=paramMinimoH:
                        puntos=min([len(inter),len(tags)-len(inter),len(tags2)-len(inter)])
                        diccionario[i]=[[foto],puntos]
                        break
                    elif len(inter)<=paramMaximoH+2 and len(inter)>=paramMinimoH-2:
                        slice2=[foto]
                        puntos==min([len(inter),len(tags)-len(inter),len(tags2)-len(inter)])
                else:
                  
                    if not  verticalPendiente is None:
                         inter=tags.intersection(tags2.union(tags3))
                    else:
                         inter=tags.intersection(tags2)
                        
                    if len(inter)<=paramMaximoV and len(inter)>=paramMinimoV:
                        if not  verticalPendiente is None:
                              puntos=min([len(inter),len(tags)-len(inter),len(tags2.union(tags3))-len(inter)])
                              diccionario[i]=[[foto,verticalPendiente],puntos]
                              break
                            
                        else:
                            verticalPendiente=foto
                            tags3=tags2
                    
                        
                    
                
                if k>=len(fotos)*paramParada:
                   
                    break
            if i not in diccionario.keys():
                
                if not slice2  is None:
                      diccionario[i]=[slice2,puntos]
                
                else:
                    for l,foto in enumerate(fotos):
                         if not diccionarioFotos[foto]["vertical"]:
                             tags2=tagsPorFoto[foto]
                             inter=tags.intersection(tags2)
                             puntos=min([len(tags)-len(inter),len(tags2)-len(inter),len(inter)])
                             diccionario[i]=[[foto],puntos]
                             break
                         else:
                              for l1,foto1 in enumerate(fotos[l+1:]):
                                    if diccionarioFotos[foto1]["vertical"]:
                                     tags2=tagsPorFoto[foto1].union(tagsPorFoto[foto])
                                     inter=tags.intersection(tags2)
                                     puntos=min([len(tags)-len(inter),len(tags2)-len(inter),len(inter)])
                                     diccionario[i]=[[foto,foto1],puntos]
                                     break
                              break
                             
                        
                    
                
          
                          
        #print(diccionario)
        u=max(diccionario,key=lambda t:diccionario[t][1])
       
        for foto in diccionario[u][0]:
                
                 eliminarFoto(foto,fotos,diccionarioTags,diccionarioFotos,diccionarioFotosVerticales,diccionarioFotosHorizontales,tagsPorFoto)
        if u==0:
            solucion.insert(0, diccionario[u][0])
           
        else:
            solucion.append(diccionario[u][0])
     
            
            
    return solucion
                
                
                    
                    
       
       
       
        
    
   
    
    
    
    