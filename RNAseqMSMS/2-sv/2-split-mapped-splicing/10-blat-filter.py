import os
D = {}
ouFile = open('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.not-splicing.fa.blated-95-70','w')
files =  os.listdir('.')
for f in files:
    if f[-7:] == '.blated':
        inFile = open(f)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if float(fields[2]) >= 95  and int(fields[7]) -int(fields[6]) >= 70:
                D[fields[0]] = line
        inFile.close()

for k in D:
    ouFile.write(D[k]+'\n')
