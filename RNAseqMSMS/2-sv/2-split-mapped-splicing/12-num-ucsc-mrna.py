def num(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.mrna','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            if item[0:3] == 'NM_' or item[0:3] == 'NR_':
                D.setdefault(item,0)
                D[item]+=1
    inFile.close()
    for k in D:
        ouFile.write(k+'\t'+str(D[k])+'\n')
    ouFile.close()

num('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fa.blated-95-70')
num('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fa.blated-100-75')
