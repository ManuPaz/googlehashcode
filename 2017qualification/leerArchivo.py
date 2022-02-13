import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
     infogeneral={}
     H,W,R= [
            int(a) for a  in data.readline().strip().split()
        ]
     Pb,Pr,B= [
            int(a) for a  in data.readline().strip().split()
        ]
     inicialPos=[int(a) for a  in data.readline().strip().split()]
     
     input_data = [line.strip().split() for line in data]
     array=[list(line[0]) for line in input_data ]
     
     return H,W,R,Pb,Pr,B, array,inicialPos