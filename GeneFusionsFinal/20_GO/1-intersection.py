import re
inFile = open('FDR.pep.annotated.final')
ouFile = open('FDR.pep.annotated.final-intersection','w')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]]=1
inFile.close()

uniprot={}
inFile = open('human_uniprot_sprot.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        uniprot.setdefault(line2,[])
        s = re.search('GN=(\w+)',line1)
        if s:
            gene = s.group(1)
            uniprot[line2].append(gene)
    else:
        break

inFile.close()

inFile = open('FDR.pep.annotated.final.omssa')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] in D:
        for k in uniprot:
            if fields[0] in k:
                ouFile.write('\n'.join(set(uniprot[k]))+'\n')
inFile.close()

