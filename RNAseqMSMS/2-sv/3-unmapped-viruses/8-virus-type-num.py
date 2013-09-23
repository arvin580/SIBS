# python 8-virus-type-num.py   unmapped-blated-viruses-100-76.type
import sys
inFile = open(sys.argv[1])
N = 0
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    N += int(fields[1])
inFile.close()
print(N)
