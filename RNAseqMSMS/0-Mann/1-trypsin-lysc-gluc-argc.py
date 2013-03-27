inFile = open('msb201181-s2-peptides.txt')
ouFile1 = open('msb201181-s2-peptides-gluc.txt','w')
ouFile2 = open('msb201181-s2-peptides-lysc.txt','w')
ouFile3 = open('msb201181-s2-peptides-trypsin.txt','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields)>=3:
        if fields[-3]!='0':
            ouFile1.write(line+'\n')
        if fields[-2]!='0':
            ouFile2.write(line+'\n')
        if fields[-1]!='0':
            ouFile3.write(line+'\n')

inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()
