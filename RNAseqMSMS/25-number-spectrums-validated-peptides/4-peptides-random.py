inFile = open('Identified-Peptides-Corresponding-Reads')
L = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields[0])
inFile.close()

import random

ouFile = open('Peptides-Identified', 'w')
xL = random.sample(L, 160)
for x in xL:
    ouFile.write(x + '\n')

ouFile.close()
