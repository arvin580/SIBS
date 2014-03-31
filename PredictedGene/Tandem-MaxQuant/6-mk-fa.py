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

inFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation.out')
ouFile = open('HeLa-Peptide-Predicted-Tandem-MaxQuant-New-NonMiss-Validation.out.fa', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    ch = fields[1]
    start = int(fields[8])
    end = int(fields[9])
    if start < end:
        seq = D[ch][start-1:end]
    else:
        seq = D[ch][end-1:start]
        seq = seq[::-1]
        seq = string.translate(seq,trans)
    ouFile.write(line + '\t' + seq + '\n')
        
inFile.close()
ouFile.close()
