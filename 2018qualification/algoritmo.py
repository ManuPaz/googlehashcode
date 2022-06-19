import numpy as np
def algoritmo():
    solucion = None
    return solucion
def calculaDistanciaVecinos(rides):
    num = len(rides.keys())
    matriz = np.zeros((num, num))
    matriz.fill(-1)
    for i in range(num):
        if i % 10 == 0:
            print(i)
        for j in range(num):
            if matriz[j, i] == -1:
                matriz[j, i] = abs(rides[i]["origin"][0] - rides[j]["destination"][0]) + abs(
                    rides[i]["origin"][1] - rides[j]["destination"][1]) + abs(
                    rides[i]["destination"][0] - rides[j]["origin"][0]) + abs(
                    rides[i]["destination"][1] - rides[j]["origin"][1])

            else:
                matriz[i, j] = matriz[j, i]

    return matriz
def calcularDistancia(punto1, punto2):
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])
# algoritmo para el c


def algoritmo1(numRows, numColumns, numVehicles, numRides, bonus, steps, rides, paramBusqueda=100, paramParada=100000,
               momento="start"):
    print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s" %
          (numRows, numColumns, numVehicles, numRides, bonus, steps))

    ridesList = [ride for ride in rides.keys()]

    tiempo = 0

    coches = [[[0, 0], 0] for idx in range(numVehicles)]
    coches = np.array(coches, dtype=object)
    solucion = {idx: [] for idx in range(numVehicles)}

    intersec1 = None
    while (tiempo < steps and len(ridesList) > 0):
        cochesLibres = np.where(coches[:, 1] == tiempo)
        for l in (cochesLibres[0]):
            coche = coches[l]

            intersec = coche[0]
            if intersec1 is None or intersec != intersec1:
                distancias = {ride: calcularDistancia(
                    rides[ride]["origin"], intersec) for ride in ridesList}
                ridesList.sort(key=lambda t: distancias[t])

            for k, ride in enumerate(ridesList):
                ride1 = rides[ride]
                dist = distancias[ride]
                if k > paramParada:
                    break
                if momento == "start":
                    if tiempo + dist <= ride1["start"]:
                        solucion[l].append(ride)
                        coches[l, 0] = ride1["destination"]
                        coches[l, 1] = ride1["start"] + ride1["distancia"]
                        ridesList.remove(ride)
                        break

                elif momento == "end":
                    if tiempo + dist + ride1["distancia"] < ride1["end"]:
                        coches[l, 0] = ride1["destination"]
                        solucion[l].append(ride)
                        ridesList.remove(ride)
                        if tiempo + dist >= ride1["start"]:
                            coches[l, 1] = tiempo + ride1["distancia"] + dist

                        else:
                            coches[l, 1] = ride1["start"] + ride1["distancia"]
                        break
        tiempo += 1

    return solucion

    return solucion, coches
# algoritmo para tener en cuenta tambien si queda mucho
# probamos añadidiendo un parametro de espera
def algoritmo2(numRows, numColumns, numVehicles, numRides, bonus, steps, rides, paramBusqueda=100, paramParada=100000,
               momento="start", parametroDeEspera=None):
    print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s" %
          (numRows, numColumns, numVehicles, numRides, bonus, steps))
    ridesList = [ride for ride in rides.keys()]

    tiempo = 0

    coches = [[[0, 0], 0] for idx in range(numVehicles)]
    coches = np.array(coches, dtype=object)
    solucion = {idx: [] for idx in range(numVehicles)}

    intersec1 = None
    while (tiempo < steps and len(ridesList) > 0):
        cochesLibres = np.where(coches[:, 1] == tiempo)
        for l in list(cochesLibres[0]):
            coche = coches[l]

            intersec = coche[0]

            if intersec1 is None or intersec != intersec1:
                distancias = {ride: calcularDistancia(
                    rides[ride]["origin"], intersec) for ride in ridesList}
                ridesList.sort(key=lambda t: distancias[t])

            for k, ride in enumerate(ridesList):
                ride1 = rides[ride]
                dist = distancias[ride]
                if k > paramParada:
                    break
                if tiempo + parametroDeEspera > ride1["start"]:
                    if momento == "start":
                        if tiempo + dist <= ride1["start"]:
                            solucion[l].append(ride)
                            coches[l, 0] = ride1["destination"]
                            coches[l, 1] = ride1["start"] + ride1["distancia"]
                            ridesList.remove(ride)
                            break

                    elif momento == "end":
                        if tiempo + dist + ride1["distancia"] < ride1["end"]:
                            coches[l, 0] = ride1["destination"]
                            solucion[l].append(ride)
                            ridesList.remove(ride)
                            if tiempo + dist >= ride1["start"]:
                                coches[l, 1] = tiempo + ride1["distancia"] + dist

                            else:
                                coches[l, 1] = ride1["start"] + ride1["distancia"]
                            break
        tiempo += 1

    return solucion
# algoritmo que ademas tiene en cuenta si la calle tiene mas calles cerca
def algoritmo3(numRows, numColumns, numVehicles, numRides, bonus, steps, rides, paramBusqueda=100, paramParada=100000,
               momento="start", parametroDeEspera=None):
    print("R %s, C %s, V %s, Rides %s, Bonus %s, time %s" %
          (numRows, numColumns, numVehicles, numRides, bonus, steps))
    ridesList = [ride for ride in rides.keys()]

    tiempo = 0

    coches = [[[0, 0], 0] for idx in range(numVehicles)]
    coches = np.array(coches, dtype=object)
    solucion = {idx: [] for idx in range(numVehicles)}

    intersec1 = None
    while (tiempo < steps and len(ridesList) > 0):
        cochesLibres = np.where(coches[:, 1] == tiempo)
        for l in list(cochesLibres[0]):
            coche = coches[l]

            intersec = coche[0]

            if intersec1 is None or intersec != intersec1:
                distancias = {ride: abs(rides[ride]["start"] - calcularDistancia(
                    rides[ride]["origin"], intersec) - rides[ride]["distancia"] - tiempo) for ride in ridesList}
                ridesList.sort(key=lambda t: distancias[t])

            for k, ride in enumerate(ridesList):
                ride1 = rides[ride]
                dist = distancias[ride]
                if k > paramParada:
                    break
                if tiempo + parametroDeEspera > ride1["start"]:
                    if momento == "start":
                        if tiempo + dist <= ride1["start"]:
                            solucion[l].append(ride)
                            coches[l, 0] = ride1["destination"]
                            coches[l, 1] = ride1["start"] + ride1["distancia"]
                            ridesList.remove(ride)
                            break

                    elif momento == "end":
                        if tiempo + dist + ride1["distancia"] < ride1["end"]:
                            coches[l, 0] = ride1["destination"]
                            solucion[l].append(ride)
                            ridesList.remove(ride)
                            if tiempo + dist >= ride1["start"]:
                                coches[l, 1] = tiempo + ride1["distancia"] + dist

                            else:
                                coches[l, 1] = ride1["start"] + ride1["distancia"]
                            break
        tiempo += 1

    return solucion
