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

inFile = open('Liver-SNV-INDEL-new-pep-gene')
ouFile1 = open('Liver-SNV-INDEL-new-pep-gene-new','w')
ouFile2 = open('Liver-SNV-INDEL-new-pep-gene-known','w')
for line in inFile:
    fields = line.split('\t')
    flag = 0
    for k in D:
        if fields[0] in D[k]:
            flag+=1
            break
    if flag:
        ouFile2.write('KNOWN'+'\t'+line)
    else:
        ouFile1.write('NEW'+'\t'+line)

inFile.close()
ouFile1.close()
ouFile2.close()
