import numpy as np


def algoritmo():
    solucion = None
    return solucion


def algoritmo1(numContributors, numProyects, contributors, projects, skills, usuariosNivel):
    # guarda el tiempo al que esta disponible el usuari0
    usuariosTiempo = {e: 0 for e in contributors.keys()}
    usuariosArray = [e for e in contributors.keys()]
    # array depryectos ordnados por tiempo
    proyectosTiempo = [e for e in projects.keys()]
    proyectosTiempoDisponible = {e: [0, ""] for e in projects.keys()}
    # array de proyectos ordenados por puntuacion
    proyectosPuntuacion = [e for e in projects.keys()]
    proyectosTiempo.sort(key=lambda t: projects[t]["days"])
    proyectosPuntuacion.sort(key=lambda t: projects[t]["score"], reverse=True)
    skillsTiempoMaximo = {e: 0 for e in skills.keys()}
    solucionProyects = []
    solucionUsuarios = []
    while (1):
        addProject = True

        usuariosAdd = []
        [skill["usuariosArray"].sort(key=lambda t: usuariosTiempo[t]) for skill in skills.values()]
        proyectoElegido = proyectosPuntuacion[0]
        proyectoElegidoValor = projects[proyectoElegido]
        for i, skill in enumerate(proyectoElegidoValor["roles"]):
            nivel = proyectoElegidoValor["levels"][i]
            usuarios = [clave for clave, valor in skills[skill]["usuarios"].items() if
                        valor >= nivel and clave not in usuariosAdd]
            for us in usuariosAdd:
                if skill in usuariosNivel[us]:
                    usuarios = (usuarios) + usuariosNivel[us][skill]
            usuarios = list(set(usuarios) - set(usuariosAdd))
            if (len(usuarios) > 0):
                usuario = usuarios[0]
                usuariosAdd.append(usuario)
                usuariosTiempo[usuario] = usuariosTiempo[usuario] + proyectoElegidoValor["days"]





            else:
                addProject = False
                break
        if addProject:
            l = 0
            for i, skill in enumerate(proyectoElegidoValor["roles"]):
                nivel = proyectoElegidoValor["levels"][i]

                usuario = usuariosAdd[l]
                l += 1

                if skills[skill]["usuarios"][usuario] < nivel:
                    skills[skill]["usuarios"][usuario] += 1
                usuariosTiempo[usuario] = usuariosTiempo[usuario] + proyectoElegidoValor["days"]

                array = [usuariosTiempo[usuario1] for usuario1, valor in skills[skill]["usuarios"].items() if
                         valor >= nivel]

                maximo = np.min(array)

                for e, valor in skills[skill]["proyectos"].items():
                    maximo1 = np.max(valor)
                    if maximo1 >= nivel:
                        if maximo > proyectosTiempoDisponible[e][0]:
                            proyectosTiempoDisponible[e] = [maximo, skill]

        if addProject:
            solucionProyects.append(proyectoElegido)
            solucionUsuarios.append(usuariosAdd)
        proyectosTiempo.sort(
            key=lambda t: projects[t]["daybefore"] + projects[t]["days"] - proyectosTiempoDisponible[t][0],
            reverse=True)
        if proyectosTiempoDisponible[proyectosTiempo[0]][0] < 0:
            break
        proyectosPuntuacion.remove(proyectoElegido)
        proyectosPuntuacion1 = [t for t in proyectosPuntuacion if
                                projects[t]["daybefore"] + projects[t]["days"] - proyectosTiempoDisponible[t][0] > 0]
        proyectosPuntuacion = proyectosPuntuacion1
        proyectosPuntuacion.sort(key=lambda t: projects[t]["score"], reverse=True)
        if len(proyectosPuntuacion) == 0:
            break

    return solucionProyects, solucionUsuarios


def algoritmo2(numContributors, numProyects, contributors, projects, skills, usuariosNivel):
    # guarda el tiempo al que esta disponible el usuari0
    usuariosTiempo = {e: 0 for e in contributors.keys()}
    # array depryectos ordnados por tiempo
    proyectosTiempo = [e for e in projects.keys()]
    proyectosTiempoDisponible = {e: [0, ""] for e in projects.keys()}
    # array de proyectos ordenados por puntuacion
    proyectosPuntuacion = [e for e in projects.keys()]
    proyectosPuntuacionDict = {e: valor["score"] for e, valor in projects.items()}
    proyectosPuntuacion.sort(key=lambda t: proyectosPuntuacionDict[t])
    proyectosTiempo.sort(key=lambda t: projects[t]["days"])
    proyectosPuntuacion.sort(key=lambda t: projects[t]["score"], reverse=True)
    skillsTiempoMaximo = {e: 0 for e in skills.keys()}
    solucionProyects = []
    solucionUsuarios = []

    while (1):
        addProject = True

        usuariosAdd = []
        [skill["usuariosArray"].sort(key=lambda t: usuariosTiempo[t]) for skill in skills.values()]
        proyectoElegido = proyectosPuntuacion[0]

        proyectoElegidoValor = projects[proyectoElegido]

        proyectosAEliminar = []
        tiempo = proyectoElegidoValor["daybefore"] + proyectoElegidoValor["score"] - proyectoElegidoValor["days"]
        for i, skill in enumerate(proyectoElegidoValor["roles"]):
            nivel = proyectoElegidoValor["levels"][i]
            usuarios = [clave for clave, valor in skills[skill]["usuarios"].items() if
                        valor >= nivel and clave not in usuariosAdd and usuariosTiempo[clave] < tiempo]
            for us in usuariosAdd:
                if skill in usuariosNivel[us] and skills[skill]["usuarios"][us] == nivel:
                    usuarios = (usuarios) + usuariosNivel[us][skill]
            usuarios = list(set(usuarios) - set(usuariosAdd))

            if (len(usuarios) > 0):
                usuario = usuarios[0]
                usuariosAdd.append(usuario)
                usuariosTiempo[usuario] = usuariosTiempo[usuario] + proyectoElegidoValor["days"]





            else:
                addProject = False

                break
        if addProject:
            l = 0
            for i, skill in enumerate(proyectoElegidoValor["roles"]):
                nivel = proyectoElegidoValor["levels"][i]

                usuario = usuariosAdd[l]
                l += 1

                if skills[skill]["usuarios"][usuario] < nivel:
                    skills[skill]["usuarios"][usuario] += 1
                temp = usuariosTiempo[usuario] + proyectoElegidoValor["days"]
                usuariosTiempo[usuario] = temp

                array = [usuariosTiempo[usuario1] for usuario1, valor in skills[skill]["usuarios"].items() if
                         valor >= nivel]

                maximo = np.min(array)

                if temp == maximo:
                    for e, valor in skills[skill]["proyectos"].items():
                        maximo1 = np.max(valor)
                        if maximo1 >= nivel:
                            if maximo > proyectosTiempoDisponible[e][0]:
                                proyectosTiempoDisponible[e] = [maximo, skill]
                                if projects[e]["daybefore"] + projects[e]["score"] - projects[e]["days"] - maximo < 0:
                                    proyectosAEliminar.append(e)

        if addProject:
            solucionProyects.append(proyectoElegido)
            solucionUsuarios.append(usuariosAdd)

        proyectosPuntuacion.remove(proyectoElegido)

        if len(proyectosPuntuacion) == 0:
            break

    return solucionProyects, solucionUsuarios
