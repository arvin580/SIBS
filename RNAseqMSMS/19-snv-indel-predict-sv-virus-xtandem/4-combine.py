def uniqueList(inList):
    ouList=list()
    for item in inList :
        if item not in ouList :
            ouList.append(item)
    return ouList


D = {}
D1 = {}
D2 = {}

ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus','w')

def combine(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        pep = fields[2]
        pep_num = fields[3]
        pep_cleavage = fields[0]
        D.setdefault(pep,[])
        D1.setdefault(pep,[])
        D2.setdefault(pep,[])
        D[pep].append(line)
        D1[pep].append(pep_cleavage)
        D2[pep].append(pep_num)
    inFile.close()

combine('HeLa-variant-Trypsin-evidence-unique-peptide-snv-indel-predict-sv-virus')
combine('HeLa-variant-LysC-evidence-unique-peptide-snv-indel-predict-sv-virus')
combine('HeLa-variant-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus')

for k in D:
    ouFile.write(';'.join((uniqueList(D1[k])))+'\t'+k+'\t'+';'.join(uniqueList(D2[k]))+'\t')
    ouFile.write('\t'.join(D[k])+'\n')
