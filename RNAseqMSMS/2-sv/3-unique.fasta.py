inFile = open('ERR0498-04-05.unmapped')
ouFile = open('ERR0498-04-05.unmapped.unique.fasta','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[9]]=fields[0]
inFile.close()
n = 0
for k in D:
    n += 1
    
    ouFile.write('>'+D[k]+'\n')
    ouFile.write(k+'\n')
ouFile.close()
