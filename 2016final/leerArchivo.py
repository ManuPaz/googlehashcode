import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
     infogeneral={}
     duracion=int( data.readline().strip().split()[0])
        
     numSatelites=int(data.readline().strip().split()[0])
        
     
     
     input_data = [line.strip().split() for line in data]
     diccionario1 = {
            idx: {
                "pos": (int(line[0]), int(line[1])),
                
                "v": int(line[2]),
                 "w": int(line[3]),
                "d": int(line[4])
            }
            for idx, line in enumerate(input_data[: numSatelites])
        }
     numCollections=int(input_data[numSatelites][0])
     diccionario={}
     e=numSatelites+1
     dicImagenes={}
     
     k=0
     while (e<len(input_data[numSatelites+1:])):
         diccionario[k]={"value":int(input_data[e][0]),"numLocations":int(input_data[e][1]),"numRanges":int(input_data[e][2])}
         diccionario[k]["images"]=[]
         diccionario[k]["timeRanges"]=[]
       
         e+=1
         for i in range(diccionario[k]["numLocations"]):
               diccionario[k]["images"].append([int(input_data[e][0]),int(input_data[e][1])])
               if (int(input_data[e][0]),int(input_data[e][1])) not in  dicImagenes.keys():
                   dicImagenes[(int(input_data[e][0]),int(input_data[e][1]))]=[]
                  
               dicImagenes[(int(input_data[e][0]),int(input_data[e][1]))].append(k)
               e+=1
         for i in range(diccionario[k]["numRanges"]):
               diccionario[k]["timeRanges"].append([int(input_data[e][0]),int(input_data[e][1])])
               e+=1
         k+=1
             
         
         
         
         
     
     return  duracion,numSatelites,numCollections,diccionario1,diccionario,dicImagenes