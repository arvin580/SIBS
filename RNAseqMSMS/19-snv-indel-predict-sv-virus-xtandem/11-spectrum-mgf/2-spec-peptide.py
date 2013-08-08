#!/usr/bin/env python

import sys
DIR = '/netshare1/home1/people/hansun/Data/HeLa/HeLa-MSMS'

def spec(sp):
    inFile = open(DIR+'/'+sp.split(':')[0]+'.mgf')
    L = inFile.readlines()
    inFile.close()
    #s = L.index('TITLE=%s\n'%sp)
    for i in range(len(L)):
        if L[i].find('TITLE')==0 and L[i].find(sp.split(':')[1]+'.'+sp.split(':')[1])!=-1:
            s=i
            break
    e = s + L[s:].index('END IONS\n')
    mgf = L[s-1:e+1]
    #print(''.join(mgf))
    return mgf

def peptide(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'-pep-spec.mgf','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        pep = fields[0]
        sp = fields[2].strip()
        mgf = spec(sp)
        ouFile1.write(''.join(mgf))
    inFile.close()
    ouFile1.close()

peptide(sys.argv[1])
