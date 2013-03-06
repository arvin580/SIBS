import os
import sys

files = os.listdir('.')
def viruse(n1,n2):
    ouFile = open('unmapped-blated-viruses-'+str(n1)+'-'+str(n2), 'w')
    for f in files:
        if f[-7:] == '.blated':
            inFile = open(f)
            for line in inFile:
                line = line.strip()
                fields = line.split()
                if float(fields[2]) >=n1 and float(fields[3]) >=n2 :
                    ouFile.write(line+'\n')
    
            inFile.close()
    
    ouFile.close()

viruse(95,70)
viruse(100,76)


