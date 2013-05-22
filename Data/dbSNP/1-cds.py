L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    fields = line.split('\t')
    L.append([fields[2],int(fields[6]),int(fields[7])])
inFile.close()

inFile = open('hg19_snp137.txt')
ouFile = open('hg19_snp137.cds','w')
for line in inFile:
    fields = line.split('\t')
    for item in L:
        if item[0] == fields[1] and item[1] <= int(fields[2]) <= item[2]:
            ouFile.write(line)
            break
inFile.close()
ouFile.close()
