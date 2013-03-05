import sys
import os
D = {}
files = os.listdir('.')
for f in files:
    if f.find('unmapped.pep.nonstop.digested.6acid.unique')!=-1 or f=='human_uniprot_sprot.digested.6acid.fa':
    #if f=='human_uniprot_sprot.digested.6acid.fa':
        inFile = open(f)
        while True:
            line1 = inFile.readline().strip('>\n')
            line2 = inFile.readline().strip()
            if line1:
                D.setdefault(line2,[])
                D[line2].append(line1)
            else:
                break
        inFile.close()

ouFile = open('unmapped.database.fa','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    ouFile.write('>'+'REVERSE'+'|'+'|'.join(D[k])+'\n')
    ouFile.write(k[::-1]+'\n')
ouFile.close()




