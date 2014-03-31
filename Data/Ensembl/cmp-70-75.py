D1 = {}
inFile = open('Homo_sapiens.GRCh37.75.pep.all.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D1[line2] = line1
    else:
        break
inFile.close()

D2 = {}
inFile = open('Homo_sapiens.GRCh37.75.pep.abinitio.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D2[line2] = line1
    else:
        break
inFile.close()

D3 = {}
inFile = open('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D3[line2] = line1
    else:
        break
inFile.close()



inFile = open('Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        if line2 in D1 :
            if line2 not in D3:
                print(line2)
    else:
        break
inFile.close()


