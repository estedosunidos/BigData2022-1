import sys

precios=[]
ciudades=[]
fechas=[]
anos=[]
for line in sys.stdin:
        precio=line.split(",")
        precios.append(precio[1])
        fechas.append(precio[2])
        if precio[6] == "STAMFORD":
                ciudades.append(precio[6])

precios.pop(0)
fechas.pop(0)

for fecha in fechas:
        separado=fecha.split("-")
        if separado[0] == "2015":
                anos.append(separado[0])
for preci, ciu,ano  in zip(precios, ciudades,anos):

        print( ciu,":",preci,":",ano)
