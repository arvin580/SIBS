L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[2]
    start = int(fields[4])
    end = int(fields[5])
    gene = fields[12]
    L.append([ch,start,end,gene])
inFile.close()
def gene(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'-human-gene','w')
    ouFile2 = open(inF+'-human-gene2','w')
    ouFile3 = open(inF+'-human-gene3','w')
    while True:
        line1 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            ch1 = fields[4]
            start1 = int(fields[11])
            end1 = int(fields[12])
            start1_query = int(fields[9])
            end1_query = int(fields[10])
            ch2 = fields[16]
            start2 = int(fields[23])
            end2 = int(fields[24])
            start2_query= int(fields[21])
            end2_query=int(fields[22])
            for item in L:
                if (item[0]==ch1 and (item[1]<=start1 <= item[2] or item[1]<=end1<=item[2])) or \
                        (item[0]==ch2 and (item[1]<=start2 <= item[2] or item[1]<=end2<=item[2])):
                    D.setdefault(item[3], [])
                    D[item[3]].append(line1) 
        else:
            break
    inFile.close()
    
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(set(x[1])),len(set(y[1]))),reverse=True)
    
    for item in d:
        ouFile.write(item[0]+'\n')
        ouFile2.write(item[0]+'\t'+str(len(set(item[1])))+'\n')
        ouFile3.write(item[0]+'\t'+'\t'.join(set(item[1]))+'\n')
#gene('ERR0498-04-05.unmapped.unique.human-viruse-checked')
#gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-1420-1428')
#gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-439-447')
#gene('ERR0498-04-05.unmapped.unique.human-viruse-checked-NC_001357.1-2236-2244')
gene('HeLa-predict-rnaseq-msms')
