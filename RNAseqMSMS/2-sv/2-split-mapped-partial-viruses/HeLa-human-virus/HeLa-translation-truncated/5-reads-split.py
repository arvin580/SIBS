inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-split','w')
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
        ouFile.write(line1+'\t'+line2+'\t'+str(pos1_query)+':'+str(pos2_query)+':'+line2[pos1_query-1:pos2_query]+'\t'+str(pos3_query)+':'+str(pos4_query)+':'+line2[pos3_query-1:pos4_query]+'\n')



    else:
        break
inFile.close()
