import re
import math

def getwords(inF):
    D = dict() 
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        for item in fields:
            item = item.lower()
            D.setdefault(item, 0)
            D[item] += 1
    inFile.close()
    return D

w = getwords('doc_class.py')
for k in w:
    print(k)
    print(w[k])

