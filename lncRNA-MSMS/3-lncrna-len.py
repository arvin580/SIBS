inFile = open('Homo_sapiens.GRCh37.75.lncrna.fa.fa')
D = {}
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        lh = len(line2)
        D.setdefault(lh, [])
        D[lh].append(line1)
    else:
        break
inFile.close()
print(D[87])
