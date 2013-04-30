inFile = open('ERR0498-04-05.unmapped.unique.human-viruse')
ouFile1 = open('ERR0498-04-05.unmapped.unique.human-viruse-high-quality','w')
ouFile2 = open('ERR0498-04-05.unmapped.unique.human-viruse-low-quality','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        ch1 = fields[3]
        ch2 = fields[15]
        if ch1 == 'NC_001357.1' or ch2 == 'NC_001357.1':
            pos1 = int(fields[8])
            pos2 = int(fields[9])
            pos3 = int(fields[20])
            pos4 = int(fields[21])
            
            if (1<= pos1 <=5 and 72<=pos4<=76 and -15<=pos3-pos2<=15) or \
                    (72 <= pos2 <= 76 and 1 <= pos3 <= 5 and  -15 <= pos1 - pos4 <= 15):
                        ouFile1.write(line1+'\n')
                        ouFile1.write(line2+'\n')
            else:
                ouFile2.write(line1 + '\n')
                ouFile2.write(line2 + '\n')

        pass
    else:
        break



inFile.close()
ouFile1.close()
ouFile2.close()
