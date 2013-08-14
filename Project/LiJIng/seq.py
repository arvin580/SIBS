D = {}
inFile = open('human_uniprot_sprot.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        symbol = line1.split()[0]
        D[symbol] = [line1, line2]
    else:
        break
inFile.close()

D2 = {}
D3 = {}
inFile = open('PDB.fasta.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        symbol = line1
        D2[symbol] = [line1, line2]
        D3.setdefault(symbol, 0)
        D3[symbol] += 1
    else:
        break
inFile.close()
for k in D3:
    print(k)
    print(D3[k])


