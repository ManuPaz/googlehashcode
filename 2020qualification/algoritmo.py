import numpy as np
def algoritmo():
    solucion = None
    return solucion
def puntos(t, booksOfLibraries, puntosPorLibroDict, librosAñadidos):
    return np.sum([puntosPorLibroDict[i] for i in booksOfLibraries[t] if i not in librosAñadidos])
def ordenarLibros(libros, puntosPorLibroDict):
    libros.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
    return libros
# algoritmo principalmente para problemas en archivos c,e y f en los que se  pueden meter pocas librerias por tiempo
# algoritmo para elegir las librerias por tiempo sin tener mucho en cuenta los puntos que da cada libreria
def algoritmo1(infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict):
    tiempoMaximo = infogeneral["days"]
    t = 0
    solucion = {}
    solucionOrden = []
    numLibros = infogeneral["books"]
    libreriasPorLibro = {e: [] for e in puntosPorLibroDict.keys()}
    [libreriasPorLibro[e].append(libreria) for libreria, f in booksOfLibraries.items() for e in f]
    librosAñadidos = []
    librerias = list(libraryDescriptions.keys())
    puntosPorLibreria = {i: puntos(i, booksOfLibraries, puntosPorLibroDict, librosAñadidos) for i in librerias}

    while (t < tiempoMaximo and len(librerias) > 0 and len(librosAñadidos) < numLibros):
        mediaPuntosLibreria = np.mean([e for e in puntosPorLibreria.values()])
        desvPuntosLibreria = np.std([e for e in puntosPorLibreria.values()])

        librerias.sort(key=(lambda t: (libraryDescriptions[t]["signupdays"], - puntosPorLibreria[t])))
        libreria = librerias[0]

        singupdays = libraryDescriptions[libreria]["signupdays"]
        librerias.remove(libreria)
        libros1 = booksOfLibraries[libreria]
        libros1.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)

        libros = list(set.difference(set(libros1), set(librosAñadidos)))

        libros.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        solucion[libreria] = libros
        if libraryDescriptions[libreria]["signupdays"] + t < tiempoMaximo:
            diferencia = tiempoMaximo - (libraryDescriptions[libreria]["signupdays"] + t)
            librosAñadir = min(diferencia * libraryDescriptions[libreria]["booksperday"], len(libros))

            for i in range(librosAñadir):
                libro = libros[i]
                for e in libreriasPorLibro[libro]:
                    puntosPorLibreria[e] -= puntosPorLibroDict[libro]
                librosAñadidos.append(libro)

            solucionOrden.append(libreria)

        t += singupdays

    return solucion, solucionOrden, librosAñadidos
# modificacion del algoritmo1 introduciendo aletoriedad para no elegir el mejor si no uno entre los mejores
def algoritmo1VAleatorio(infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict, paramAleatoriedad=100):
    import random as ra
    tiempoMaximo = infogeneral["days"]
    t = 0
    solucion = {}
    solucionOrden = []
    numLibros = infogeneral["books"]
    libreriasPorLibro = {e: [] for e in puntosPorLibroDict.keys()}
    [libreriasPorLibro[e].append(libreria) for libreria, f in booksOfLibraries.items() for e in f]
    librosAñadidos = []
    librerias = list(libraryDescriptions.keys())
    puntosPorLibreria = {i: puntos(i, booksOfLibraries, puntosPorLibroDict, librosAñadidos) for i in librerias}

    while (t < tiempoMaximo and len(librerias) > 0 and len(librosAñadidos) < numLibros):
        librerias.sort(key=(lambda t: (libraryDescriptions[t]["signupdays"], - puntosPorLibreria[t])))
        libreria = ra.sample(librerias[:paramAleatoriedad], 1)[0]
        singupdays = libraryDescriptions[libreria]["signupdays"]
        librerias.remove(libreria)
        libros1 = booksOfLibraries[libreria]
        libros1.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        libros = list(set.difference(set(libros1), set(librosAñadidos)))
        libros.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        solucion[libreria] = libros
        if libraryDescriptions[libreria]["signupdays"] + t < tiempoMaximo:
            diferencia = tiempoMaximo - (libraryDescriptions[libreria]["signupdays"] + t)
            librosAñadir = min(diferencia * libraryDescriptions[libreria]["booksperday"], len(libros))

            for i in range(librosAñadir):
                libro = libros[i]
                for e in libreriasPorLibro[libro]:
                    puntosPorLibreria[e] -= puntosPorLibroDict[libro]
                librosAñadidos.append(libro)

            solucionOrden.append(libreria)

        t += singupdays

    return solucion, solucionOrden, librosAñadidos
