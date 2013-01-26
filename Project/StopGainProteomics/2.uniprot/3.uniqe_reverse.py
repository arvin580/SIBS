inFile = open('human_uniprot_sprot.fa')
ouFile = open('human_uniprot_sprot.reverse.fa', 'w')
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

