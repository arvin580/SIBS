import sys
D = {}
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.stop','w')
ouFile2 = open(sys.argv[1]+'.stop2','w')
ouFile3 = open(sys.argv[1]+'.not.stop','w')
for line in inFile:
    fields = line.split(',')
    pep = fields[2]
    if pep[-1]=='K' or pep[-1]=='R':
        uniprot=fields[9].split('|')[1]
        ouFile3.write(pep+'\t'+uniprot+'\n')
    elif pep==' Peptide':
        D.setdefault(fields[2], 0)
        D[fields[2]]+=1
inFile.close()

'''
def protein():
    D2 = {}
    inFile = open('/netshare1/home1/people/hansun/StopGainProteomics/2.uniprot/human_uniprot_sprot.fa')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('|')
            name = fields[1]
            D2.setdefault(line2,[])
            D2[line2].append(name)
        else:
            break
    inFile.close()
    return D2

D2=protein()

for k in D:
    ouFile.write(k+'\t'+str(D[k])+'\n')
    ouFile2.write(k+'\t')
    for x in D2:
        if x[-len(k):]==k:
            ouFile2.write('\t'.join(D2[x])+'\t')
    ouFile2.write('\n')
ouFile2.close()
'''
