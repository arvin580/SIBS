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
                D[line2].append(line1)
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('sum_snv.exome_summary.overall.filter.nonsynonymous-splicing.pep.nonstop','SNV')
unique('sum_snv.exome_summary.indel.overall.filter.pep.nonstop','INDEL')

ouFile = open('Homo_known-protein_filltered-snv_indel','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')

ouFile.close()

