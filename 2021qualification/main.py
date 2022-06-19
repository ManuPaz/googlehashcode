import algoritmo
import escribirArchivo
import funciones
import leerArchivo
# %%
archivos = ["a.txt"]
archivo = archivos[0]
infogeneral, diccionario1, generadorParaContar = leerArchivo.leerArchivo(archivo)

# %%

v = []

# %%
solucion = algoritmo.algoritmo()
a = funciones.devolverColumnaDiccionario(diccionario1, "a")

# %%
archivoSolucion = "solucion" + archivo
escribirArchivo.escribirSolucion(solucion, archivoSolucion)
