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

inFile = open('HeLa-Peptide-Validation-gene-dist')
ouFile = open('HeLa-Peptide-Validation-gene-dist-seq', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split()
    fds = fields[0].split(':')
    ch = fds[1]
    start = int(fds[2])
    end = int(fds[3])
    seq = D[ch][start-1:end]
    seq_rev = seq[::-1]
    seq_comp = string.translate(seq_rev, trans)
    ouFile.write(line + '\n')
    ouFile.write(seq + '\n')
    ouFile.write(seq_comp + '\n')
inFile.close()
ouFile.close()
