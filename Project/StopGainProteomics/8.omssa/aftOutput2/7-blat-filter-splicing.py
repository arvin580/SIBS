inFile = open('dna_protein_out1.anno')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>5:
        pep = fields[5]
        D.setdefault(pep,[])
    else:
        D[pep].append(fields[0])
        D[pep].append(fields[1])
        D[pep].append(fields[2])
        D[pep].append(fields[3])
        D[pep].append(fields[4])
inFile.close()

inFile = open('3-stopgain-protein-unique2-filtered.blated.filtered3')
ouFile = open('3-stopgain-protein-unique2-filtered.blated.filtered3.splicing','w')
ouFile2 = open('3-stopgain-protein-unique2-filtered.blated.filtered3.splicing.not','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pep = fields[0].split(':')[1]
    flag = 0
    for k in D:
        if k.find(pep)!=-1:
            ouFile.write(line+'\t'+k+'\t'+'\t'.join(D[k])+'\n')
            flag = 1
    if not flag:
        ouFile2.write(line+'\n')
    

inFile.close()
ouFile.close()
ouFile2.close()
