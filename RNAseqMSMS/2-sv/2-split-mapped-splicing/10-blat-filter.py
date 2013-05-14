import os
def filter(n1,n2):
    D = {}
    ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fa.blated-%s-%s'%(n1,n2),'w')
    files =  os.listdir('.')
    for f in files:
        if f[-7:] == '.blated':
            inFile = open(f)
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                if float(fields[2]) >= n1  and int(fields[7]) -int(fields[6]) >= n2:
                    D.setdefault(fields[0],[])
                    D[fields[0]].append(line) 
            inFile.close()
    
    for k in D:
        ouFile.write(k+'\t'+'\t'.join(D[k])+'\n')

filter(95,70)
filter(100,75)
