inFile = open('ERR0498-04-05.unmapped')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[9]]=fields[0]
inFile.close()
N = 100000
d = D.items()

for i in range(0,len(d),N): 
    f = i/N
    ouFile = open('ERR0498-04-05.unmapped.unique.'+str(f)+'.fasta','w')
    for j in range(N):
        if i+j < len(d):
            ouFile.write('>'+d[i+j][1]+'\n')
            ouFile.write(d[i+j][0]+'\n')
    ouFile.close()
