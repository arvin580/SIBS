inFile = open('/netshare1/home1/people/hansun/Data/Lundberg/Illumina/ERR0498-04-05.sam')
ouFile1 = open('ERR0498-04-05.soft','w')
ouFile2 = open('ERR0498-04-05.unmapped','w')
for n in range(95):
    inFile.readline()
for line in inFile:
    fields = line.split('\t')
    if int(fields[1]) == 4:
        ouFile2.write(line)
    else:
        if fields[5].find('S')!=-1:
            ouFile1.write(line)
inFile.close()
ouFile1.close()
ouFile2.close()
