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
inFile = open('PDB.fasta.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        symbol = line1
        D2[symbol] = [line1, line2]
    else:
        break
inFile.close()

inFile = open('PDB-blasted')
ouFile = open('PDB-blasted-seq.txt', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    head1 = fields[1]
    head2 = fields[0]
    ouFile.write(line + '\t' + D2[head2][0] + '\t' + D2[head2][1] + '\t' + D[head1][0] +'\t'+D[head1][1] + '\n')
inFile.close()
ouFile.close()




