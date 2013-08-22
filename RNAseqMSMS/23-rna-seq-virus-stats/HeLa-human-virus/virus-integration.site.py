inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
ouFile1 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-site-before-3000','w')
ouFile2 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-site-after-3000','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
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

        if ch1 == 'NC_001357.1':
            if pos1_subject <= 3000 and pos2_subject <= 3000: 
                ouFile1.write(line1+'\n')
                ouFile1.write(line2+'\n')
            else:
                ouFile2.write(line1+'\n')
                ouFile2.write(line2+'\n')
        elif ch2 == 'NC_001357.1':
            if pos3_subject <= 3000 and pos4_subject <= 3000: 
                ouFile1.write(line1+'\n')
                ouFile1.write(line2+'\n')
            else:
                ouFile2.write(line1+'\n')
                ouFile2.write(line2+'\n')

            

    else:
        break



inFile.close()
ouFile1.close()
ouFile2.close()
