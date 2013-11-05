Nature = ['128230632', '128233367', '128234255', '128241494']

ouFile = open('Nature-breakpoints','w')
import os
DIR = '.'
Fs = os.listdir(DIR)
D = {}
for F in Fs:
    if F[-7:] == '.blated':
        inFile = open(DIR + os.sep + F)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            for x in Nature:
                if x in fields:
                    D[line] = 1
        inFile.close()
for k in D:
    ouFile.write(k+'\n')
ouFile.close()
    
