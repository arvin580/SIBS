inFile = open('human_uniprot_sprot.digested.stopgain.fa')
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
    print('>'+'+'.join([x.lstrip('>') for x in D[k]]))
    print(k)

