def escribirSolucion(solucion, archivo):
    solucionAEscribir = solucion
    escribirEnArchivo(solucionAEscribir, archivo)
def escribirEnArchivo(solucionAEscribir, archivo):
    file = open(archivo, "w")

    if solucionAEscribir is not None and len(solucionAEscribir) > 0:
        file.writelines(str(len(solucionAEscribir)) + "\n")
        for linea in solucionAEscribir:
            for e in linea:
                file.writelines(str(e) + " ")
            file.writelines("\n")

    else:
        print("Solucion vacia")
    file.close()
