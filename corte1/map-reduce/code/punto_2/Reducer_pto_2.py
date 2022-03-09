import sys

current_word = None
current_count = 0
word = None
total=0
promedio=1
for line in sys.stdin:
        word, count = line.split(" : ")

        total=int(count)

        if current_word == word:
                current_count += total
                promedio+=1
        else:
                if current_word:

                        print (current_word, (current_count/promedio))
                        promedio=1
                current_count = total
                current_word = word

if current_word == word:
        print (current_word, (current_count/promedio))
