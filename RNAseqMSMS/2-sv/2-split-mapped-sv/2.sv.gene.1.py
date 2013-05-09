###  python ctx_gene.py  /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx

import sys

def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist


genes=[]
inFile1=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19_refGene.txt','r')

D = {}
for line in inFile1 :
    fields=line.split('\t')
    gene=[]
    gene.append(fields[0])
    gene.append(fields[1])
    gene.append(fields[2])
    gene.append(fields[3])
    gene.append(fields[4])
    gene.append(fields[5])
    gene.append(fields[12])
    genes.append(gene)

inFile1.close()

def sv(inF):
    inFile=open(inF)
    ouFile=open(inF+'.gene','w')
    
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields=line1.split('\t')
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
            flag = 0
            for it in genes :
                    if (ch1 == it[2]) and (int(it[4])<=int(start1)<=int(it[5]) or int(it[4])<=int(end1)<=int(it[5]) or (int(start1)<=int(it[4]) and int(end1)>=int(it[5]))) or (ch2 == it[2] and (int(it[4])<=int(start2)<=int(it[5]) or int(it[4])<=int(end2)<=int(it[5]) or (int(start2)<=int(it[4]) and int(end2)>=int(it[5])))):
                        gene = it[-1]
                        D.setdefault(gene,[])
                        D[gene].append(line1)
                        flag += 1

            ouFile.write(g+'\n')

        else:
            break
    
    
    inFile.close()
    ouFile.close()



sv('split-mapped-deletion')
#sv('split-mapped-inversion')
#sv('split-mapped-duplication')
#sv('split-mapped-translocation')
