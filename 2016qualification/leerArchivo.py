import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
     infogeneral={}
     cabecera= [
            int(a) for a  in data.readline().strip().split()
        ]
     
     
     input_data = [line.strip().split() for line in data]
     diccionario1 = {
            line[2]: {
                "a": int(line[0]),
                "b": int(line[1]),
                "c": int(line[3])
            }
            for idx, line in enumerate(input_data[:cabecera[1]])
        }
     generadorParaContar= [{"num_streets": int(line[0]), "streets": line[1:]} for line in input_data[cabecera[1]:]]
     return cabecera,diccionario1, generadorParaContar