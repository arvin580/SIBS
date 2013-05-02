def select_chr_region(inF,ch,start,end):
    inFile = open(inF)
    ouFile = open(inF+'-'+ch+'-'+str(start)+'-'+str(end),'w')
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
            if ch1 == ch:
                if start<= pos1_subject <= end or start<= pos2_subject <=end:
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')
            elif ch2 == ch:
                if start<= pos3_subject <= end or start<= pos4_subject <=end:
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')

        else:
            break
    inFile.close()
    ouFile.close()

#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr8',128230000,128250000)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',1420,1428)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',2236,2244)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',439,447)
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',3000,8000)
