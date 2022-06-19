import numpy as np

import algoritmo
import escribirArchivo
import leerArchivo
# %%
# informacion de los archivos para saber que algoritmo utizar
archivos = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt",
            "f_libraries_of_the_world.txt"]
for archivo in archivos:
    print(archivo)
    infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo(
        "entrada/" + archivo)
    print(infogeneral)

    media = np.mean([e["signupdays"] for e in libraryDescriptions.values()])
    desv = np.std([e["signupdays"] for e in libraryDescriptions.values()])
    minimo = (np.min([e["signupdays"] for e in libraryDescriptions.values()]))
    maximo = np.max([e["signupdays"] for e in libraryDescriptions.values()])
    print("Puntos medios por libor %s" % (np.mean([e for e in puntosPorLibroDict.values()])))
    print("Mean %s" % media)
    print("Media -desv %s" % (media - desv))
    print("Media + desv %s" % (media + desv))
    print("Min %s" % (minimo))
    print("Max %s" % (maximo))
    print("last %s" % (infogeneral["days"] / media))
    mediaLibros = np.mean([e["numbooks"] for e in libraryDescriptions.values()])
    print("Media libraos %s" % mediaLibros)
    """mediaSubidaLibros=np.mean([e["booksperday"] for e in libraryDescriptions.values() ])
    mediaLibros=np.mean([e["numbooks"] for e in libraryDescriptions.values() ])
    idx1=[e for  e,i in  libraryDescriptions.items() if i["signupdays"]<=media-desv]
    idx2=[e for  e,i in  libraryDescriptions.items() if i["signupdays"]>=media+desv]
    mediaBajosTiempoSubida=np.mean([e["booksperday"] for i,e in libraryDescriptions.items() if i in idx1 ])
    mediaAltosTiempoSubida=np.mean([e["booksperday"] for i,e in libraryDescriptions.items() if i in idx2])
    mediaBajosNumBooks=np.mean([e["numbooks"] for i,e in libraryDescriptions.items() if i in idx1 ])
    mediaAltosNumBooks=np.mean([e["numbooks"] for i,e in libraryDescriptions.items() if i in idx2])"""

    print("--------------------------------")
    print("\n")

# %%
# prueba de calculo de la solucion para archivo de prueba
archivos = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt",
            "f_libraries_of_the_world.txt"]
archivo = archivos[0]
infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo("entrada/" + archivo)

solucion, solucionOrden = algoritmo.algoritmo1(infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict)

archivoSolucion = "salida/solucion_" + archivo[0]
escribirArchivo.escribirEnArchivo(solucion, solucionOrden, archivoSolucion)

# %%
# calculo de soluciones especialmente para archivo d
import time
for archivo in archivos:
    tiempo1 = time.time()
    infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo(
        "entrada/" + archivo)

    solucion, solucionOrden, librosAñadidos = algoritmo.algoritmo2(infogeneral, booksOfLibraries, libraryDescriptions,
                                                                   puntosPorLibroDict)

    archivoSolucion = "salida/solucion_" + archivo[0]
    escribirArchivo.escribirEnArchivo(solucion, solucionOrden, archivoSolucion)
    tiempo2 = time.time()
    suma = np.sum([puntosPorLibroDict[k] for k in librosAñadidos])
    print("Archivo %s,puntos %s,Tiempo %s" % (archivo, suma, tiempo2 - tiempo1))

# %%
# calculo de soluciones para archivos diferentes del d
import time
sumaT = 0
for archivo in archivos[0:3] + archivos[4:]:
    tiempo1 = time.time()
    infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo(
        "entrada/" + archivo)

    solucion, solucionOrden, librosAñadidos = algoritmo.algoritmo1(infogeneral, booksOfLibraries, libraryDescriptions,
                                                                   puntosPorLibroDict)

    archivoSolucion = "salida/solucion_" + archivo[0]
    escribirArchivo.escribirEnArchivo(solucion, solucionOrden, archivoSolucion)
    tiempo2 = time.time()
    suma = np.sum([puntosPorLibroDict[k] for k in librosAñadidos])
    sumaT += suma
    print("Archivo %s,puntos %s,Tiempo %s,sumaT %s (Millones)" % (archivo, suma, tiempo2 - tiempo1, sumaT / 1000000))

# %%
# prueba algoritmo revisando la solucion
import time
for archivo in archivos[0:3] + archivos[4:]:
    tiempo1 = time.time()
    infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo(
        "entrada/" + archivo)

    solucion, solucionOrden, librosAñadidos = algoritmo.algoritmoConRevision(algoritmo.algoritmo1, infogeneral,
                                                                             booksOfLibraries, libraryDescriptions,
                                                                             puntosPorLibroDict)

    archivoSolucion = "salida/solucion_" + archivo[0]
    escribirArchivo.escribirEnArchivo(solucion, solucionOrden, archivoSolucion)
    tiempo2 = time.time()
    suma = np.sum([puntosPorLibroDict[k] for k in librosAñadidos])
    print("Archivo %s,puntos %s,Tiempo %s" % (archivo, suma, tiempo2 - tiempo1))

# %%
# optimizacion del parametro de desviacion tipica con multiprocessing
# multiprocessing es el modulo para crear varios procesos
# se pasa una lista en zona de memoria comun creandola con  sharedList=mp.Manager().list()
import multiprocessing as mp
parametros = [2, -1, -0.5, -0.2, -0.1, -0.05, 0, 0.05, 0.1, 0.2, 0.5, 1, 2]
sumaT = 0
def ejecutar(i, parametro, archivo, shared_list):
    infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict = leerArchivo.leerArchivo(
        "entrada/" + archivo)

    solucion, solucionOrden, librosAñadidos = algoritmo.algoritmo1V2(infogeneral, booksOfLibraries, libraryDescriptions,
                                                                     puntosPorLibroDict, parametro)

    suma = np.sum([puntosPorLibroDict[k] for k in librosAñadidos])
    shared_list[i] = suma
for archivo in archivos[0:3] + archivos[4:]:
    sharedList = mp.Manager().list()
    [sharedList.append(0) for p in parametros]
    process = []
    for i, parametro in enumerate(parametros):
        process.append(mp.Process(target=ejecutar, args=[i, parametro, archivo, sharedList]))
        process[i].start()
    for proces in process:
        proces.join()

    print(sharedList)
    sumaT += max(sharedList)
    print(sumaT)

# %%

print(sumaT + 5028010)
