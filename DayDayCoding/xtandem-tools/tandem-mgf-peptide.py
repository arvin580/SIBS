#!/usr/bin/env python

import sys
DIR = '/netshare1/home1/people/hansun/Data/HeLa/HeLa-MSMS'

def spec(sp):
    inFile = open(DIR+'/'+sp.split('.')[0]+'.mgf')
    L = inFile.readlines()
    inFile.close()
    s = L.index('TITLE=%s\n'%sp)
    e = s + L[s:].index('END IONS\n')
    mgf = L[s-1:e+1]
    #print(''.join(mgf))
    return mgf

def peptide(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'-pep-spec.mgf','w')
    ouFile2 = open(inF+'-pep-spec.note','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        pep = fields[3]
        sp = fields[0].strip()
        other = fields[4]
        mgf = spec(sp)
        ouFile1.write(''.join(mgf))
        ouFile2.write(pep + '\t' + sp+'\t'+other+'\n')
    inFile.close()
    ouFile1.close()
    ouFile2.close()

peptide(sys.argv[1])
