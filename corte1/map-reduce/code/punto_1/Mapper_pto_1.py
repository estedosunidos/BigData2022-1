import sys


palabras = list()
palabra = list()
count = 0

for line in sys.stdin:
    print(line.split(",")[2][0:4], 1)

