import sys

precios=[]
ciudades=[]
valores=[]

for line in sys.stdin:
        precio=line.split(",")

        precios.append(precio[1])
        ciudades.append(precio[6])
precios.pop(0)
ciudades.pop(0)
for preci, ciu  in zip(precios, ciudades):

        print( ciu,":",preci)
