import clases

def escribirSolucion(solucion,archivo):
    solucionAEscribir=solucion
    escribirEnArchivo(solucionAEscribir,archivo)
def escribirEnArchivo(solucionAEscribir,archivo):
    file=open(archivo,"w")
    if solucionAEscribir is not None and len( solucionAEscribir)>0:
        for linea in solucionAEscribir.values():
            if len(linea)>0:
            
                cadena=str(len(linea))+" "
                for elem in linea:
                    cadena+=(str(elem)+" ")
                cadena=cadena[:-1]
                file.writelines(cadena+"\n")
    else:
        print("Solucion vacia")
    file.close()