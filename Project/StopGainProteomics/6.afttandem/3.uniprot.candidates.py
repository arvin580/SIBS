ouFile = open('tandem.peptides.uniprot.candidates', 'w')
inFile = open('tandem.peptides.is_stopgain_is_uniprot')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>5:    
        for i in range(4,len(fields),5):
            if fields[i].find('Uniprot')!=-1:
                start = int(fields[i+1].split(':')[0])
                end = int(fields[i+1].split(':')[1])

                ref = fields[i].split('+')[0].split(':')
                rstart = int(ref[-2])
                rend = int(ref[-1])

                ouFile.write(fields[0]+'\t')
                ouFile.write(fields[1]+'\t')
                ouFile.write(fields[2]+'\t')
                ouFile.write(fields[3]+'\t')
                ouFile.write(fields[i].split('+')[0]+':'+str(rstart+start-1)+':'+str(rstart+end-1)+'\t')
                ouFile.write(fields[i+1]+'\n')
                break
inFile.close()

inFile = open('tandem.peptides.not_stopgain_is_uniprot')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>5:    
        for i in range(4,len(fields),5):
            if fields[i].find('Uniprot')!=-1:
                start = int(fields[i+1].split(':')[0])
                end = int(fields[i+1].split(':')[1])

                ref = fields[i].split('+')[0].split(':')
                rstart = int(ref[-2])
                rend = int(ref[-1])

                ouFile.write(fields[0]+'\t')
                ouFile.write(fields[1]+'\t')
                ouFile.write(fields[2]+'\t')
                ouFile.write(fields[3]+'\t')
                ouFile.write(fields[i].split('+')[0]+':'+str(rstart+start-1)+':'+str(rstart+end-1)+'\t')
                ouFile.write(fields[i+1]+'\n')
                break
inFile.close()
ouFile.close()
