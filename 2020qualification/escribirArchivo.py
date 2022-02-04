import clases

def escribirSolucion(solucion,archivo):
    solucionAEscribir=solucion
    escribirEnArchivo(solucionAEscribir,archivo)
    
#esta parte cambia un poco dependiendo del problema
#la forma general esta en esquema general
#en este caso es un poco distinta
#solucion es un diccionario  que tiene de claves el numero de la libreria y de valor un array con todos los libros que se añaden en esa libreria por orden
#solucionOrden tiene los numeros de libreria ordenados, porque en solucion al ser un diccionario no estan ordenados    
def escribirEnArchivo(solucion,solucionOrden,archivo):
    file=open(archivo,"w")
    if solucionOrden is not None and len( solucionOrden)>0:
        file.writelines(str(len(solucionOrden))+"\n")
        
        for linea in solucionOrden:
            
            file.writelines(str(linea)+" "+str(len(solucion[linea]))+"\n")
            #print(linea)
            cadena=""
            for e in solucion[linea]:
                    cadena+=str(e)+" "
            cadena=cadena[:-1]        
            file.writelines(cadena+"\n")
                
           
    else:
        print("Solucion vacia")
    file.close()