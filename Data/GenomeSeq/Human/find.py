import  sys
import string
import re
chrs = ['>chr1','>chr2','>chr3','>chr4','>chr5','>chr6','>chr7','>chr8','>chr9','>chr10','>chr11','>chr12','>chr13','>chr14','>chr15','>chr16','>chr17','>chr18','>chr19','>chr20','>chr21','>chr22','>chrX','>chrY','>chrM']
D = {}
inFile = open('ucsc.hg19.fasta.fa')
ouFile = open('ucsc.hg19.fasta.fa'+'-'+''.join(sys.argv[1].split()),'w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip().upper()
    if line1 and line1 in chrs:
        D[line1] = line2
    else:
        break
inFile.close()
trans = string.maketrans('ATCG','TAGC')
for k in D:
    #pos = D[k].find(sys.argv[1].upper())
    #if pos != -1:
    #    print(k)
    #    print(pos)
    query = sys.argv[1].upper()
    for item in re.finditer(query,D[k]):
        ouFile.write(k+'\t'+str(item.start())+'\t'+item.group()+'\n')
    rev = string.translate(query[::-1],trans)
    for item in re.finditer(rev,D[k]):
        ouFile.write(k+'\t'+str(item.start())+'\t'+item.group()+'\n')
ouFile.close()
