def escribirSolucion(solucion, archivo):
    solucionAEscribir = solucion
    escribirEnArchivo(solucionAEscribir, archivo)


def escribirEnArchivo(solucionProj, solucionArch, archivo):
    file = open(archivo, "w")
    file.writelines(str(len(solucionProj)))
    file.writelines("\n")

    for i, linea in enumerate(solucionProj):
        file.writelines(str(linea))
        file.writelines("\n")
        # print(linea)
        for k in solucionArch[i]:
            file.writelines(str(k))
            file.writelines(" ")

        file.writelines("\n")
    file.close()
