inFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fasta')
D = {}
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
N = 100000
d = D.items()
for i in range(0,len(d),N): 
    f = i/N
    ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.'+str(f)+'.fa','w')
    for j in range(N):
        if i+j < len(d):
            ouFile.write('>'+d[i+j][0]+'\n')
            ouFile.write(d[i+j][1]+'\n')
    ouFile.close()
