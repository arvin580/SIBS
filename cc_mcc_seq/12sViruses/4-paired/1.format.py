import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.format', 'w')

D = dict()

ouFile.write('#' + sys.argv[1].split('.')[0] + '\n')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) > 1:
        if len(fields) == 13:
            ouFile.write(fields[0] + '\n')
            ouFile.write('\t'.join(fields[2:4] + fields[7:11])+'\n')
        else:
            ouFile.write(fields[9] + '\n')
            ouFile.write('\t'.join(fields[2:4]) + '\n')
            ouFile.write('\n')
    else:
        if sys.argv[1].find('B') == -1:
            ouFile.write(line + '\n')
        else:
            D.setdefault(fields[0], 0)
            D[fields[0]] += 1
            ouFile.write(line + ':' + str(D[fields[0]]) + '\n')




inFile.close()
ouFile.close()
