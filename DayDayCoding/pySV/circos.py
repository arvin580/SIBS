inFile = open('CHC10A.unmapped.trans.paired')
ouFile = open('CHC10A.unmapped.trans.paired.circos', 'w')

link = 0
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    
    if line1:
        if line1.split('\t')[2]!='chrM' and line2.split('\t')[2]!='chrM':
            link += 1
            fields = line1.split('\t')
            #ouFile.write('trans' + str(link) + '\t' + 'hs'+fields[2].split('chr')[1] + '\t' + str(int(fields[3])/1000000) + '\n')
            ouFile.write('trans' + str(link) + '\t' + 'hs'+fields[2].split('chr')[1] + '\t' + fields[3] + '\t' + str(int(fields[3])+500) + '\n')
            fields = line2.split('\t')
            ouFile.write('trans' + str(link) + '\t' + 'hs'+fields[2].split('chr')[1] + '\t' + fields[3] + '\t' + str(int(fields[3])+500) + '\n')

    else:
        break

inFile.close()
ouFile.close()
