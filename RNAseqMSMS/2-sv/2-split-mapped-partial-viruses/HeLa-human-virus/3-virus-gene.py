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
D = {}
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene','w')
ouFile2 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene2','w')
ouFile3 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-gene3','w')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        ch1 = fields[3]
        start1 = int(fields[10])
        end1 = int(fields[11])
        start1_query = int(fields[8])
        end1_query = int(fields[9])
        ch2 = fields[15]
        start2 = int(fields[22])
        end2 = int(fields[23])
        start2_query= int(fields[20])
        end2_query=int(fields[21])
        if ch1 =='NC_001357.1' or ch2 =='NC_001357.1':
            for item in L:
                if (item[0]==ch1 and (item[1]<=start1 <= item[2] or item[1]<=end1<=item[2])) or \
                    (item[0]==ch2 and (item[1]<=start2 <= item[2] or item[1]<=end2<=item[2])):
                    D.setdefault(item[3], [])
                    D[item[3]].append(line1+'\t'+line2) 
    else:
        break
inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(len(set(x[1])),len(set(y[1]))),reverse=True)

for item in d:
    ouFile.write(item[0]+'\n')
    ouFile2.write(item[0]+'\t'+str(len(set(item[1])))+'\n')
    ouFile3.write(item[0]+'\t'+'\t'.join(set(item[1]))+'\n')

