import clases

def escribirSolucion(solucion,archivo):
    solucionAEscribir=solucion
    escribirEnArchivo(solucionAEscribir,archivo)
def escribirEnArchivo(solucionAEscribir,archivo):
    file=open(archivo,"w")
    if solucionAEscribir is not None and len( solucionAEscribir)>0:
        for linea in solucionAEscribir:
            if isinstance(linea, int) or isinstance(linea, float) or isinstance(linea, str):
                file.writelines(str(linea)+"\n")
            #print(linea)
            else:
                cadena=""
                for elem in linea:
                    cadena+=(str(elem)+" ")
                cadena=cadena[:-1]
                file.writelines(cadena+"\n")
    else:
        print("Solucion vacia")
    file.close()