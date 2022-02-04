import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
     infogeneral={}
     l= data.readline().strip().split()
     cabecera= {"books":int(l[0]),"libraries":int(l[1]),"days":int(l[2])
           
        }
     v=data.readline().strip().split()
     puntosPorLibro={i:int(e) for i,e in enumerate(v)}
     input_data = [line.strip().split() for line in data]
     diccionario1 = {(i-1)//2:[int(e) for e in line] for  i,line in enumerate(input_data) if i%2==1 }
     diccionario2 = {(i//2):{"numbooks":int(line[0]),"signupdays":int(line[1]),"booksperday":int(line[2])} for  i,line in enumerate(input_data[:-1]) if i%2==0 }    
     
     return cabecera,diccionario1, diccionario2,puntosPorLibro