import sys


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

D=protein()

inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'-1','w')
ouFile2 = open(sys.argv[1]+'-2','w')
ouFile3 = open(sys.argv[1]+'-3','w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>2:
        ouFile1.write(line+'\n')
    else:
        L = []
        for k in D:
            if fields[0] in k:
                for x in D[k]:
                    L.append(x)
        if L:
            ouFile2.write(fields[0]+'\t'+fields[1]+'\t'+'\t'.join(L)+'\n')
        else:
            ouFile3.write(fields[0]+'\t'+fields[1]+'\n')

ouFile1.close()
ouFile2.close()
ouFile3.close()
inFile.close()
