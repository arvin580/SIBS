'''
chr12   6879165 284
chr8    128241377       70   
chr12   6879323 69
'''
#chs = ['chr12','chr8']
#poss = [6879165,128241377,6879323]

chs = []
poss = []



inFile = open('ERR0498-04-05.unmapped.unique.human-viruse')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-check','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        ch1 = fields[3]
        ch2 = fields[15]
        if ch1 == 'NC_001357.1' or ch2 == 'NC_001357.1':
            pos1_query = int(fields[8])
            pos2_query = int(fields[9])
            pos3_query = int(fields[20])
            pos4_query = int(fields[21])
            pos1_subject = int(fields[10])
            pos2_subject = int(fields[11])
            pos3_subject = int(fields[22])
            pos4_subject = int(fields[23])
            if (ch1 in chs and (pos1_subject in poss or pos2_subject in poss)) or \
                    (ch2 in chs and (pos3_subject in poss or pos4_subject in poss)) :
                pass
            else:
                ouFile.write(line1+'\t'+line2+'\n')
    else:
        break
