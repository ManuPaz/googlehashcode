import clases

def escribirEnArchivo(a, b, archivo):
    file=open(archivo,"w")
    if solucionAEscribir is not None and len( solucionAEscribir)>0:
        file.writelines(len(a)+"\n")
        for cellB in a:
            file.writelines( cellB[0]+ " " + cellB[1]+"\n")
        file.writelines(len(b)+"\n")
        for cellR in b:
            file.writelines( cellR[0]+ " " + cellR[1]+"\n")
    else:
        print("Solucion vacia")
    file.close()
