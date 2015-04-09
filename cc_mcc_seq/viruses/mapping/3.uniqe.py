import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.fa', 'w')
D = dict()
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D[seq] = head
    else:
        break
inFile.close()

D2 = dict()
for k in D:
    D2.setdefault(D[k],0)
    D2[D[k]] += 1
    if sys.argv[1].find('B') !=-1 :
        ouFile.write(D[k]+':'+str(D2[D[k]])+'\n')
        ouFile.write(k+'\n')
    else:
        ouFile.write(D[k]+'\n')
        ouFile.write(k+'\n')

ouFile.close()
