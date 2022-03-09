import sys

for line in sys.stdin:
    print(line.split(",")[2][0:7], ",", 1)

