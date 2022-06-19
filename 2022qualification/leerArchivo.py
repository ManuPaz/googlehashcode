def leerArchivo(nombreArchivo):
    data = open(nombreArchivo, "r")

    numContributors, numProyects = [
        int(a) for a in data.readline().strip().split()
    ]

    input_data = [line.strip().split() for line in data]
    contributors = {}
    e = 0

    skills = dict()

    for idx in range(numContributors):
        nombre = input_data[e][0]
        contributors[nombre] = {}

        contributors[nombre]["numRoles"] = int(input_data[e][1])
        e += 1
        contributors[nombre]["skills"] = {}
        for k in range(contributors[nombre]["numRoles"]):
            contributors[nombre]["skills"][input_data[e][0]] = int(input_data[e][1])
            e += 1
            for s in contributors[nombre]["skills"]:
                if s not in skills:
                    skills[s] = {"usuarios": {}, "proyectos": {}, "usuariosArray": []}

                skills[s]["usuarios"][nombre] = contributors[nombre]["skills"][s]
                skills[s]["usuariosArray"].append(nombre)

    input_data = input_data[e:]

    e = 0
    projects = {}
    for idx in range(numProyects):
        nombre = input_data[e][0]
        projects[nombre] = {}
        projects[nombre]["days"] = int(input_data[e][1])
        projects[nombre]["score"] = int(input_data[e][2])
        projects[nombre]["daybefore"] = int(input_data[e][3])
        projects[nombre]["numroles"] = int(input_data[e][4])
        projects[nombre]["velocidad"] = projects[nombre]["score"] / projects[nombre]["days"]
        projects[nombre]["velocidad2"] = projects[nombre]["score"] / projects[nombre]["numroles"]
        projects[nombre]["roles"] = []
        projects[nombre]["levels"] = []
        e += 1
        for k in range(projects[nombre]["numroles"]):
            projects[nombre]["roles"].append(input_data[e][0])
            projects[nombre]["levels"].append(int(input_data[e][1]))
            e += 1

        for ii, s in enumerate(projects[nombre]["roles"]):
            if s not in skills:
                skills[s] = {"usuarios": {}, "proyectos": {}, "usuariosArray": []}
            if nombre not in skills[s]["proyectos"]:
                skills[s]["proyectos"][nombre] = []

                skills[s]["proyectos"][nombre].append(projects[nombre]["levels"][ii])

    return numContributors, numProyects, contributors, projects, skills
