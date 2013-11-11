## python 3.uniqe_reverse.py human_uniprot_sprot.fa
import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1][0:-3]+'_reversed.fa', 'w')
D = {}
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D.setdefault(seq,[])
        D[seq].append(head)
    else:
        break

inFile.close()

for k in D:
    ouFile.write('>'+'+++'.join([x.lstrip('>') for x in D[k]])+'\n')
    ouFile.write(k+ '\n')
    ouFile.write('>REVERSE:'+'+'.join([x.lstrip('>') for x in D[k]])+'\n')
    ouFile.write(k[::-1]+ '\n')

