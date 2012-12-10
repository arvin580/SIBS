#!/usr/bin/env python
import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.merged', 'w')
pre = ['chrN', 'chrN', 0, 0]
interval = 500
row = 0
for line in inFile:
    row += 1
    line = line.strip()
    fields = line.split('\t')
    if fields[0] == pre[0] and fields[1] == pre[1]:
        if int(pre[2]) - interval <= int(fields[2]) <= int(pre[2]) + interval \
                and int(pre[3]) - interval <= int(fields[3]) <= int(pre[3]) + interval :
            ouFile.write(line + '\t')
        else:
            ouFile.write('\n')
            ouFile.write(line + '\t')

    else:
        if row ==1:
            ouFile.write(line + '\t')
        else:
            ouFile.write('\n')
            ouFile.write(line + '\t')
    pre = fields
        


inFile.close()
ouFile.close()
