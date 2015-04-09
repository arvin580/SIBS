import sys
inFile = open(sys.argv[1])
L = []
for line in inFile:
    line = line.strip()
    fields = line.split()
    L.append(fields)
inFile.close()

inFile = open('hg19_refGene.txt')
ouFile = open(sys.argv[1]+'.depth', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[2]
    start = int(fields[4])
    end = int(fields[5])
    gene = fields[12]
    nm = fields[1]
    normal_dep = 0
    #normal_len = 0
    tumor_dep = 0
    #tumor_len = 0
    for item in L:
        if item[0]==ch and start<=int(item[1])<=end and start<=int(item[2])<=end:
            normal_dep += float(item[4])
            #normal_len += int(item[3])
            tumor_dep += float(item[5])
            #tumor_len += int(item[3])
        #print(gene+'\t'+nm+'\t'+str(normal_dep)+'\t'+str(tumor_dep)+'\t'+str(normal_dep/normal_len)+'\t'+str(tumor_dep/tumor_len)+'\t'+str(tumor_dep/normal_dep))
    ouFile.write(gene+'\t'+nm+'\t'+ch+':'+str(start)+':'+str(end)+'\t'+str(normal_dep)+'\t'+str(tumor_dep)+'\t'+str((tumor_dep+1)/(normal_dep+1))+'\n')
inFile.close()
ouFile.close()

