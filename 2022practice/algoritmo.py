import multiprocessing
import random

import numpy as np

import funciones
def algoritmo():
    solucion = None
    return solucion
# algoritmo para maximizar ejerciciod
def añadirIngrediente(ingrediente, ingredientes, dicClientes, solucion):
    solucion.append(ingrediente)
    idx = [i for i, cliente in dicClientes.items() if ingrediente in cliente["no"]]

    [ingredientes[ing]["si"].remove(x) for x in idx for ing in dicClientes[x]["si"]]
    [ingredientes[ing]["no"].remove(x) for x in idx for ing in dicClientes[x]["no"]]
    [dicClientes.pop(x) for x in idx]
def eliminarIngrediente(ingrediente, ingredientes, dicClientes):
    idx = [i for i, cliente in dicClientes.items() if ingrediente in cliente["si"]]
    [ingredientes[ing]["si"].remove(x) for x in idx for ing in dicClientes[x]["si"]]
    [ingredientes[ing]["no"].remove(x) for x in idx for ing in dicClientes[x]["no"]]
    [dicClientes.pop(x) for x in idx]
def algoritmo1(dicClientes, ingredientes, cotaSup, operador, minimosINgredientes=None, maximosIngredientes=None):
    ingredientesTotales = list(ingredientes.keys())
    ingredientesTotales = funciones.devolverListaOrdenada(ingredientesTotales, ingredientes)
    solucion = []
    while (1):
        ingredientesTotales = funciones.devolverListaOrdenada(ingredientesTotales, ingredientes)

        if len(ingredientesTotales) == 1:
            if len(ingredientes[ingredientesTotales[0]]["si"]) - len(ingredientes[ingredientesTotales[0]]["no"]) > 0:
                solucion.append(ingredientesTotales[0])
            break
        if len(ingredientesTotales) >= 2:
            ing1 = ingredientesTotales[0]
            ing2 = ingredientesTotales[-1]
            allowed1 = True
            allowed2 = True
            dif1 = len(ingredientes[ing1]["si"]) - len(ingredientes[ing1]["no"])
            dif2 = len(ingredientes[ing2]["no"]) - len(ingredientes[ing2]["si"])
            if not operador(dif1, 0):
                allowed1 = False
            if not operador(dif2, 0):
                allowed2 = False

            if allowed1:
                añadirIngrediente(ing1, ingredientes, dicClientes, solucion)
                ingredientesTotales.remove(ing1)
            if allowed2:
                eliminarIngrediente(ing2, ingredientes, dicClientes)
                ingredientesTotales.remove(ing2)
            if not allowed1 and not allowed2:
                break
        else:
            break
    return solucion
