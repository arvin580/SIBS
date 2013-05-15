import  sys
import string
D = {}
inFile = open('ucsc.hg19.fasta.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip().upper()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()
trans = string.maketrans('ATCG','TAGC')
for k in D:
    pos = D[k].find(sys.argv[1].upper())
    if pos != -1:
        print(k)
        print(pos)
    rev = string.translate(sys.argv[1].upper()[::-1],trans)
    pos = D[k].find(rev)
    if pos != -1:
        print(k+':'+'REVERSE')
        print(pos)

