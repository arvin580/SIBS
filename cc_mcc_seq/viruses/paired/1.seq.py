### ls *.fa |xargs -n 1 python 1.seq.py
import sys
inFile = open(sys.argv[1])
D = dict()
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D[head] = seq
    else:
        break
inFile.close()

inFile = open(sys.argv[1] + '')

