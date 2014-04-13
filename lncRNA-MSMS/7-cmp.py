D = {}
ouFile = open('Homo_sapiens.GRCh37.lncrna.in_70.not_in_75.fa.fa','w')
inFile = open('Homo_sapiens.GRCh37.75.lncrna.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line2] = line1
    else:
        break
inFile.close()


inFile = open('Homo_sapiens.GRCh37.70.lncrna.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        if line2 not in D:
            ouFile.write(line1 + '\n')
            ouFile.write(line2 + '\n')
    else:
        break
inFile.close()
ouFile.close()

