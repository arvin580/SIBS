import sys
inF = 'ICC9B.unmapped.fa'
inF2 = 'ICC9B.unmapped.sam.mapped.fa.fa.blasted.top'
inF3 = '../ICC9B.unmapped'

inFile = open(inF)
D = dict()
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D.setdefault(head,[])
        D[head].append(seq)
    else:
        break
inFile.close()

inFile = open(inF3)
D2 = dict()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '>'+fields[0]
    D2.setdefault(k, [])
    D2[k].append(line)
inFile.close()

inFile = open(inF2)
ouFile = open(inF2 + '.seq1', 'w')
ouFile2 = open(inF2 + '.seq2', 'w')
ouFile3 = open(inF2 + '.seq3', 'w')

for line in inFile:
    line = line.strip()
    fields =line.split('\t')
    fs = fields[0].split(':')
    k = '>'+ ':'.join(fs[0:-1])
    if k in D:
        if len(D[k]) > 1:
            ouFile.write(k + '\n')
            for item in D[k]:  
                ouFile.write(item + '\n')
        elif k in D2:
            ouFile2.write(k + '\n')
            for item in D[k]:  
                ouFile2.write(item + '\t' + line + '\n')
            #ouFile2.write(k +'\t'+line+ '\n')
            ouFile2.write(k + '\n')
            for item in D2[k]:  
                if item.split('\t')[5]!='*':
                    ouFile2.write(item + '\n')
    else:
        ouFile3.write(k.strip('>') + '\n')

inFile.close()
ouFile.close()
ouFile2.close()
ouFile3.close()


