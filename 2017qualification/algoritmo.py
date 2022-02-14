

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
def añadirCable(inicial,final,cable):
    dif1=abs(inicial[0]-final[0])
    dif2=abs(inicial[1]-final[1])
    coste=0
    if dif1>dif2:
        k1=0
        for k in range(dif2):
            if inicial[0]>final[0]  and inicial[1]>final[1]   :
                if (inicial[0]-k,inicial[1]-k) not in cable:
                    cable.append((inicial[0]-k,inicial[1]-k))
                    coste+=1
            if inicial[0]<final[0]  and inicial[1]>final[1]   :
             
                if (inicial[0]+k,inicial[1]-k) not in cable:
                    cable.append((inicial[0]+k,inicial[1]-k))
                    coste+=1
            if inicial[0]<final[0]  and inicial[1]<final[1]   :
                 if (inicial[0]+k,inicial[1]+k)not in cable:
                
                    cable.append((inicial[0]+k,inicial[1]+k))
                    coste+=1
            if inicial[0]>final[0]  and inicial[1]<final[1]   :
                if (inicial[0]-k,inicial[1]+k)not in cable:
                    cable.append((inicial[0]-k,inicial[1]+k))
                    coste+=1
            k1=k
        k=k1
         
                
        
        for l in range(dif2,dif1):
            if inicial[0]>final[0]  and inicial[1]>=final[1]   :
                 if (inicial[0]-k-l,inicial[1]-k) not in cable:
                    cable.append((inicial[0]-k-l,inicial[1]-k))
                    coste+=1
            if inicial[0]<final[0]  and inicial[1]>=final[1]   :
                 if (inicial[0]+k+l,inicial[1]-k) not in cable:
                    cable.append((inicial[0]+k+l,inicial[1]-k))
                    coste+=1
            if inicial[0]<final[0]  and inicial[1]<=final[1]   :
                if (inicial[0]+k+l,inicial[1]+k)not in cable:
                    cable.append((inicial[0]+k+l,inicial[1]+k))
                    coste+=1
            if inicial[0]>final[0]  and inicial[1]<=final[1]   :
                    if (inicial[0]-k-l,inicial[1]+k) not in cable:
                        cable.append((inicial[0]-k-l,inicial[1]+k))
                        coste+=1
          
            
    else:
          k1=0
          for k in range(dif1):
            if inicial[0]>final[0]  and inicial[1]>final[1]   :
                  if (inicial[0]-k,inicial[1]-k) not in cable:
                        cable.append((inicial[0]-k,inicial[1]-k))
                        coste+=1
            if inicial[0]<final[0]  and inicial[1]>final[1]   :
                   if (inicial[0]+k,inicial[1]-k) not in cable:
                        cable.append((inicial[0]+k,inicial[1]-k))
                        coste+=1
            if inicial[0]<final[0]  and inicial[1]<final[1]   :
                if (inicial[0]+k,inicial[1]+k) not in cable:
                    cable.append((inicial[0]+k,inicial[1]+k))
                    coste+=1
            if inicial[0]>final[0]  and inicial[1]<final[1]   :
                  if (inicial[0]-k,inicial[1]+k) not in cable:
                    cable.append((inicial[0]-k,inicial[1]+k))
                    coste+=1
            k1=k
          k=k1
         
                  
          for l in range(dif1,dif2):
            if inicial[0]>=final[0]  and inicial[1]>final[1]   :
                 if (inicial[0]-k,inicial[1]-k-l) not in cable:
                     cable.append((inicial[0]-k,inicial[1]-k-l))
                     coste+=1
            if inicial[0]<=final[0]  and inicial[1]>final[1]   :
                if (inicial[0]+k,inicial[1]-k-l) not in cable:
                
                    cable.append((inicial[0]+k,inicial[1]-k-l))
                    coste+=1
            if inicial[0]<=final[0]  and inicial[1]<final[1]   :
                if (inicial[0]+k,inicial[1]+k+l) not in cable:
                    cable.append((inicial[0]+k,inicial[1]+k+l))
                    coste+=1
            if inicial[0]>=final[0]  and inicial[1]<final[1]   :
                if (inicial[0]-k,inicial[1]+k+l) not in cable:
                    cable.append((inicial[0]-k,inicial[1]+k+l))
                    coste+=1
    if final not in cable:
        cable.append(final)
        coste+=1
    return coste
        
