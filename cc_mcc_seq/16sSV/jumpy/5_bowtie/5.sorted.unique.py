import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.unique', 'w')
D = {}
for line in inFile:
    line = line.strip()
    fields  = line.split('\t')
    ch = fields[0] + '\t' + fields[1]
    D.setdefault(ch , [fields + [int(fields[-2]) + int(fields[-1]) - 1000] + [int(fields[-2]) + int(fields[-1]) +1000]])
    flag = 0
    for item in D[ch]:
        if (int(fields[-2]) + int(fields[-1])) in xrange(item[-2], item[-1]):
            continue
        else:
            flag += 1
    if flag == len(D[ch]):
        D[ch].append(fields + [int(fields[-2]) + int(fields[-1]) - 1000] + [int(fields[-2]) + int(fields[-1]) +1000])

for k in D:
    for item in D[k]:
        print(item)



inFile.close()
ouFile.close()
