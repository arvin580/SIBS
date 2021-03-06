D = {}
D2 = {}
inFile = open('/netshare1/home1/people/hansun/Data/Uniprot/human_uniprot_sprot.fa')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        D[line1]= line2
        D2[line1]= line2
    else:
        break
inFile.close()

inFile = open('/netshare1/home1/people/hansun/Data/Ensembl/Homo_sapiens.GRCh37.70.pep.all.fa.fa')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        D[line1]= line2
        D2[line1]= line2
    else:
        break
inFile.close()

inFile = open('/netshare1/home1/people/hansun/Data/Ensembl/Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        D[line1]= line2
    else:
        break
inFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new','w')
for line in inFile:
    fields = line.split('\t')
    flag = 0
    if fields[7].find('PREDICT')!=-1:
        for k in D2:
            if fields[4] in D2[k]:
                flag+=1
                break
        if flag:
            ouFile.write('KNOWN'+'\t'+line)
        else:
            ouFile.write('NEW'+'\t'+line)
    else:
        for k in D:
            if fields[4] in D[k]:
                flag+=1
                break
        if flag:
            ouFile.write('KNOWN'+'\t'+line)
        else:
            ouFile.write('NEW'+'\t'+line)

inFile.close()
ouFile.close()