def algoritmo2(dicClientes, ingredientes, cotaSup, operador, minimosINgredientes=None, maximosIngredientes=None,
               numeroInicios=30, aleatorizacionIngredientes=10, numeroAgrupacion=10, iteraciones=100):
    ingredientesTotales = list(ingredientes.keys())

    clientesTotales = []
    clientes = list(dicClientes.keys())
    clientes.sort(key=lambda t: len(dicClientes[t]["si"]) + len(dicClientes[t]["no"]))
    ingredientesAñadidos = []
    ingredientesProhibidos = []

    for cliente in clientes:
        if set.intersection(set(dicClientes[cliente]["si"]), set(ingredientesProhibidos)) == set():
            if set.intersection(set(dicClientes[cliente]["no"]), set(ingredientesAñadidos)) == set():
                [ingredientesAñadidos.append(e) for e in dicClientes[cliente]["si"] if e not in ingredientesAñadidos]
                [ingredientesProhibidos.append(e) for e in dicClientes[cliente]["no"] if
                 e not in ingredientesProhibidos]
                clientesTotales.append(cliente)

    [ingredientesAñadidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) == set()]
    [ingredientesProhibidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) != set()]

    ingredientes1 = ingredientes
    [ingredientes1[e]["si"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["si"] if
     x not in clientesTotales]
    [ingredientes1[e]["no"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["no"] if
     x not in clientesTotales]
    # print(ingredientes1)
    k = numeroAgrupacion
    long = len(clientesTotales)
    for i in range(iteraciones):
        print("Indice %s" % i)
        print("Valor de k %s" % k)
        if k > 0:
            ingredientesProhibidos.sort(key=lambda t: len(ingredientes1[t]["si"]) - len(ingredientes1[t]["no"]),
                                        reverse=True)
            ingAñadir = ingredientesProhibidos[0:k]
            ingredientesAñadidos.sort(key=lambda t: len(ingredientes1[t]["no"]) - len(ingredientes1[t]["si"]),
                                      reverse=True)
            ingQuitar = ingredientesAñadidos[0:k]
        else:
            ingredientesProhibidos = random.sample(ingredientesProhibidos, len(ingredientesProhibidos))
            ingredientesAñadidos = random.sample(ingredientesAñadidos, len(ingredientesAñadidos))
            ingAñadir = ingredientesProhibidos[0:numeroAgrupacion * 100]
            ingQuitar = ingredientesAñadidos[0:numeroAgrupacion * 100]

        if k > 0:
            k -= 1
        ingAñadidos1 = list(set(ingredientesAñadidos + ingAñadir) - set(ingQuitar))
        ingProhibidos1 = list(set(ingredientesProhibidos + ingQuitar) - set(ingAñadir))
        clientesTotales1 = []
        for cliente in clientes:
            if set.intersection(set(dicClientes[cliente]["si"]), set(ingProhibidos1)) == set():
                if set.intersection(set(dicClientes[cliente]["no"]), set(ingAñadidos1)) == set():
                    [ingAñadidos1.append(e) for e in dicClientes[cliente]["si"] if e not in ingAñadidos1]
                    [ingProhibidos1.append(e) for e in dicClientes[cliente]["no"] if e not in ingProhibidos1]
                    clientesTotales1.append(cliente)
        print("NUeva posible sol %s" % (len(clientesTotales1)))
        if len(clientesTotales1) > long:
            print("Nueva sol")
            k = numeroAgrupacion
            long = len(clientesTotales1)
            ingredientesAñadidos = ingAñadidos1
            ingredientesProhibidos = ingProhibidos1
            clientesTotales = clientesTotales1
        ingredientes1 = ingredientes
        [ingredientes1[e]["si"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["si"] if
         x not in clientesTotales]
        [ingredientes1[e]["no"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["no"] if
         x not in clientesTotales]
        print("Tam sol %s" % long)

    return np.unique(ingredientesAñadidos), len(clientesTotales)
def devolverIngCliente(x, ingAñadididos, ingFuera, param1, param2):
    a = []
    [a.append(param1) for e in x["si"] if e not in ingAñadididos]
    [a.append(param2) for e in x["no"] if e not in ingFuera]

    return param1 * len(set.difference(set(x["si"]), ingAñadididos)) + param2 * len(
        set.difference(set(x["no"]), ingFuera))
def algoritmo3(dicClientes, ingredientes, cotaSup, operador, minimosINgredientes=None, maximosIngredientes=None,
               numeroInicios=30, aleatorizacionIngredientes=10, numeroAgrupacion=10, iteraciones=100, param1=1,
               param2=1, salto=100, inicios=10, aleatoriedad=10):
    ingredientesTotales = list(ingredientes.keys())

    clientesTotales = []
    clientes = list(dicClientes.keys())
    ingredientesAñadidos = []
    ingredientesProhibidos = []
    clientes.sort(
        key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1, param2))

    while (len(clientes) > 0):
        if len(clientes) % salto == 0:
            clientes.sort(
                key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1,
                                                 param2))

        cliente = clientes.pop(0)

        if set.intersection(set(dicClientes[cliente]["si"]), set(ingredientesProhibidos)) == set():
            if set.intersection(set(dicClientes[cliente]["no"]), set(ingredientesAñadidos)) == set():
                [ingredientesAñadidos.append(e) for e in dicClientes[cliente]["si"] if e not in ingredientesAñadidos]
                [ingredientesProhibidos.append(e) for e in dicClientes[cliente]["no"] if
                 e not in ingredientesProhibidos]
                clientesTotales.append(cliente)

    [ingredientesAñadidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) == set()]
    [ingredientesProhibidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) != set()]

    ingredientes1 = ingredientes
    [ingredientes1[e]["si"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["si"] if
     x not in clientesTotales]
    [ingredientes1[e]["no"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["no"] if
     x not in clientesTotales]

    k = numeroAgrupacion
    long = len(clientesTotales)

    return np.unique(ingredientesAñadidos), len(clientesTotales)
def ejecutar(i, sharedlist, clientes, dicClientes, aleatoriedad, salto, param1, param2):
    import random as ra
    ingredientesAñadidos = []
    ingredientesProhibidos = []
    clientesTotales = []
    clientes1 = clientes[0:aleatoriedad]
    clientes1 = ra.sample(clientes1, len(clientes1))
    clientes[0:aleatoriedad] = clientes1
    while (len(clientes) > 0):
        if len(clientes) % salto == 0:
            clientes.sort(
                key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1,
                                                 param2))

            clientes1 = clientes[0:aleatoriedad]
            clientes1 = ra.sample(clientes1, len(clientes1))
            clientes[0:aleatoriedad] = clientes1

        cliente = clientes.pop(0)

        if set.intersection(set(dicClientes[cliente]["si"]), set(ingredientesProhibidos)) == set():
            if set.intersection(set(dicClientes[cliente]["no"]), set(ingredientesAñadidos)) == set():
                [ingredientesAñadidos.append(e) for e in dicClientes[cliente]["si"] if e not in ingredientesAñadidos]
                [ingredientesProhibidos.append(e) for e in dicClientes[cliente]["no"] if
                 e not in ingredientesProhibidos]

                clientesTotales.append(cliente)

    sharedlist[i] = len(clientesTotales)
def algoritmo4(dicClientes, ingredientes, cotaSup, operador, minimosINgredientes=None, maximosIngredientes=None,
               numeroInicios=30, aleatorizacionIngredientes=10, numeroAgrupacion=10, iteraciones=100, param1=1,
               param2=1, salto=100, inicios=10, aleatoriedad=10):
    ingredientesTotales = list(ingredientes.keys())

    clientesTotales = []
    clientes = list(dicClientes.keys())
    ingredientesAñadidos = []
    ingredientesProhibidos = []
    clientes.sort(
        key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1, param2))

    [ingredientesAñadidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) == set()]
    [ingredientesProhibidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) != set()]

    ingredientes1 = ingredientes
    [ingredientes1[e]["si"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["si"] if
     x not in clientesTotales]
    [ingredientes1[e]["no"].remove(x) for e in ingredientes1.keys() for x in ingredientes1[e]["no"] if
     x not in clientesTotales]

    k = numeroAgrupacion
    long = len(clientesTotales)
    manager = multiprocessing.Manager()
    shared_list = manager.list()
    [shared_list.append(0) for i in range(inicios)]

    process = []
    for i in range(inicios):
        process.append(multiprocessing.Process(target=ejecutar,
                                               args=[i, shared_list, clientes, dicClientes, aleatoriedad, salto, param1,
                                                     param2]))

        process[i].start()
    for i in range(inicios):
        process[i].join()

    for e in shared_list:
        print(e)
    print("-------------------")

    return np.unique(ingredientesAñadidos), max(shared_list)
def algoritmo5(dicClientes, ingredientes, cotaSup, operador, minimosINgredientes=None, maximosIngredientes=None,
               numeroInicios=30, aleatorizacionIngredientes=10, numeroAgrupacion=10, iteraciones=100, param1=1,
               param2=1, salto=100, inicios=10, aleatoriedad=10):
    ingredientesTotales = list(ingredientes.keys())

    clientesTotales = []
    clientesEliminados = []
    clientes = list(dicClientes.keys())
    ingredientesAñadidos = []
    ingredientesProhibidos = []
    clientes.sort(
        key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1, param2))

    while (len(clientes) > 0):
        if len(clientes) % salto == 0:
            clientes.sort(
                key=lambda t: devolverIngCliente(dicClientes[t], ingredientesAñadidos, ingredientesProhibidos, param1,
                                                 param2))

        cliente = clientes.pop(0)

        if set.intersection(set(dicClientes[cliente]["si"]), set(ingredientesProhibidos)) == set():
            if set.intersection(set(dicClientes[cliente]["no"]), set(ingredientesAñadidos)) == set():
                [ingredientesAñadidos.append(e) for e in dicClientes[cliente]["si"] if e not in ingredientesAñadidos]
                [ingredientesProhibidos.append(e) for e in dicClientes[cliente]["no"] if
                 e not in ingredientesProhibidos]
                clientesTotales.append(cliente)
            else:
                clientesEliminados.append(cliente)
        else:
            clientesEliminados.append(cliente)

    [ingredientesAñadidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) == set() and e not in ingredientesAñadidos]
    [ingredientesProhibidos.append(e) for e, u in ingredientes.items() if
     set.intersection(set(clientesTotales), set(u["no"])) != set() and e not in ingredientesProhibidos]

    ingredientes1 = ingredientes

    k = numeroAgrupacion
    long = len(clientesTotales)
    posibilidad = True

    ingredientesProhidosClientesPos = {i: [] for i in ingredientesProhibidos}
    ingredientesProhidosClientesNeg = {i: [] for i in ingredientesProhibidos}
    ingredientesAñadidosClientesPos = {i: [] for i in ingredientesAñadidos}
    ingredientesAñadidosClientesNeg = {i: [] for i in ingredientesAñadidos}
    [ingredientesProhidosClientesPos[i].append(e) for i in ingredientesProhibidos for e in
     list(set.intersection(set(ingredientes[i]["si"]), set(clientesEliminados))) if
     (not any(k in ingredientesProhibidos for k in dicClientes[e]["si"])) and all(
         k in (ingredientesAñadidos + [i]) for k in dicClientes[e]["si"])]

    [ingredientesProhidosClientesNeg[i].append(e) for i in ingredientesProhibidos for e in
     list(set.intersection(set(ingredientes[i]["no"]), set(clientesTotales)))]

    [ingredientesAñadidosClientesPos[i].append(e) for i in ingredientesAñadidos for e in
     list(set.intersection(set(ingredientes[i]["si"]), set(clientesTotales)))]

    [ingredientesAñadidosClientesNeg[i].append(e) for i in ingredientesAñadidos for e in
     list(set.intersection(set(ingredientes[i]["no"]), set(clientesEliminados))) if
     (not any(k in list(set(ingredientesAñadidos) - set((i,))) for k in dicClientes[e]["no"])) and all(
         k in (ingredientesAñadidos) for k in dicClientes[e]["si"])]

    ingredientesProhibidos.sort(
        key=lambda t: len(ingredientesProhidosClientesPos[t]) - len(ingredientesProhidosClientesNeg[t]), reverse=True)
    ingredientesAñadidos.sort(
        key=lambda t: len(ingredientesAñadidosClientesPos[t]) - len(ingredientesAñadidosClientesNeg[t]))
    while 1:
        if len(ingredientesProhibidos) > 0 and len(ingredientesAñadidos) > 0:
            ingredientesProhidosClientesPos = {i: [] for i in ingredientesProhibidos}
            ingredientesProhidosClientesNeg = {i: [] for i in ingredientesProhibidos}
            ingredientesAñadidosClientesPos = {i: [] for i in ingredientesAñadidos}
            ingredientesAñadidosClientesNeg = {i: [] for i in ingredientesAñadidos}
            [ingredientesProhidosClientesPos[i].append(e) for i in ingredientesProhibidos for e in
             list(set.intersection(set(ingredientes[i]["si"]), set(clientesEliminados))) if
             (not any(k in ingredientesProhibidos for k in dicClientes[e]["si"])) and all(
                 k in (ingredientesAñadidos + [i]) for k in dicClientes[e]["si"])]

            [ingredientesProhidosClientesNeg[i].append(e) for i in ingredientesProhibidos for e in
             list(set.intersection(set(ingredientes[i]["no"]), set(clientesTotales)))]

            [ingredientesAñadidosClientesPos[i].append(e) for i in ingredientesAñadidos for e in
             list(set.intersection(set(ingredientes[i]["si"]), set(clientesTotales)))]

            [ingredientesAñadidosClientesNeg[i].append(e) for i in ingredientesAñadidos for e in
             list(set.intersection(set(ingredientes[i]["no"]), set(clientesEliminados))) if
             (not any(k in list(set(ingredientesAñadidos) - set((i,))) for k in dicClientes[e]["no"])) and all(
                 k in (ingredientesAñadidos) for k in dicClientes[e]["si"])]
            ingredientesProhibidos.sort(
                key=lambda t: len(ingredientesProhidosClientesPos[t]) - len(ingredientesProhidosClientesNeg[t]),
                reverse=True)
            ingredientesAñadidos.sort(
                key=lambda t: len(ingredientesAñadidosClientesPos[t]) - len(ingredientesAñadidosClientesNeg[t]))
            ing1 = ingredientesProhibidos[0]
            ing2 = ingredientesAñadidos[0]
            suma1 = len(ingredientesProhidosClientesPos[ing1]) - len(ingredientesProhidosClientesNeg[ing1])
            suma2 = len(ingredientesAñadidosClientesPos[ing2]) - len(ingredientesAñadidosClientesNeg[ing2])
            if suma1 - suma2 > 0:
                print(ing1)
                ingredientesAñadidos.append(ing1)
                ingredientesAñadidos.remove(ing2)
                ingredientesProhibidos.remove(ing1)

                [clientesTotales.append(e) for e in ingredientesProhidosClientesPos[ing1] if
                 e not in ingredientesAñadidosClientesPos[ing2]]
                [clientesTotales.append(e) for e in ingredientesAñadidosClientesNeg[ing2] if
                 e not in ingredientesProhidosClientesNeg[ing1]]
                [clientesEliminados.remove(e) for e in ingredientesProhidosClientesPos[ing1] if
                 e not in ingredientesAñadidosClientesPos[ing2]]
                [clientesEliminados.remove(e) for e in ingredientesAñadidosClientesNeg[ing2] if
                 e not in ingredientesProhidosClientesNeg[ing1]]
                [clientesEliminados.append(e) for e in ingredientesAñadidosClientesPos[ing2]]
                [clientesEliminados.append(e) for e in ingredientesProhidosClientesNeg[ing1]]
                [clientesTotales.remove(e) for e in ingredientesAñadidosClientesPos[ing2]]
                [clientesTotales.remove(e) for e in ingredientesProhidosClientesNeg[ing1]]
            else:
                break;

        else:
            break

    return np.unique(ingredientesAñadidos), len(clientesTotales)
