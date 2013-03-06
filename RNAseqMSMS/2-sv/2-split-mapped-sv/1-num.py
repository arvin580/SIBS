import sys
import os
files = os.listdir('.')
D = {}
for f in files:
    if f[-12:]=='not-splicing':
        inFile = open(f)
        while True:
            line1 = inFile.readline()
            line2 = inFile.readline()
            if line1:
                fields = line1.split('\t')
                D.setdefault(fields[0],0)
                D[fields[0]]+=1
            else:
                break
        inFile.close()

print(len(D))

