D = {}
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19.chr.len')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = int(fields[1])
inFile.close()

chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
        'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

I = 10000

for ch in chs:
    #CHR = {}
    #for i in range(0,D[ch],I):
    #    CHR[str(i)+'\t'+str(i+I)]=0
    CHR = []
    inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-chr-site')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == ch:
            for k in CHR:
                if int(k.split('\t')[0])<=int(fields[1])<=int(k.split('\t')[1]):
                    CHR[k]+=1
    inFile.close()
    print(ch)
    for k in CHR:
        print(k)
        print(CHR[k])
   


'''
for ch in chs:
    L = [0]*D[ch]
    inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-chr-site')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == ch:
            L[int(fields[1])]+=1
    inFile.close()
    for i in range(len(L)) :
        if L[i] != 0:
            print(i)
            print(L[i])
'''    





