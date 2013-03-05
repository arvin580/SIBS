import sys
import os
D = {}
files = os.listdir('.')
for f in files:
    if f[-6:]=='blated':
        inFile = open(f)
        for line in inFile:
            line = line.strip()
            fields = line.split()
            D[fields[0]]=1
        inFile.close()
print(len(D))


