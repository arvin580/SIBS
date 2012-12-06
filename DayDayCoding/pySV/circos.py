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
            ouFile.write('trans' + str(link) + '\t' + fields[2] + '\t' + fields[3] + '\n')
            link += 1
            fields = line2.split('\t')
            ouFile.write('trans' + str(link) + '\t' + fields[2] + '\t' + fields[3] + '\n')

    else:
        break

inFile.close()
ouFile.close()
