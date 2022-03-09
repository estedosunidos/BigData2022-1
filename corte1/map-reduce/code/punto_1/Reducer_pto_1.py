import sys

current_word = None
current_count = 0
word = None
count = 0


for line in sys.stdin:
    word, count = line.split(" ")
    count = int(count[0])

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t\t\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print('%s \t\t\t%s' % (current_word, current_count))

