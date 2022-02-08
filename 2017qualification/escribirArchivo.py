import clases

def escribirSolucion(solucion,archivo):
    solucionAEscribir=solucion
    escribirEnArchivo(solucionAEscribir,archivo)
def escribirEnArchivo(solucionAEscribir,archivo):
    file=open(archivo,"w")
    if solucionAEscribir is not None and len( solucionAEscribir)>0:
        file.writelines(numCellsBackbone+"\n")
        for cellB in numCellsBackbone:
            file.writelines( + " " + +"\n")
        file.writelines(numCellsRouters+"\n")
        for cellR in numCellsRouters:
            file.writelines( + " " + +"\n")
    else:
        print("Solucion vacia")
    file.close()
