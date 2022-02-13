

import pandas as pd
import numpy as np
import funciones
import itertools

def algoritmo():
    solucion=None
    return solucion



def calcularDistancia(matriz,inicialPos):
    t=np.where(matriz==".")
    tar=[[t[0][i],t[1][i]] for i in range(len(t[0]))]
    distanciaInicialMedia=([abs((t[0]-inicialPos[0]))+abs(np.mean(t[1]-inicialPos[1])) for t in tar])
    
def algoritmo1(H,W,R,Pb,Pr,B, array,inicialPos):
    solucion1=[]
    solucion2=[]
   
    print(" H %s,W %s,R %s,Pb %s,Pr %s,B %s"%(H,W,R,Pb,Pr,B))
    numCells=H*W
    
    print("Num cells %s,inicial pos %s"%(numCells,inicialPos))
    numtarjets=len([ u for e in array for u in e if u=="."])
    numwalls=len([ u for e in array for u in e if u=="#"])
    print("Tarjets %s"%(numtarjets/numCells))
    print("Walls %s"%(numwalls/numCells))
    matriz=np.array(array)
    t=np.where(matriz==".")
    tar=[[t[0][i],t[1][i]] for i in range(len(t[0]))]
    
    distanciaInicialMedia=np.mean([max(abs((t[0]-inicialPos[0])),abs(np.mean(t[1]-inicialPos[1]))) for t in tar])
    print("Dis inicial media %s"%distanciaInicialMedia)
    
    
    
    
    