def buscar(inicalPos,matriz,R,simbolo,H,W):
  
     m1=max(inicalPos[0]-R,0)
     m2=max(0,inicalPos[1]-R)
     a1=np.where(matriz[np.ix_(range(m1,inicalPos[0]),range(m2,inicalPos[1]))]==simbolo)
     a1=list(a1)
     a1[0]+=m1
     a1[1]+=m2
     m1=max(0,inicalPos[0]-R)
     m2=inicalPos[1]+1
     a2=np.where(matriz[np.ix_(range(max(0,inicalPos[0]-R),inicalPos[0]),range(m2,min(inicalPos[1]+R+1,W)))]==simbolo)
     a2=list(a2)
     a2[0]+=m1
     a2[1]+=m2
     m1=inicalPos[0]+1
     m2=max(inicalPos[1]-R,0)
     a3=np.where(matriz[np.ix_(range(m1,min(inicalPos[0]+R+1,H)),range(m2,inicalPos[1]))]==simbolo)
     a3=list(a3)
     a3[0]+=m1
     a3[1]+=m2
     m1=inicalPos[0]+1
     m2=inicalPos[1]+1
     a4=np.where(matriz[np.ix_(range(m1,min(inicalPos[0]+R+1,H)),range(m2,min(inicalPos[1]+R+1,W)))]==simbolo)
     a4=list(a4)
     a4[0]+=m1
     a4[1]+=m2
     m1=inicalPos[0]
     m2=max(inicalPos[1]-R,0)
     a5=np.where(matriz[np.ix_(range(m1,inicalPos[0]+1),range(m2,inicalPos[1]))]==simbolo)
     a5=list(a5)
     a5[0]+=m1
     a5[1]+=m2
     m1=inicalPos[0]
     m2=inicalPos[1]+1
     a6=np.where(matriz[np.ix_(range(m1,inicalPos[0]+1),range(m2,min(inicalPos[1]+R+1,W)))]==simbolo)
     a6=list(a6)
     a6[0]+=m1
     a6[1]+=m2
     m1=max(inicalPos[0]-R,0)
     m2=inicalPos[1]
     a7=np.where(matriz[np.ix_(range(m1,inicalPos[0]),range(m2,inicalPos[1]+1))]==simbolo)
     a7=list(a7)
     a7[0]+=m1
     a7[1]+=m2
     m1=inicalPos[0]+1
     m2=inicalPos[1]
     a8=np.where(matriz[np.ix_(range(m1,min(inicalPos[0]+R+1,H)),range(m2,inicalPos[1]+1))]==simbolo)
     a8=list(a8)
     a8[0]+=m1
     a8[1]+=m2
    
    
     
     return  a1,a2,a3,a4,a5,a6,a7,a8
def calcularCubiertos(inicalPos,matriz,R,H,W):
     import time
     a1,a2,a3,a4,a5,a6,a7,a8= buscar(inicalPos,matriz,R,"#",H,W)
    
     b1,b2,b3,b4,b5,b6,b7,b8= buscar(inicalPos,matriz,R,".",H,W)
     cubiertos=0
     for b,a in zip([b1,b2,b3,b4,b5,b6,b7,b8],[a1,a2,a3,a4,a5,a6,a7,a8]):
          #print(b)
          #time.sleep(2)
          if len(a[0])==0 and len(b[0])>0:
             cubiertos+=len(b[0])
          elif  len(a[0])>0  and  len(b[0])>0:
           
           
           
            if a[0][0]>=inicalPos[0] and a[1][0]>=inicalPos[0]:
                minimoX=np.min(a[0])   
                minimoY=np.min(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX or b[1][i]<=minimoY ]
                cubiertos+=len(b)
            elif a[0][0]>=inicalPos[0] and  a[1][0]<inicalPos[0]:
                minimoX=np.min(a[0])   
                minimoY=np.max(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX or b[1][i]>=minimoY ]
                cubiertos+=len(b)
            elif a[0][0]<inicalPos[0] and a[1][0]>=inicalPos[0]:
                minimoX=np.max(a[0])   
                minimoY=np.min(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]>=minimoX or b[1][i]<=minimoY ]
                cubiertos+=len(b)
            elif a[0][0]<inicalPos[0] and  a[1][0]<inicalPos[0]:
                minimoX=np.max(a[0])   
                minimoY=np.max(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX or b[1][i]<=minimoY ]
                cubiertos+=len(b)
             
     return cubiertos
             
     
     
