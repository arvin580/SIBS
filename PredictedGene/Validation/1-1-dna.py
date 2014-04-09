import string
trans = string.maketrans('atcgATCG','tagcTAGC')
D = {}
inFile = open('HeLa-Peptide-Validation2.txt')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split()
    dna = fields[1]
    dna_rev = dna[::-1]
    dna_rev = string.translate(dna_rev, trans)
    D[dna] = 1
    D[dna_rev] = 1
inFile.close()

'''
for k in D:
    head = k[3:len(k)/2]
    tail = k[len(k)/2:len(k)-3]
    print(k)
    print(head)
    print(tail)
'''
 
inFile = open('/netshare1/home1/people/hansun/Data/HeLa/Illumina/ERR0498-04-05.fastq')
ouFile = open('ERR0498-04-05-DNA2', 'w')
while True:
    line1 = inFile.readline().strip()
    seq = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()
    if line1:
        for k in D:
            head = k[3:len(k)/2]
            tail = k[len(k)/2:len(k)-3]
            if k in seq:
                ouFile.write('>FULL:' + k + '\n')
                ouFile.write(seq + '\n')
            if head in seq:
                ouFile.write('>HEAD:'+k+':' + head + '\n')
                ouFile.write(seq + '\n')
            if tail in seq:
                ouFile.write('>TAIL:'+k+':' + tail + '\n')
                ouFile.write(seq + '\n')
    else:
        break
inFile.close()
ouFile.close()
