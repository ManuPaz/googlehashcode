import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
     infogeneral={}
     cabecera= [
            int(a) for a  in data.readline().strip().split()
        ]
     
     
     input_data = [line.strip().split() for line in data]
     diccionario1 = {
            idx: {
                "tags":  line[2:],
                "numTags": int(line[1]),
                "vertical": True if line[0]=="V"  else False
            }
            for idx, line in enumerate(input_data)
        }
     diccionario2={e:[] for  k in diccionario1.values() for e in k["tags"] }
     [diccionario2[e].append(i)  for  i,k in diccionario1.items() for e in k["tags"] ]
     return cabecera,diccionario1,diccionario2