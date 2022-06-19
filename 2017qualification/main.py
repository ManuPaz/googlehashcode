import os

import numpy as np

import algoritmo
import leerArchivo
archivos = os.listdir("entrada/")
archivo = archivos[0]

H, W, R, Pb, Pr, B, array, inicialPos = leerArchivo.leerArchivo("entrada/" + archivo)
matriz = np.array(array)
print(matriz.shape)
# %%
archivos = ["charleston_road.in", "lets_go_higher.in", "opera.in", "rue_de_londres.in"]
for archivo in archivos:
    print(archivo)
    H, W, R, Pb, Pr, B, array, inicialPos = leerArchivo.leerArchivo("entrada/" + archivo)
    print(" H %s,W %s,R %s,Pb %s,Pr %s,B %s" % (H, W, R, Pb, Pr, B))
    numCells = H * W

    print("Num cells %s,inicial pos %s" % (numCells, inicialPos))
    tarjets = len([u for e in array for u in e if u == "."])
    walls = len([u for e in array for u in e if u == "#"])
    print("Tarjets %s" % (tarjets / numCells))
    print("Walls %s" % (walls / numCells))
    matriz = np.array(array)
    t = np.where(matriz == ".")
    tar = [[t[0][i], t[1][i]] for i in range(len(t[0]))]
    distanciaInicialMedia = np.mean([max(abs((t[0] - inicialPos[0])), abs(np.mean(t[1] - inicialPos[1]))) for t in tar])
    print("Dis inicial media %s" % distanciaInicialMedia)
    print(matriz.shape)
    print("-------------")

# %%
k = 0
archivo = archivos[k]
H, W, R, Pb, Pr, B, array, inicialPos = leerArchivo.leerArchivo("entrada/" + archivo)
matriz = np.array(array)
print(archivo)
#
# 0
if k == 0:
    posicionSiguiente = (209, 110)
elif k == 1:
    posicionSiguiente = (333, 218)
elif k == 2:
    posicionSiguiente = (457, 450)
elif k == 3:
    posicionSiguiente = (509, 253)
posiciones, cable, matriz = algoritmo.algoritmo1(H, W, R, Pb, Pr, B, array, inicialPos, posicionSiguiente)

print(len(cable) * Pb + len(posiciones) * Pr)
print(len(posiciones))
for e in posiciones:
    matriz[e] = "N"
for b in cable:
    if matriz[b] != "N":
        matriz[b] = "B"

print(len(cable))
np.savetxt("archivoMatriz.txt", matriz, fmt="%c")
