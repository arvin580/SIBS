import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
D = {}
inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1[1:]] = line2
    else:
        break
inFile.close()

D2 = {}
inFile = open('/netshare1/home1/people/hansun/PredictedGene/Homo_sapiens.GRCh37.75.pep.abinitio.fa.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        gene = line1.split()[0]
        D2[gene] = line2
    else:
        break
inFile.close()



inFile = open('HeLa-Peptide-Validation-gene-dist2')
ouFile = open('HeLa-Peptide-Validation-gene-dist2-seq', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split()
    fds = fields[0].split(':')
    gene = fds[0]
    ch = fds[1]
    start = int(fds[2])
    end = int(fds[3])
    seq = D[ch][start-1:end]
    #seq_rev = seq[::-1]
    #seq_comp = string.translate(seq_rev, trans)
    ouFile.write(line + '\n')
    ouFile.write('>'+D2[gene] + '\n')
    ouFile.write(seq + '\n')
    #ouFile.write(seq_comp + '\n')
inFile.close()
ouFile.close()
