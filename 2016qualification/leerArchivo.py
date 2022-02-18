import clases

def leerArchivo(nombreArchivo):
     data = open(nombreArchivo, "r")
   
    
     rows,columns,drones,turns,payload= [
            int(a) for a  in data.readline().strip().split()
        ]
     numProdTypes=int( data.readline().strip().split()[0])
     prodTypes= [
            int(a) for a  in data.readline().strip().split()
        ]
     numWarehouses=int( data.readline().strip().split()[0])
    
     
     input_data = [line.strip().split() for line in data]
     diccionarioWarehouses = {
            idx: {
                "loc": (int(input_data[2*idx][0]),int(input_data[idx][1])),
                "items": [int(e) for e in input_data[2*idx+1]]
                
            }
            for idx in range( numWarehouses)
        }
     input_data=input_data[numWarehouses*2:]
     numOrders=int(input_data[0][0])
     
     input_data= input_data[1:]
  
     diccionarioOrders = {
            idx: {
                "loc": (int(input_data[3*idx][0]),int(input_data[3*idx][1])),
                "numItems": [int(e) for e in input_data[3*idx+1]],
                "itemTypes": [int(e) for e in input_data[3*idx+2]]
                
            }
            for idx in range( numOrders)
        }
     
     return rows,columns,drones,turns,payload,numProdTypes,numWarehouses,numOrders,diccionarioWarehouses,diccionarioOrders 