inFile = open('Homo_sapiens.GRCh37.75.lncrna.fa.fa.pep')
ouFile1 = open('Homo_sapiens.GRCh37.75.lncrna.fa.fa.pep-1', 'w')
ouFile2 = open('Homo_sapiens.GRCh37.75.lncrna.fa.fa.pep-2', 'w')
D = {}
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        if line2.find('*') == -1:
            ouFile1.write(line1+ '\n')
            ouFile1.write(line2+ '\n')
        else:
            peps = line2.split('*')
            for i,x in enumerate(peps):
                if len(x) >= 95:
                    D.setdefault(x, [])
                    D[x].append(line1 + ':' + str(i))
    else:
        for k in D:
            ouFile2.write('\t'.join(D[k])+'\n')
            ouFile2.write(k + '\n')
        break
inFile.close()
ouFile1.close()
ouFile2.close()
