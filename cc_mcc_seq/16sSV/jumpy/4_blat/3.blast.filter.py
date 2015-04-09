import sys


chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

identity = 95
size = 90
if sys.argv[1].find('ICC4A') != -1:
    size = 60

D = {}
def blat():
    inFile = open(sys.argv[1])
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields) > 3:
            if float(fields[2]) >= identity and float(fields[3]) >= size:
                D.setdefault(fields[0], [])
                D[fields[0]].append(line)
    inFile.close()

blat()


inFile = open(sys.argv[1].split('.blated')[0])
ouFile = open(sys.argv[1] + '.unique', 'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()

    if line1:
        k1 = line1.lstrip('>')
        k2 = line3.lstrip('>')

        if k1 in D and k2 in D:
            if len(D[k1]) == 1 and len(D[k2]) == 1:
                ch1 = D[k1][0].split('\t')[1]
                ch2 = D[k2][0].split('\t')[1]
                if ch1 in chrs and ch2 in chrs and ch1 != ch2:
                    ouFile.write(D[k1][0] + '\n')
                    ouFile.write(line2 + '\n')
                    ouFile.write(D[k2][0] + '\n')
                    ouFile.write(line4 + '\n')

    else:
        break



inFile.close()
ouFile.close()

