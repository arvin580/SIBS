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
    ouFile = open(inF+'-pep-spec.mgf','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('&&&')
            pep = line2
            sp = fields[1].strip().split('+++')[0]
            print(sp)
            mgf = spec(sp)
            ouFile.write(''.join(mgf))
        else:
            break
    inFile.close()
    ouFile.close()

peptide('Peptides-Identified-Second-unSpec')