# modificacion algoritmo1 teniendo mas en cuenta los puntos por libreria
def algoritmo1V2(infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict, parametroDesviacion=1):
    tiempoMaximo = infogeneral["days"]
    t = 0
    solucion = {}
    solucionOrden = []
    numLibros = infogeneral["books"]
    libreriasPorLibro = {e: [] for e in puntosPorLibroDict.keys()}
    [libreriasPorLibro[e].append(libreria) for libreria, f in booksOfLibraries.items() for e in f]
    librosAñadidos = []
    librerias = list(libraryDescriptions.keys())
    puntosPorLibreria = {i: puntos(i, booksOfLibraries, puntosPorLibroDict, librosAñadidos) for i in librerias}

    while (t < tiempoMaximo and len(librerias) > 0 and len(librosAñadidos) < numLibros):
        mediaPuntosLibreria = np.mean([e for e in puntosPorLibreria.values()])
        desvPuntosLibreria = np.std([e for e in puntosPorLibreria.values()])

        if parametroDesviacion != 0:
            librerias1 = [e for e in librerias if
                          puntosPorLibreria[e] > mediaPuntosLibreria + parametroDesviacion * desvPuntosLibreria]

            if len(librerias1) > 0:
                librerias1.sort(key=(lambda t: (libraryDescriptions[t]["signupdays"], - puntosPorLibreria[t])))
                libreria = librerias1[0]
            else:
                librerias.sort(key=(lambda t: (libraryDescriptions[t]["signupdays"], - puntosPorLibreria[t])))
                libreria = librerias[0]
        else:
            librerias.sort(key=(lambda t: (libraryDescriptions[t]["signupdays"], - puntosPorLibreria[t])))
            libreria = librerias[0]

        singupdays = libraryDescriptions[libreria]["signupdays"]
        librerias.remove(libreria)
        libros1 = booksOfLibraries[libreria]
        libros1.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        libros = list(set.difference(set(libros1), set(librosAñadidos)))

        libros.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        solucion[libreria] = libros
        if libraryDescriptions[libreria]["signupdays"] + t < tiempoMaximo:
            diferencia = tiempoMaximo - (libraryDescriptions[libreria]["signupdays"] + t)
            librosAñadir = min(diferencia * libraryDescriptions[libreria]["booksperday"], len(libros))

            for i in range(librosAñadir):
                libro = libros[i]
                for e in libreriasPorLibro[libro]:
                    puntosPorLibreria[e] -= puntosPorLibroDict[libro]
                librosAñadidos.append(libro)

            solucionOrden.append(libreria)

        t += singupdays

    return solucion, solucionOrden, librosAñadidos
# prueba sin acabar
def algoritmoConRevision(algorimo, *args):
    solucion, solucionOrden, librosAñadidos = algorimo(*args)
    return solucion, solucionOrden, librosAñadidos
# algoritmo para cuando se pueden meter muchas linbrerias, se ordena solo por puntos sin tener en cuenta el tamaño de las librerias
def algoritmo2(infogeneral, booksOfLibraries, libraryDescriptions, puntosPorLibroDict):
    tiempoMaximo = infogeneral["days"]
    t = 0
    solucion = {}
    solucionOrden = []
    numLibros = infogeneral["books"]
    libreriasPorLibro = {e: [] for e in puntosPorLibroDict.keys()}
    [libreriasPorLibro[e].append(libreria) for libreria, f in booksOfLibraries.items() for e in f]
    librosAñadidos = []
    librerias = list(libraryDescriptions.keys())
    puntosPorLibreria = {i: puntos(i, booksOfLibraries, puntosPorLibroDict, librosAñadidos) for i in librerias}

    while (t < tiempoMaximo and len(librerias) > 0 and len(librosAñadidos) < numLibros):
        librerias.sort(key=(lambda t: (- puntosPorLibreria[t])))
        libreria = librerias[0]

        singupdays = libraryDescriptions[libreria]["signupdays"]
        librerias.remove(libreria)
        libros1 = booksOfLibraries[libreria]
        libros1.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)

        libros = list(set.difference(set(libros1), set(librosAñadidos)))

        libros.sort(key=lambda t: puntosPorLibroDict[t], reverse=True)
        solucion[libreria] = libros
        if libraryDescriptions[libreria]["signupdays"] + t < tiempoMaximo:
            diferencia = tiempoMaximo - (libraryDescriptions[libreria]["signupdays"] + t)
            librosAñadir = min(diferencia * libraryDescriptions[libreria]["booksperday"], len(libros))

            for i in range(librosAñadir):
                libro = libros[i]
                for e in libreriasPorLibro[libro]:
                    puntosPorLibreria[e] -= puntosPorLibroDict[libro]
                librosAñadidos.append(libro)

            solucionOrden.append(libreria)

        t += singupdays

    return solucion, solucionOrden, librosAñadidos
