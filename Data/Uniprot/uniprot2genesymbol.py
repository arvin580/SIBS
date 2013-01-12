inFile = open('/netshare1/home1/people/hansun/Data/Uniprot/gene_symbol_ensembl_id_uniprot_id')
ouFile = open('/netshare1/home1/people/hansun/Data/Uniprot/uniprot2genesymbol','w')
D = {}
for line in inFile:
    line = line.strip('\n')
    fields = line.split('\t')
    if fields[2]:
        D.setdefault(fields[2],[])
        D[fields[2]].append(fields[1])
inFile.close()
for k in D:
    D[k]=':'.join(set(D[k]))
for k in D:
    ouFile.write(k+'\t'+D[k]+'\n')
ouFile.close()

