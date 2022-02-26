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
for archivo in archivos[0:6]:
    print(archivo)
    numContributors,numProyects, contributors, projects,skills=leerArchivo.leerArchivo("entrada/"+archivo)
    usuarios={e:0 for e in contributors.keys()}
    usuariosNivel={}
    for usuario in  usuarios:
       usuariosNivel[usuario]={}
       for nombre,skill in contributors[usuario]["skills"].items():
           nivel=skill
           usuariosNivel[usuario][nombre]=[]
           for usuario1 in skills[nombre]["usuariosArray"]:
               if skills[nombre]["usuarios"][usuario1]==nivel-1:
                   usuariosNivel[usuario][nombre].append(usuario1)
    solProjects,solUsuarios=algoritmo.algoritmo2(numContributors,numProyects, contributors, projects,skills,usuariosNivel)
    archivoSolucion="salida/solucion_"+archivo
    escribirArchivo.escribirEnArchivo(solProjects,solUsuarios,archivoSolucion)
    #print(solProjects)
    #print(solUsuarios)
   
#%%
#en el e in 
import time
for archivo in archivos:
    print(archivo)
    numContributors,numProyects, contributors, projects,skills=leerArchivo.leerArchivo("entrada/"+archivo)
    print("num contrib %s, numproyects %s "%(numContributors,numProyects))
    print("media de skills por project %s"%(np.mean([e["numroles"] for e in projects.values()])))
    print("media de skills por contrib %s"%(np.mean([e["numRoles"] for e in contributors.values()])))
    print("media de puntos por project %s"%np.mean([e["score"] for e in projects.values()]))
    print("----------------")
    
    
#archivos e y f muchos mas proyectos que contribuidores
#archivo c mas contribuidores que proyectos
#archivo e todos tienen skills 10
#
#%%   
    # print("Media de %s"%(np.mean([e for e in ])))
for archivo in archivos:  
    
      numContributors,numProyects, contributors, projects=leerArchivo.leerArchivo("entrada/"+archivo)
      for e in  projects.values():
          print (e["numroles"])
      time.sleep(0.3)
      print("-------------------")
      time.sleep(2)
      for e in  contributors.values():
          print (e["numRoles"])
      time.sleep(0.3)
      print("-------------------")
      time.sleep(5)
      
      print("###################################")
      time.sleep(2)
     
      
    

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
        

