inFile = open('tandem.peptides.is_stopgain_not_uniprot')
ouFile = open('tandem.peptides.real_stopgain', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[5].split(':')[-1]==']':
        start = int(fields[5].split(':')[0])
        end = int(fields[5].split(':')[1])

        ref = fields[4].split('+')[0].split(':')
        rstart = int(ref[-2])
        rend = int(ref[-1])

        ouFile.write(fields[0]+'\t')
        ouFile.write(fields[1]+'\t')
        ouFile.write(fields[2]+'\t')
        ouFile.write(fields[3]+'\t')
        ouFile.write(fields[4].split('+')[0]+':'+str(rstart+start-1)+':'+str(rstart+end-start)+'\t')
        ouFile.write(fields[5]+'\n')
inFile.close()
