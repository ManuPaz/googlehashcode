import algoritmo
import leerArchivo
import escribirArchivo
import funciones
import clases
import numpy as np
import pandas as pd
#funcion para calcular los puntos de cada solucion
def calcularPuntos(solucion,rides,bonus):
    r1=[]    
    puntos=0
    bonusPoints=0
    for coche in solucion.values():
        tiempo=0
        posicionCoche=[0,0]
        for ride in coche:
           
                rid=rides[ride]
                tiempo+=algoritmo.calcularDistancia(posicionCoche,rid["origin"])
                if tiempo+rid["distancia"]<=rid["end"]:
                    puntos+=rid["distancia"]
                if tiempo<=rid["start"]:
                    puntos+=bonus
                    bonusPoints+=bonus
                tiempo+=rid["distancia"]
                posicionCoche=rid["destination"]
                    
                
            
            #esto es invalido, comprobar que no hay rides repetidos
                if ride in r1:
                    print("Repe")
                else:
                        r1.append(ride)
        
    print("Puntos %s"%puntos)
    print("Puntos por bonus %s"%bonusPoints)
    return puntos
#%%
archivos=["a_example.in","b_should_be_easy.in","c_no_hurry.in","d_metropolis.in","e_high_bonus.in"]
archivo=archivos[1]
numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s"%(numRows,numColumns,numVehicles,numRides,bonus,steps))
#%%
for archivo in archivos:
    print(archivo)
    numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
    print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s"%(numRows,numColumns,numVehicles,numRides,bonus,steps))
    distanciaMedia=np.mean([ride["distancia"] for ride in rides.values()])
    distanciaMediaOrigen=np.mean([ride["distanciaOrigen"] for ride in rides.values()])
    tiempoMedio=np.mean([ride["end"]-ride["start"] for ride in rides.values()])
    tiempoInicioMedio=np.mean([ride["start"] for ride in rides.values()])
    tiempoFinMedio=np.mean([ride["end"] for ride in rides.values()])
    tiempoInicioDesv=np.std([ride["start"] for ride in rides.values()])
    tiempoFinDesv=np.std([ride["end"] for ride in rides.values()])
    tiempoInicioMedian=np.median([ride["start"] for ride in rides.values()])
    tiempoFinMedian=np.median([ride["end"] for ride in rides.values()])
    print("Dist media %s, distancia origen %s, tiempo medio %s"%(distanciaMedia, distanciaMediaOrigen,tiempoMedio))
    print("T ini medio %s, T fin medio %s, T ini median %s, T fin median %s, T ini desv %s, T fin desv %s"
          %( tiempoInicioMedio, tiempoFinMedio,  tiempoInicioMedian,  tiempoFinMedian, tiempoInicioDesv, tiempoFinDesv))
    print("---------")
#para el c solo hay que ir a las rutas que de tiempo y tengan mas vecinos
#para e hay mucho bonus, hay que conseguir sacar muchos coches al inicio
#para el b da igual no sacarlos al inicio


#%%
numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
distancias=algoritmo.calculaDistanciaVecinos(rides)
#%%
print(np.min(distancias))
#%%
archivos=["a_example.in","b_should_be_easy.in","c_no_hurry.in","d_metropolis.in","e_high_bonus.in"]
archivo=archivos[4]
numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s"%(numRows,numColumns,numVehicles,numRides,bonus,steps))
parametroDeEspera=np.mean([ride["end"]-ride["start"] for ride in rides.values()])
#parametroDeEspera=np.mean([ride["end"]-ride["start"] for ride in rides.values()])+np.mean([ride["distanciaOrigen"] for ride in rides.values()])
#solucion=algoritmo.algoritmo1(numRows,numColumns,numVehicles,numRides,bonus,steps,rides,paramBusqueda=100,momento="end")
solucion=algoritmo.algoritmo2(numRows,numColumns,numVehicles,numRides,bonus,steps,rides,paramBusqueda=100,momento="end",parametroDeEspera=parametroDeEspera)
#a=funciones.devolverColumnaDiccionario(diccionario1, "a")
#matriz=funciones.crearmatriz((2,2),10)
print(calcularPuntos(solucion,rides,bonus))

#%%

ridesCompletos=np.sum([len(a) for a in solucion.values()])
print("Numero de rides completos %s"%ridesCompletos)
print(calcularPuntos(solucion,rides,bonus))

#%%
numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
import cProfile
cProfile.run("algoritmo.algoritmo2(numRows,numColumns,numVehicles,numRides,bonus,steps,rides,paramBusqueda=100,momento='end',parametroDeEspera=parametroDeEspera)")

#%%

#ejecucion de todos los archivos en multiprocessing
import time
import multiprocessing  as mp

def ejecutar(i,archivo, shared_list):
    puntos=0
    tiempo1=time.time()
    print(archivo)
    numRows,numColumns,numVehicles,numRides,bonus,steps,rides=leerArchivo.leerArchivo("entrada/"+archivo)
    #parametroDeEspera=np.mean([ride["distancia"] for ride in rides.values()])+np.mean([ride["distanciaOrigen"] for ride in rides.values()])
   
    parametroDeEspera=np.mean([ride["end"]-ride["start"] for ride in rides.values()])+np.mean([ride["distanciaOrigen"] for ride in rides.values()])
   
    # solucion=algoritmo.algoritmo1(numRows,numColumns,numVehicles,numRides,bonus,steps,rides,paramBusqueda=100,momento="end")
    solucion=algoritmo.algoritmo2(numRows,numColumns,numVehicles,numRides,bonus,steps,rides,paramBusqueda=100,momento="end",parametroDeEspera=parametroDeEspera)
    archivoSolucion="salida/solucion_"+archivo[0]
    escribirArchivo.escribirSolucion(solucion, archivoSolucion)
    tiempo2=time.time()
    ridesCompletos=np.sum([len(a) for a in solucion.values()])
    print("Numero de rides completos %s"%ridesCompletos)
    puntos=calcularPuntos(solucion,rides,bonus)
    
    
    print("Tiempo total %s,archivo %s"%((tiempo2-tiempo1),archivo))
    print("-------------------")
    sharedList[i]=puntos
    
sharedList=mp.Manager().list() 
process=[]
for i,archivo in enumerate(archivos):
    sharedList.append(0)

    
    process.append(mp.Process(target=ejecutar,args=[i,archivo,sharedList]))
    process[i].start()
    for proces in process:
        proces.join()
        
#%%
print(np.sum(sharedList))