def calcularPosicionesCubiertas(inicalPos,matriz,R,H,W):
     a1,a2,a3,a4,a5,a6,a7,a8= buscar(inicalPos,matriz,R,"#",H,W)
     b1,b2,b3,b4,b5,b6,b7,b8= buscar(inicalPos,matriz,R,".",H,W)
     cubiertos=[]
     for b,a in zip([b1,b2,b3,b4,b5,b6,b7,b8],[a1,a2,a3,a4,a5,a6,a7,a8]):
         if len(a[0])==0 and len(b[0])>0:
            
            
             cubiertos+=[(b[0][i],b[1][i]) for i in range(len(b[0]))]
             
         elif  len(a[0])>0 and len(b[0])>0:
         
          
           
            if a[0][0]>=inicalPos[0] and  a[1][0]>=inicalPos[0]:
                minimoX=np.min(a[0])   
                minimoY=np.min(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX or b[1][i]<=minimoY ]
                cubiertos+=[(b[0][i],b[1][i]) for i in u]
            elif a[0][0]>=inicalPos[0] and  a[1][0]<inicalPos[0]:
                minimoX=np.min(a[0])   
                minimoY=np.max(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX or b[1][i]>=minimoY ]
                cubiertos+=[(b[0][i],b[1][i]) for i in u]
            elif a[0][0]<inicalPos[0] and  a[1][0]>=inicalPos[0]:
                minimoX=np.max(a[0])   
                minimoY=np.min(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]>=minimoX or b[1][i]<=minimoY ]
                cubiertos+=[(b[0][i],b[1][i]) for i in u]
            elif a[0][0]<inicalPos[0] and  a[1][0]<inicalPos[0]:
                minimoX=np.max(a[0])   
                minimoY=np.max(a[1])
                
                u=[i for i in range(len(b[0])) if b[0][i]<=minimoX  or b[1][i]<=minimoY ]
                cubiertos+=[(b[0][i],b[1][i]) for i in u]
             
             
     return cubiertos
    
#charleston_road.in

def calcularPosicinesNuevas(inicalPos,matriz,R,diccionario1,diccionario,H,W,posiciones1):
    
    inicalPos=list(inicalPos)
    pos=inicalPos.copy()
    
    pos[1]+=2*R
    
     
    ini=diccionario1[tuple(inicalPos)]
    pos=tuple(pos)
  
    
    if pos[1]<W and (matriz[pos]=="-" or matriz[pos]==".") and tuple(pos)!=tuple(ini):
        if pos not in posiciones1:
            posiciones1.append(pos)
            diccionario1[pos]=inicalPos
            diccionario[pos]=calcularCubiertos(pos,matriz,R,H,W)
    pos=inicalPos.copy()
    pos[1]-=2*R
    pos=tuple(pos)
    if pos[1]>0 and (matriz[pos]=="-" or matriz[pos]==".") and tuple(pos)!=tuple(ini):
        if pos not in posiciones1:
            posiciones1.append(pos)
            diccionario1[pos]=inicalPos
            diccionario[pos]=calcularCubiertos(pos,matriz,R,H,W)
    pos=inicalPos.copy()
   
    pos[0]+=2*R
  
    pos=tuple(pos)
    if pos[0]<H and (matriz[pos]=="-" or matriz[pos]==".") and tuple(pos)!=tuple(ini):
         if pos not in posiciones1:
            posiciones1.append(pos)
            diccionario1[pos]=inicalPos
            diccionario[pos]=calcularCubiertos(pos,matriz,R,H,W)
    pos=inicalPos.copy()
    pos[0]-=2*R
    pos=tuple(pos)
    if pos[0]>0 and (matriz[pos]=="-" or matriz[pos]==".") and tuple(pos)!=tuple(ini):
         if pos not in posiciones1:
            posiciones1.append(pos)
            diccionario1[pos]=inicalPos
            diccionario[pos]=calcularCubiertos(pos,matriz,R,H,W)
    
        
    
def algoritmo1(H,W,R,Pb,Pr,B, array,inicialPos,posicionSiguiente):
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

    posiciones=[]
    siguiente=posicionSiguiente
    
    diccionario={}
    diccionario1={}
    diccionario1[tuple(inicialPos)]=(-100,-11)
    diccionario1[siguiente]=tuple(inicialPos)
    posicionesNuevas=[]
    #diccionario[inicialPos]=calcularCubiertos(inicialPos,matriz,R)
    cable=[]
    posicion=inicialPos
    posiciones.append(tuple(posicion))
   
    posicionesCubiertas=calcularPosicionesCubiertas(posicion,matriz,R,H,W)
    for e in posicionesCubiertas:
        matriz[e]="+" 
    while(B>0):
        
        distancia=añadirCable(posicion, siguiente, cable)
        posiciones.append(siguiente)
        calcularPosicinesNuevas(siguiente,matriz,R,diccionario1,diccionario,H,W,posicionesNuevas)
       
        
        posicionesNuevas.sort(key=lambda t:diccionario[t],reverse=True)
        #print(posicionesNuevas)
        siguiente=posicionesNuevas[0]
        diccionario.pop(siguiente)
        posicionesNuevas.remove(siguiente)
        
        
        posicion=diccionario1[siguiente]
       
                
            
               
                
        
    
            
        
        
        posicionesCubiertas=calcularPosicionesCubiertas(siguiente,matriz,R,H,W)
        #print(siguiente)
        for e in posicionesCubiertas:
          
            matriz[e]="+"
            #print(e)
        B-=distancia*Pb+Pr
        
        print(B)
    return posiciones,cable,matriz
        
        
        
        
    