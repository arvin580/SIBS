inFs=['CHC10A.br.fasta.blasted.filtered.seq1',
'CHC10B.br.fasta.blasted.filtered.seq1',
'CHC5A.br.fasta.blasted.filtered.seq1',
'CHC5B.br.fasta.blasted.filtered.seq1',
'CHC6A.br.fasta.blasted.filtered.seq1',
'CHC6B.br.fasta.blasted.filtered.seq1',
'CHC7A.br.fasta.blasted.filtered.seq1',
'CHC7B.br.fasta.blasted.filtered.seq1',
'ICC4A.br.fasta.blasted.filtered.seq1',
'ICC4B.br.fasta.blasted.filtered.seq1',
'ICC5A.br.fasta.blasted.filtered.seq1',
'ICC5B.br.fasta.blasted.filtered.seq1',
'ICC9A.br.fasta.blasted.filtered.seq1',
'ICC9B.br.fasta.blasted.filtered.seq1',
'ICC10A.br.fasta.blasted.filtered.seq1',
'ICC10B.br.fasta.blasted.filtered.seq1'
        ]
D = {}
for inF in inFs:
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        k = ''.join(fields[0:-1])
        D.setdefault(k, [])
        D[k].append(fields[-1])
    inFile.close()

ouFile = open('16sSV.read.name','w')

for k in D:
    if len(k)>0:
        ouFile.write(k+'\t')
        ouFile.write('\t'.join(D[k])+'\n')
ouFile.close()

