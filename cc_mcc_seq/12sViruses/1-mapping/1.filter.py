import sys
head = 3537
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.mapped', 'w')
ouFile2 = open(sys.argv[1] + '.stat', 'w')
ouFile3 = open(sys.argv[1] + '.unmapped.fa', 'w')

for n in range(head):
    inFile.readline()

for line in inFile:
    fields = line.split('\t')
    flag = int(fields[1])
    D.setdefault(flag, 0)
    D[flag] += 1
    if flag != 4:
        ouFile.write(line)
    else:
        ouFile3.write('>'+fields[0]+'\n')
        ouFile3.write(fields[9]+'\n')


for k in D:
    ouFile2.write(str(k) + '\t' + str(D[k])+'\n')

inFile.close()
ouFile.close()
ouFile2.close()
ouFile3.close()




