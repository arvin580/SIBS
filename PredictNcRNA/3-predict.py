inFile = open('Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa')
S1 = inFile.read()
inFile.close()

inFile = open('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
S2 = inFile.read()
inFile.close()

inFile = open('human_uniprot_sprot.fa.fa')
S3 = inFile.read()
inFile.close()

inFile = open('ERR0498-04-05.fastq.pep')
ouFile = open('ERR0498-04-05.fastq.pep.predict2','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        if (line2 in S1)  and (line2 not in S3):
            ouFile.write(line1+'\n')
            ouFile.write(line2+'\n')
    else:
        break

inFile.close()
ouFile.close()
