import sys

current_word = None
current_precio = []
word = None
precio = 0
total=0
for line in sys.stdin:
        word,count,ano = line.split(" : ")
        precio = int(count)
        current_precio.append(precio)
        current_precio.sort()
for i in current_precio:
        print (word,i,ano)

