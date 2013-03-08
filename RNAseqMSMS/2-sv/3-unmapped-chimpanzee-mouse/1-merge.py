import os

D2 = {}
files = os.listdir('.')
for f in files:
    if f[-9:]=='.unmapped':
        inFile = open(f)
        while True:
            line1 = inFile.readline().strip('>\n')
            line2 = inFile.readline().strip()
            if line1:
                D2[line1]=line2
            else:
                break
        inFile.close()





D = {}

ouFile = open('unmapped-blated-chimpanzee-90-60-mouse-90-60.seq', 'w')

inFile = open('unmapped-blated-chimpanzee-90-60')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], [])
    D[fields[0]].append(line)
inFile.close()
inFile = open('unmapped-blated-mouse-90-60')
for line in inFile:
    line = line.strip()
    fields = line.split()
    D.setdefault(fields[0], [])
    D[fields[0]].append(line)
inFile.close()

for k in D:
    ouFile.write('>'+'\t'.join(D[k])+'\n')
    ouFile.write(D2[k]+'\n')
