D = {}
inFile = open('/netshare1/home1/people/hansun/Data/Uniprot/human_uniprot_sprot.fa')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        D[line1]= line2
    else:
        break
inFile.close()

inFile = open('/netshare1/home1/people/hansun/Data/Ensembl/Homo_sapiens.GRCh37.70.pep.all.fa.fa')
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    if line1:
        D[line1]= line2
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




inFile = open('HeLa-SNV-Virus-SV.fa')
ouFile1 = open('HeLa-SNV-Virus-SV-known.fa','w')
ouFile2 = open('HeLa-SNV-Virus-SV-new.fa','w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        flag = 0
        for k in D:
            if line2 in D[k]:
                if line1.find('Predict')==-1:
                    flag += 1
        if flag:
            ouFile1.write(line1+'\n')
            ouFile1.write(line2+'\n')
        else:
            ouFile2.write(line1+'\n')
            ouFile2.write(line2+'\n')
    else:
        break
        
inFile.close()
