inFile = open('Homo_sapiens.GRCh37.74.lncrna.fa.fa')
L = []
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        lh = len(line2)
        L.append(lh)
    else:
        break
inFile.close()
L.sort()
print(L)
