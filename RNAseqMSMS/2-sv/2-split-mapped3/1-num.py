import sys
import os
DIR='.'
files = os.listdir(DIR)
D = {}
for f in files:
    if f[-8:]=='splicing':
        inFile = open(DIR+'/'+f)
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

