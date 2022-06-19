def escribirEnArchivo(a, b, archivo):
    file = open(archivo, "w")

    file.writelines(len(a) + "\n")
    for cellB in a:
        file.writelines(cellB[0] + " " + cellB[1] + "\n")
    file.writelines(len(b) + "\n")
    for cellR in b:
        file.writelines(cellR[0] + " " + cellR[1] + "\n")

    file.close()
