import sys

current_word = None
current_count = 0
word = None
count = 0
mount = None
max = 0
year = None


for line in sys.stdin:
    word, count = line.split(",")
    if(word != "Date of "):
        count = int(count[1])
        year = word

        if current_word == word:
            current_count += count
        else:
            if current_word:

                if(max < current_count):
                    mount = current_word
                    max = current_count
                if(current_word[5:7] == "12" or current_word == "2017-05 "):
                    print(mount, ",", max)
                    max = 0

            current_count = count
            current_word = word

if current_word == word:
    print('%s,%s' % (current_word, current_count))

