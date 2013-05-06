D = {}
inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/2-sv/ERR0498-04-05.unmapped.unique.fasta')
while True:
    line1 = inFile.readline().strip('>\n')
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()

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
    print(D[read])


inFile.close()
