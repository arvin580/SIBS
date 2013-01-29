'''
not remove N:43003468
    remove N:41139006
'''
inFile = open('ERR0498-04-05.unmapped')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[9].find('N')==-1 and fields[9].find('n')==-1:
        D[fields[9]]=fields[0]
inFile.close()
N = 100000
d = D.items()

ouFile1 = open('ERR0498-04-05.unmapped.unique.fasta','w')
for i in range(0,len(d),N): 
    f = i/N
    ouFile = open('ERR0498-04-05.unmapped.unique.'+str(f)+'.fasta','w')
    for j in range(N):
        if i+j < len(d):
            ouFile.write('>'+d[i+j][1]+'\n')
            ouFile.write(d[i+j][0]+'\n')

            ouFile1.write('>'+d[i+j][1]+'\n')
            ouFile1.write(d[i+j][0]+'\n')
    ouFile.close()
ouFile1.close()
