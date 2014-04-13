inFile = open('Homo_sapiens.GRCh37.70.ncrna.fa.fa')
ouFile = open('Homo_sapiens.GRCh37.70.lncrna.fa.fa', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        if line1.find('lncRNA') != -1 or line1.find('lincRNA') != -1:
        #if line1.find('transcript_biotype:lincRNA') != -1 :
            ouFile.write(line1 + '\n')
            ouFile.write(line2 + '\n')
    else:
        break

inFile.close()
ouFile.close()
