D = {}

def unique(inF):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            D[line2].append(line1)
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('')
unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')

ouFile = open('Homo_known-protein_filltered-snv_indel','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')

ouFile.close()

