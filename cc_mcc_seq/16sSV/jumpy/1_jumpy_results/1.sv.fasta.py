import sys
inFile = open(sys.argv[1])
sv = {}
seq = []
L = 30
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
                'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
                        'chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
for line in inFile:
    line = line.strip()
    fields = line.split()
    if len(fields) > 2:
        if fields[0].find('chr')!=0:
            s = ''.join(fields[0:-1])
            n = 0
            for item in fields[0:-1]:
                if len(item)>L:
                    n += 1
            if n >= 2:
                seq.append(s)
        
        else:
            k = ''
            for item in fields:
                if item.find('>')==-1:
                    k = ':'.join([k, item])
                else:
                    k = ':'.join([k, item])
                    break
            sv[k] = seq
            seq = []

inFile.close()

ouFile = open(sys.argv[1].split('txt')[0]+'fasta','w')

for key in sv:
    if sv[key]:
        fields = key.split(':')
        if fields[1] in chrs and fields[3] in chrs:
            ouFile.write('>'+key+'\n')
            ouFile.write(sv[key][0]+'\n')

ouFile.close()
