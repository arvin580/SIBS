#!/usr/bin/env python

D = {}
def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            if flag:
                D[line2].append(flag+':'+':'.join(line1.split('\t')))
            else:
                D[line2].append(':'.join(line1.split('\t')))
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa')
unique('split-mapped-deletion-translocation-inversion-duplication-K','SV')
unique('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict-K','PREDICT-SPLICING')

ouFile = open('HeLa-predict-splicing-sv-K.fasta','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    #ouFile.write('>REVERSE:'+'|'.join(D[k])+'\n')
    #ouFile.write(k[::-1]+'\n')

ouFile.close()

