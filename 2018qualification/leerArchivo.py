def leerArchivo(nombreArchivo):
    data = open(nombreArchivo, "r")
    numRows, numColumns, numVehicles, numRides, bonus, steps = [
        int(a) for a in data.readline().strip().split()
    ]

    input_data = [line.strip().split() for line in data]
    diccionario1 = {
        idx: {
            "origin": (int(line[0]), int(line[1])),
            "destination": (int(line[2]), int(line[3])),
            "distancia": abs(int(line[2]) - int(line[0])) + abs(int(line[3]) - int(line[1])),
            "distanciaOrigen": abs(int(line[0])) + abs(int(line[1])),
            "start": int(line[4]),
            "end": int(line[5])
        }
        for idx, line in enumerate(input_data)
    }
    return numRows, numColumns, numVehicles, numRides, bonus, steps, diccionario1
