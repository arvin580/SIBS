chrom=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8',
'chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

N=0
for ch in chrom :
    dict1=dict()
    inFile=open('coding.tmp')
    for line in inFile :
        line=line.strip()
        if line.split(':')[0]==ch :
            dict1[line]=0
    N+=len(dict1)
    print(len(dict1))
print(N)
        

