import string
Read = {}
inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/2-sv/ERR0498-04-05.unmapped.unique.fasta')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        Read[line1] = line2
    else:
        break
inFile.close()

Human = {}
inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        Human[line1] = line2
    else:
        break
inFile.close()

HPV = {}
inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/HPV-genome.fa')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        HPV[line1.split()[0]] = line2
    else:
        break
inFile.close()

trans = string.maketrans('ATCGatcg','TAGCtagc')


inFile = open('ha')
for line in inFile:
    line = line.strip('>\n')
    fields = line.split('\t')
    ch1 = fields[3]
    ch2 = fields[15]
    pos1_query = int(fields[8])
    pos2_query = int(fields[9])
    pos3_query = int(fields[20])
    pos4_query = int(fields[21])
    pos1_subject = int(fields[10])
    pos2_subject = int(fields[11])
    pos3_subject = int(fields[22])
    pos4_subject = int(fields[23])
    read = fields[0]
    print(Read[read])
    if ch1 == 'NC_001357.1':
        if pos3_subject < pos4_subject:
            seq=Human[ch2][pos3_subject-1:pos4_subject]
            print(seq)
        else:
            seq = string.translate(Human[ch2][pos4_subject-1:pos3_subject][::-1],trans)
            print(seq)
        if pos1_subject < pos2_subject:
            seq=HPV[ch1][pos1_subject-1:pos2_subject]
            print(seq)
        else:
            seq = string.translate(Human[ch1][pos2_subject-1:pos1_subject][::-1],trans)
            print(seq)
    else:
        if pos1_subject < pos2_subject:
            seq = Human[ch1][pos1_subject-1:pos2_subject]
            print(seq)
        else:
            seq = string.translate(Human[ch1][pos2_subject-1:pos1_subject][::-1],trans)
            print(seq)
        if pos3_subject < pos4_subject:
            seq =HPV[ch2][pos3_subject-1:pos4_subject]
            print(seq)
        else:
            seq = string.translate(Human[ch2][pos4_subject-1:pos3_subject][::-1],trans)
            print(seq)

inFile.close()
