D = {}
inFile = open('hg19_refGene.txt')
for line in inFile:
    fields = line.split('\t')
    D.setdefault(fields[1], 0)
    D[fields[1]]+=1
inFile.close()
for k in D:
    if D[k]>1:
        print(k)
