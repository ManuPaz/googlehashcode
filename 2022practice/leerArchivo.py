def leerArchivo(nombreArchivo):
    data = open(nombreArchivo, "r")

    infogeneral = {}
    cabecera = [
        int(a) for a in data.readline().strip().split()
    ]

    input_data = [line.strip().split() for line in data]
    diccionario1 = {
        idx: {
            "si": input_data[2 * idx][1:],
            "no": input_data[2 * idx + 1][1:]
        }
        for idx in range(len(input_data) // 2)
    }
    ingredientes = {e: {"si": [], "no": []} for x in diccionario1.values() for e in x["si"] + x["no"]}
    [ingredientes[e]["si"].append(i) for i, x in diccionario1.items() for e in x["si"]]
    [ingredientes[e]["no"].append(i) for i, x in diccionario1.items() for e in x["no"]]
    return cabecera, diccionario1, ingredientes
