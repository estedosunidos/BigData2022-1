import sys

palabra_anterior = None
menor=0
for line in sys.stdin:
        palabra, valor = line.split(':')
        aux=float(valor)
        if palabra == palabra_anterior:
                if aux<menor:
                        menor=aux
        else:
                if palabra_anterior is not None:
                        print('%s\t\t\t%s' % (palabra_anterior, menor))
                        menor=0
                menor=aux
                palabra_anterior = palabra
print('%s\t\t\t%s' % (palabra_anterior, menor))
